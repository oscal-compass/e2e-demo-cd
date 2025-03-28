trestle task csv-to-oscal-cd -c data/csv-to-oscal-cd-software.config
trestle task csv-to-oscal-cd -c data/csv-to-oscal-cd-validation.config
trestle author component-generate -n Ubuntu_Linux_24.04_LTS -o md_components/Ubuntu_Linux_24.04_LTS
trestle author component-generate -n oscap -o md_components/oscap