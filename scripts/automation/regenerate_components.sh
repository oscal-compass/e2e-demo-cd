for d in ./component-definitions/* ; do
    compdef=$(basename "$d")
    echo "Regenerating ${compdef}" 
    trestle author component-generate --output md_components/$compdef --name $compdef
done
