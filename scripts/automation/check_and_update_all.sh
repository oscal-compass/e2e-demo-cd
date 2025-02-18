#!/bin/bash

CHANGES=`git diff-tree --no-commit-id --name-only -r HEAD`

xml_changed=false

xml1=$"^data/"
xml2=$"\.xml$"

for val in ${CHANGES[@]} ; do
  if [[ $val =~ $xml1 && $val =~ $xml2 ]]; then
    xml_changed=true
  fi
done

if [[ $xml_changed = true ]]; then
    echo "xml changed, regenerating OSCAL observations..."
    ./scripts/automation/regenerate_observations.sh
fi

echo "$xml_changed"
