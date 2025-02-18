
echo "Regenerating assessment results" 

trestle task xccdf-result-to-oscal-ar -c data/cis_rhel9_scan.config
