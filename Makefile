
.ONESHELL:
SHELL := /bin/bash

SOURCE_INIT = /tmp/venv.trestle
SOURCE = $(SOURCE_INIT)

all: venv cd
all-clean: clean venv cd

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

cd: cd-sw

cd-sw:
	echo "=> cd-sw"; \
	source $(SOURCE)/bin/activate; \
	trestle task cis-xlsx-to-oscal-cd -c data/cis-xlsx-to-oscal-cd.snippet.config
	python python/cisb_to_nist_cd.py --cis-yml data/cis_ubuntu2404.yml --cis-cd component-definitions/Cis_Ubuntu_Linux_24.04_LTS/component-definition.json --nist-cd component-definitions/NIST_800_53_Ubuntu_Linux_24.04_LTS/component-definition.json --cis-nist-mapping data/CIS_Controls_v8_Mapping_to_NIST_SP_800_53_Rev_5_Moderate_and_Low_Base.xlsx --nist-catalog catalogs/NIST_800-53_rev5/catalog.json 