#!/bin/bash

CHANGES=`git diff-tree --no-commit-id --name-only -r HEAD`

src_changed=false

# bash regex does not support lazy match, so need to use two patterns to match before and after the control id

xlsx1=$"^data/"
xlsx2=$"\.xlsx$"

yml1=$"^data/"
yml2=$"\.yml$"

config1=$"^data/"
config2=$"\.config$"

catalog1=$"^catalogs/"
catalog2=$"\.json$"

profile1=$"^profiles/"
profile2=$"\.json$"

for val in ${CHANGES[@]} ; do
  if [[ $val =~ $xlsx1 && $val =~ $xlsx2 ]]; then
    src_changed=true
  fi

  if [[ $val =~ $yml1 && $val =~ $yml2 ]]; then
    src_changed=true
  fi
  
  if [[ $val =~ $config1 && $val =~ $config2 ]]; then
    src_changed=true
  fi
  
  if [[ $val =~ $catalog1 && $val =~ $catalog2 ]]; then
    src_changed=true
  fi
  
  if [[ $val =~ $profile1 && $val =~ $profile2 ]]; then
    src_changed=true
  fi
done

if [[ $src_changed = true ]]; then
    echo "Source file(s) were changed regenerating component definitions..."
    ./scripts/automation/regenerate_components.sh
fi

echo "$src_changed"
