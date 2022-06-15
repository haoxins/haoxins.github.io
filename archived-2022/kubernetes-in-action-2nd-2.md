---
title: Kubernetes in Action (中) - 2nd Edition
description: 树木丛生, 百草丰茂. 秋风萧瑟, 洪波涌起.
date: 2021-09-07
---

- [Kubernetes in Action, Second Edition](https://book.douban.com/subject/34986745/)
  - https://www.manning.com/books/kubernetes-in-action-second-edition

## Deploying stateful workloads with StatefulSets

- Therefore, to deploy a MongoDB replica set in Kubernetes,
  you need to ensure that:
  - each Pod has its own `PersistentVolume`,
  - each Pod is addressable by its own unique address,
  - when a Pod is deleted and replaced,
    the new Pod is assigned the same
    address and `PersistentVolume`.

```
As with Deployments, in a StatefulSet you specify a Pod template,
the desired number of replicas, and a label selector.
However, you can also specify a PersistentVolumeClaim template.

Each time the StatefulSet controller creates a new replica,
it creates not only a new Pod object,
but also one or more PersistentVolumeClaim objects.
```

```
When a StatefulSet Pod is deleted and recreated,
it's given the same name as the Pod it replaced.
Also, a Pod with a particular ordinal number is always
associated with PersistentVolumeClaims with the same number.

When you create a StatefulSet, only the first Pod is created initially.
Then the StatefulSet controller waits until the Pod is ready
before creating the next one.
```

- When using a __headless__ Service with a StatefulSet,
  an additional DNS record is created for each Pod so that
  the IP address of each Pod can be looked up by its name.
  - This is how stateful Pods maintain their stable network identity.
  - These DNS records don't exist when the __headless__ Service
    isn't associated with a StatefulSet.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: quiz-pods
spec:
  clusterIP: None
  publishNotReadyAddresses: true
  selector:
    app: quiz
  ports:
  - name: mongodb
    port: 27017
```

- In the listing, the `clusterIP` field is set to `None`,
  which makes this a __headless__ Service.
- If you set `publishNotReadyAddresses` to `true`,
  the DNS records for each Pod are created immediately when
  the Pod is created, rather than only when the Pod is ready.

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: quiz
spec:
  serviceName: quiz-pods
  podManagementPolicy: Parallel
  replicas: 3
  selector:
    matchLabels:
      app: quiz
  template:
    metadata:
      labels:
        app: quiz
        ver: "0.1"
    spec:
      volumes:
      - name: db-data
        persistentVolumeClaim:
          claimName: db-data
      containers:
      - name: quiz-api
        ...
      - name: mongo
        ...
        volumeMounts:
        - name: db-data
          mountPath: /data/db
  volumeClaimTemplates:
  - metadata:
      name: db-data
      labels:
        app: quiz
    spec:
      resources:
        requests:
          storage: 10Gi
      accessModes:
      - ReadWriteOnce
```

- In the `serviceName` field, for example,
  you specify the name of the headless Service
  that governs this StatefulSet.
- By setting `podManagementPolicy` to `Parallel`,
  the StatefulSet controller creates all Pods simultaneously.
- Unlike the Pod templates, where you omit the name field,
  you __must__ specify the name in the `PersistentVolumeClaim` template.
  - This name __must__ match the name in the
    volumes section of the Pod template.

---

- The only label you defined in the Pod template in the
  StatefulSet manifest was `app`, but the StatefulSet
  controller added two additional labels to the Pod:
  - The label `controller-revision-hash` serves the same
    purpose as the label `pod-template-hash` on the
    Pods of a ReplicaSet.
  - It allows the controller to determine to which
    revision of the StatefulSet a particular Pod belongs.
  - The label `statefulset.kubernetes.io/pod-name` specifies
    the Pod name and allows you to create a Service for
    a specific Pod instance by using this label in
    the Service's label selector.
- Since this Pod object is managed by the StatefulSet,
  the `ownerReferences` field indicates this fact.
  - Unlike Deployments, where Pods are owned by ReplicaSets,
    which in turn are owned by the Deployment,
  - StatefulSets own the Pods directly.
- The Pod's containers match the containers defined
  in the StatefulSet's Pod template, but that's
  __not__ the case for the Pod's volumes.
  - In the template you specified the `claimName` as `db-data`,
    but here in the Pod it's been changed to `db-data-quiz-0`.
  - This is because each Pod instance gets its own
    `PersistentVolumeClaim`.
  - The name of the claim is made up of the `claimName`
    and the name of the Pod.

---


### Understanding StatefulSet behavior
