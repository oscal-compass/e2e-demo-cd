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

from nist_csv_helper import NistCsvSoftwareHelper
from nist_csv_helper import NistCsvValidationHelper

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
        #
        parser.add_argument('--nist-csv-software', required=True, help='trestle csv software file path')
        parser.add_argument(
            '--nist-csv-software-component-title', required=True, help='trestle csv software component title'
        )
        parser.add_argument(
            '--nist-csv-software-component-description',
            required=False,
            help='trestle csv software component description',
            default=None
        )
        #
        parser.add_argument('--nist-csv-validation', required=True, help='trestle csv validation file path')
        parser.add_argument(
            '--nist-csv-validation-component-title', required=True, help='trestle validation csv component title'
        )
        parser.add_argument(
            '--nist-csv-validation-component-description',
            required=False,
            help='trestle validation csv component description',
            default=None
        )
        parser.add_argument(
            '--nist-csv-validation-check-prefix', required=True, help='trestle validation csv check prefix'
        )
        #
        parser.add_argument('--nist-csv-profile-source', required=True, help='trestle csv profile source')
        parser.add_argument('--nist-csv-profile-description', required=True, help='trestle csv profile description')
        self.args = parser.parse_args()
        self._init_cis_yml_helper()
        self._init_cis_cd_helper()
        self._init_nist_csv_software_helper()
        self._init_nist_csv_validation_helper()
        self._init_cis_to_nist_mapping_helper()

    def _init_cis_yml_helper(self):
        """Initialize cis_yml helper."""
        ipath = pathlib.Path(self.args.cis_yml)
        self.cis_yml_helper = CisYmlHelper(ipath)

    def _init_cis_cd_helper(self):
        """Initialize cis_cd helper."""
        ipath = pathlib.Path(self.args.cis_cd)
        self.cis_cd_helper = CisCdHelper(ipath)

    def _init_nist_csv_software_helper(self):
        """Initialize nist csv software helper."""
        ipath = pathlib.Path(self.args.nist_csv_software)
        component_title = self.args.nist_csv_software_component_title
        component_title = component_title.replace(' ', '_')
        component_description = self.args.nist_csv_software_component_description
        if not component_description:
            component_description = component_title
        component_description = component_description.replace('_', ' ')
        profile_source = self.args.nist_csv_profile_source
        profile_description = self.args.nist_csv_profile_description
        self.nist_csv_software_helper = NistCsvSoftwareHelper(
            ipath, component_title, component_description, profile_source, profile_description
        )

    def _init_nist_csv_validation_helper(self):
        """Initialize nist csv validation helper."""
        ipath = pathlib.Path(self.args.nist_csv_validation)
        component_title = self.args.nist_csv_validation_component_title
        component_title = component_title.replace(' ', '_')
        component_description = self.args.nist_csv_validation_component_description
        if not component_description:
            component_description = component_title
        component_description = component_description.replace('_', ' ')
        check_prefix = self.args.nist_csv_validation_check_prefix
        target_component = self.args.nist_csv_software_component_title
        target_component = target_component.replace(' ', '_')
        self.nist_csv_validation_helper = NistCsvValidationHelper(
            ipath, component_title, component_description, check_prefix, target_component
        )

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
                self.nist_csv_software_helper.add_control(nist_control, rule_texts)
                self.nist_csv_validation_helper.add_checks(nist_control, rule_texts)
        self.nist_csv_software_helper.generate_csv()
        self.nist_csv_validation_helper.generate_csv()


def main():
    """Start."""
    obj = CisToNist()
    obj.process()


if __name__ == '__main__':
    main()
