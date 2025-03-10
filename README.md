# End-to-End Demo: Ubuntu Component Definitions
Repository to demo oscal based component definitions and agile authoring using compliance-trestle and github actions

The [demo overview](https://github.com/oscal-compass/e2e-demo).

1. Input: It was initialized with OSCAL catalog.json, profile.json, [Ubuntu yml](https://github.com/ComplianceAsCode/content/blob/master/controls/cis_ubuntu2404.yml) from ComplianceAsCode, and control selections specified in spread sheets.

2. Processing: Changes to any of the input files will cause regeneration of the `software` and `validation` component definitions.

    - [type=software Component Definition](component-definitions/Ubuntu_Linux_24.04_LTS/component-definition.json)
    - [type=validation Component Definition](component-definitions/oscap/component-definition.json)

3. Output: Updated component-definition.json files in component-definition repo

4. Next action: Updated component-definition.json files pushed to ssp repo

Demo for this repo:

- Show changes to spread sheet (delete control, re-add control) are incorporated into component-definition.json files