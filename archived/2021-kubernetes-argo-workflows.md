---
title: Kube stack - Argo workflows, Kubeflow pipelines
description: 日月之行, 若出其中; 星汉灿烂, 若出其里. 幸甚至哉, 歌以咏志.
date: 2021-09-04
---

## Argo workflows

* Argo Workflows is implemented as a Kubernetes CRD.
  - `Workflow`: a Kubernetes resource defining
    the execution of one or more *template*.
    Workflows are named.
  - `Template`: a *step*, *steps* or *dag*.
  - `Step`: a single step of a *workflow*,
    typically run a container based on
    *inputs* and capture the *outputs*.
  - `Steps`: a list of *steps*
  - `Entrypoint`: the first *step* to execute
    when running a *workflow*
  - `Node`: a step
  - `Directed Acyclic Graph` (**DAG**): a set of
    *steps* (nodes) and the *dependencies* (edges) between them.
  - `Workflow Template`: a Kubernetes resource defining
    a reusable workflow for a namespace.
  - `Cluster Workflow Template`: a Kubernetes resource
    defining a reusable workflow for a cluster.
  - `Inputs`: *parameters* and *artifacts* passed to the *step*
  - `Outputs`: *parameters* and *artifacts* outputed by a *step*
  - `Parameters`: objects, strings, booleans, arrays
  - `Artifacts`: files saved by a container
  - `Artifact Repository`: a place where *artifacts* are stored
  - `Executor`: the method to execute a container
  - `Workflow Service Account`: the service account that
    a workflow is executed as

* [Argo Workflows](https://github.com/argoproj/argo-workflows)
* [Argo Events](https://github.com/argoproj/argo-events)
  - The *Event-driven Workflow Automation* Framework

```yaml
- name: gen-random-int
  script:
    image: python:alpine3.6
    command: [python]
    source: |
      import random
      i = random.randint(1, 100)
      print(i)
---
- name: k8s-owner-reference
  resource:
    action: create
    manifest: |
      apiVersion: v1
      kind: ConfigMap
      metadata:
        generateName: owned-eg-
      data:
        some: value
```

```yaml
- name: hello-hello-hello
  steps:
  - - name: step1
      template: prepare-data
  - - name: step2a
      template: run-data-first-half
    - name: step2b
      template: run-data-second-half
---
- name: diamond
  dag:
    tasks:
    - name: A
      template: echo
    - name: B
      dependencies: [A]
      template: echo
    - name: C
      dependencies: [A]
      template: echo
    - name: D
      dependencies: [B, C]
      template: echo
```

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: hello-world-parameters-
spec:
  entrypoint: whalesay
  arguments:
    parameters:
    - name: message
      value: hello world
  templates:
  - name: whalesay
    inputs:
      parameters:
      - name: message
    container:
      image: docker/whalesay
      command: [ cowsay ]
      args: [ "{{inputs.parameters.message}}" ]
```

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: empty-dir-
spec:
  entrypoint: main
  templates:
  - name: main
    container:
      image: argoproj/argosay:v2
      command: [sh, -c]
      args: ["cowsay hello world | tee /mnt/out/hello_world.txt"]
      volumeMounts:
      - name: out
        mountPath: /mnt/out
    volumes:
    - name: out
      emptyDir: {}
    outputs:
      parameters:
      - name: message
        valueFrom:
          path: /mnt/out/hello_world.txt
```

```yaml
apiVersion: argoproj.io/v1alpha1
kind: CronWorkflow
metadata:
  name: test-cron-wf
spec:
  schedule: "* * * * *"
  concurrencyPolicy: Replace
  startingDeadlineSeconds: 0
  workflowSpec:
    entrypoint: whalesay
    templates:
    - name: whalesay
      container:
        image: alpine:3.6
        command: [sh, -c]
        args: ["date; sleep 90"]
```

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: http-template-
spec:
  entrypoint: main
  templates:
  - name: main
    steps:
    - - name: good
        template: http
        arguments:
          parameters: [{name: url, value: "https://a.com/b.json"}]
  - name: http
    inputs:
      parameters:
      - name: url
    http:
     url: "{{inputs.parameters.url}}"
```

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: container-set-template-
spec:
  entrypoint: main
  templates:
  - name: main
    volumes:
    - name: workspace
      emptyDir: {}
    containerSet:
      volumeMounts:
      - mountPath: /workspace
        name: workspace
      containers:
      - name: a
        image: argoproj/argosay:v2
      - name: b
        image: argoproj/argosay:v2
      - name: main
        image: argoproj/argosay:v2
        dependencies:
        - a
        - b
    outputs:
      parameters:
      - name: message
        valueFrom:
          path: /workpsace/message
```

## Kubeflow pipelines

* *Python* code -> **KFP** *Python* library -> **Argo** workflow YAMLs
