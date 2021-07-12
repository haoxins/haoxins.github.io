#!/usr/bin/env python3


fmt_md() {
  MD_FILE="./$MD_FILE"

  if [ -f $MD_FILE ]; then
    cat $MD_FILE | \
    tr '\t' ' ' | \
    tr '’' "'" | \
    tr '‘' "'" | \
    tr '“' '"' | \
    tr '”' '"' | \
    tr '（' '(' | \
    tr '）' ')' | \
    tr '【' '[' | \
    tr '】' ']' | \
    tr '《' '<' | \
    tr '》' '>' | \
    tr '，' ', ' | \
    tr '、' ', ' | \
    tr '。' '. ' | \
    tr '；' '; ' | \
    tr '：' ': ' | \
    tr '！' '! ' | \
    tr '？' '? ' > \
    $MD_FILE
  else
    echo "$MD_FILE does not exist."
  fi
}

MD_FILES=`git add --all && git status -s | grep '.md' | grep -E 'A|M' | cut -c 2- | xargs`

for MD_FILE in $MD_FILES
do
  fmt_md
done
