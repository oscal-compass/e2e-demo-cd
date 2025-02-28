# Copyright (c) 2025 The OSCAL Compass Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limit
"""OSCAL transformation tasks."""
import argparse
import logging
import pathlib

from cis_cd_helper import CisCdHelper

from cis_to_nist_mapping_helper import CisToNistMappingHelper

from cis_yml_helper import CisYmlHelper

from nist_cd_helper import NistCdSoftwareHelper
from nist_cd_helper import NistCdValidationHelper

logging.basicConfig(
    level=logging.WARNING,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s %(levelname)s %(message)s',  # Log message format
)

logger = logging.getLogger(__name__)


class CisToNist():
    """CisToNist."""

    def __init__(self) -> None:
        """Initialize."""
        parser = argparse.ArgumentParser()
        parser.add_argument('--cis-yml', required=True, help='CIS yml')
        parser.add_argument('--cis-cd', required=True, help='CIS component definition')
        parser.add_argument('--cis-nist-mapping', required=True, help='CIS to NIST mapping')
        parser.add_argument('--nist-cd-software', required=True, help='NIST 800-53 software component definition')
        parser.add_argument('--nist-cd-validation', required=True, help='NIST 800-53 validation component definition')
        parser.add_argument('--nist-catalog', required=True, help='NIST 800-53 catalog')
        self.args = parser.parse_args()
        self._init_cis_yml_helper()
        self._init_cis_cd_helper()
        self._init_nist_cd_software_helper()
        self._init_nist_cd_validation_helper()
        self._init_cis_to_nist_mapping_helper()

    def _init_cis_yml_helper(self):
        """Initialize cis_yml helper."""
        ipath = pathlib.Path(self.args.cis_yml)
        self.cis_yml_helper = CisYmlHelper(ipath)

    def _init_cis_cd_helper(self):
        """Initialize cis_cd helper."""
        ipath = pathlib.Path(self.args.cis_cd)
        self.cis_cd_helper = CisCdHelper(ipath)

    def _init_nist_cd_software_helper(self):
        """Initialize nist cd software helper."""
        ipath = pathlib.Path(self.args.nist_cd_software)
        title = self.args.nist_cd_software
        title = title.replace('component-definitions', '')
        title = title.replace('component-definition.json', '')
        title = title.replace('/', '')
        title = title.replace('_', ' ')
        title = title.replace('800 53', '800-53')
        version = self.cis_cd_helper.get_version()
        source = self.args.nist_catalog
        self.nist_cd_software_helper = NistCdSoftwareHelper(ipath, title, version, source)

    def _init_nist_cd_validation_helper(self):
        """Initialize nist cd validation helper."""
        ipath = pathlib.Path(self.args.nist_cd_validation)
        title = self.args.nist_cd_software
        title = title.replace('component-definitions', '')
        title = title.replace('component-definition.json', '')
        title = title.replace('/', '')
        title = title.replace('_', ' ')
        title = title.replace('800 53', '800-53')
        version = self.cis_cd_helper.get_version()
        self.nist_cd_validation_helper = NistCdValidationHelper(ipath, title, version, self.cis_yml_helper)

    def _init_cis_to_nist_mapping_helper(self):
        """Initialize cis_nist_mapping helper."""
        ipath = pathlib.Path(self.args.cis_nist_mapping)
        self.cis_to_nist_mapping_helper = CisToNistMappingHelper(ipath)

    def process(self):
        """Process."""
        cis_cd_controls = self.cis_cd_helper.get_controls()
        logger.debug(f'cis controls: {cis_cd_controls}')
        cis_to_nist_controls_map = self.cis_to_nist_mapping_helper.get_map(cis_cd_controls)
        logger.debug(f'cis-to-nist controls map: {cis_to_nist_controls_map}')
        nist_to_cis_controls_map = self.cis_to_nist_mapping_helper.get_map_reverse(cis_cd_controls)
        logger.debug(f'nist-to-cis controls map: {nist_to_cis_controls_map}')
        # create cds
        for nist_control in nist_to_cis_controls_map.keys():
            cis_control_list = nist_to_cis_controls_map[nist_control]
            for control_id in cis_control_list:
                rule_ids = self.cis_cd_helper.get_rules_for_control(control_id)
                rule_texts = self.cis_yml_helper.get_rule_texts_for_rule_id_list(rule_ids)
                self.nist_cd_software_helper.add_control(nist_control, rule_texts)
                self.nist_cd_validation_helper.add_checks(rule_texts)
        self.nist_cd_software_helper.add_rule_sets(self.cis_yml_helper)
        self.nist_cd_software_helper.write_component_definition()
        self.nist_cd_validation_helper.write_component_definition()


def main():
    """Start."""
    obj = CisToNist()
    obj.process()


if __name__ == '__main__':
    main()
