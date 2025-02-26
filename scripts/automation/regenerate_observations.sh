
echo "Regenerating assessment results" 

trestle task xccdf-result-to-oscal-ar -c data/scan.config
