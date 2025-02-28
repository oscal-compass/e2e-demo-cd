#!/bin/bash

CHANGES=`git diff-tree --no-commit-id --name-only -r HEAD`

md_changed=false
json_changed=false
xlsx_changed=false
profile_changed=false
catalog_changed=false

# bash regex does not support lazy match, so need to use two patterns to match before and after the control id
md1=$"^md_components/"
md2=$"\.md$"

json1=$"^component-definitions/"
json2=$"\.json$"

xlsx1=$"^data/"
xlsx2=$"\.xlsx$"

profile1=$"^profiles/"
profile2=$"\.json$"

catalog1=$"^catalogs/"
catalog2=$"\.json$"

for val in ${CHANGES[@]} ; do
  if [[ $val =~ $md1 && $val =~ $md2 ]]; then
    md_changed=true
  fi

  if [[ $val =~ $json1 && $val =~ $json2 ]]; then
    json_changed=true
  fi
  
  if [[ $val =~ $xlsx1 && $val =~ $xlsx2 ]]; then
    xlsx_changed=true
  fi
  
  if [[ $val =~ $profile1 && $val =~ $profile2 ]]; then
    profile_changed=true
  fi
  
  if [[ $val =~ $catalog1 && $val =~ $catalog2 ]]; then
    catalog_changed=true
  fi
done

if [[ $xlsx_changed = true ]]; then
    echo "CSV file(s) were changed, generating component JSON and regenerating markdowns..."
    trestle task cis-xlsx-to-oscal-cd -c data/cis-xlsx-to-oscal-cd.config
    ./scripts/automation/regenerate_components.sh
fi

if [[ $json_changed = true ]]; then
    echo "Json file(s) were changed, regenerating markdowns..."
    ./scripts/automation/regenerate_components.sh
fi

if [[ $catalog_changed = true ]]; then
    echo "Catalog file(s) were changed, regenerating markdowns..."
    ./scripts/automation/regenerate_components.sh
fi

if [[ $profile_changed = true ]]; then
    echo "Profile file(s) were changed, regenerating markdowns..."
    ./scripts/automation/regenerate_components.sh
fi


if [[ $md_changed = true ]]; then
    echo "Md file(s) were changed, assembling markdowns..."
    ./scripts/automation/assemble_components.sh
fi


echo "$md_changed $json_changed $xlsx_changed"
