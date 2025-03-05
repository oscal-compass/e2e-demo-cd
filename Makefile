
.ONESHELL:
SHELL := /bin/bash

SOURCE_INIT = /tmp/venv.trestle
SOURCE = $(SOURCE_INIT)

CIS_YML = --cis-yml data/cis_ubuntu2404.yml

CIS_MAP = --cis-nist-mapping data/CIS_Controls_v8_Mapping_to_NIST_SP_800_53_Rev_5_Moderate_and_Low_Base.xlsx

CSV_SW = --nist-csv-software data/csv/NIST_800_53_Ubuntu_Linux_24.04_LTS.software.csv
CSV_SW_TITLE = --nist-csv-software-component-title "Ubuntu Linux 24.04 LTS"
CSV_VAL = --nist-csv-validation data/csv/NIST_800_53_Ubuntu_Linux_24.04_LTS.validation.csv
CSV_VAL_TITLE = --nist-csv-validation-component-title "oscap"
CSV_VAL_CHECK_PREFIX = --nist-csv-validation-check-prefix xccdf_org.ssgproject.content_rule_

CSV_PROF_SRC = --nist-csv-profile-source profiles/NIST_800-53_rev5_selected/profile.json
CSV_PROF_DESC = --nist-csv-profile-description "NIST SP 800-53 Rev 5 Controls, selected"

CIS_CD = --cis-cd component-definitions/Cis_Ubuntu_Linux_24.04_LTS/component-definition.json

all: venv comp-defs
all-clean: clean all

.SILENT: clean
clean: clean-venv

.SILENT: clean-venv
clean-venv:
	rm -fr $(SOURCE_INIT)

.SILENT: venv
venv:
	if [ ! -d $(SOURCE_INIT) ]; then \
		echo "=> create python virtual environment"; \
		python -m venv $(SOURCE_INIT); \
		source $(SOURCE_INIT)/bin/activate; \
		echo "=> install prereqs"; \
		python -m pip install -q --upgrade pip setuptools; \
		python -m pip install -q compliance-trestle; \
	fi

comp-defs:
	echo "=> cd-sw"; \
	source $(SOURCE)/bin/activate; \
	trestle task cis-xlsx-to-oscal-cd -c data/cis-xlsx-to-oscal-cd.snippet.config; \
	python python/cisb_to_nist_cd.py $(CIS_YML) $(CIS_MAP) $(CIS_CD) $(CSV_SW) $(CSV_SW_TITLE) $(CSV_VAL) $(CSV_VAL_TITLE) $(CSV_VAL_CHECK_PREFIX) $(CSV_PROF_SRC) $(CSV_PROF_DESC); \
	trestle task csv-to-oscal-cd -c data/csv-to-oscal-cd-software.config; \
	trestle task csv-to-oscal-cd -c data/csv-to-oscal-cd-validation.config; \
	
	