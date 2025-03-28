version_tag=$1
for d in ./component-definitions/* ; do
   compdef=$(basename "$d")
   if ! find "md_components/$compdef" -mindepth 1 -not -name ".*" -print -quit | grep -q .; then
      echo "Directory md_components/$compdef is empty, skipping..."
      continue
   fi
   echo "Assembling ${compdef}" 
   if [ "$1" != "" ]; then 
      trestle author component-assemble --name $compdef --markdown md_components/$compdef --output $compdef --version $version_tag 
   else
      trestle author component-assemble --name $compdef --markdown md_components/$compdef --output $compdef
   fi
done
