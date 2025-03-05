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
import csv
import os
import pathlib
from typing import List

from nist_helper import NisHelper

from trestle.tasks.csv_to_oscal_cd import CHECK_DESCRIPTION
from trestle.tasks.csv_to_oscal_cd import CHECK_ID
from trestle.tasks.csv_to_oscal_cd import COMPONENT_DESCRIPTION
from trestle.tasks.csv_to_oscal_cd import COMPONENT_TITLE
from trestle.tasks.csv_to_oscal_cd import COMPONENT_TYPE
from trestle.tasks.csv_to_oscal_cd import CONTROL_ID_LIST
from trestle.tasks.csv_to_oscal_cd import HEADER_DECORATION_CHAR
from trestle.tasks.csv_to_oscal_cd import NAMESPACE
from trestle.tasks.csv_to_oscal_cd import PROFILE_DESCRIPTION
from trestle.tasks.csv_to_oscal_cd import PROFILE_SOURCE
from trestle.tasks.csv_to_oscal_cd import RULE_DESCRIPTION
from trestle.tasks.csv_to_oscal_cd import RULE_ID
from trestle.tasks.csv_to_oscal_cd import TARGET_COMPONENT

optional = f'{HEADER_DECORATION_CHAR}'
required = f'{HEADER_DECORATION_CHAR}{HEADER_DECORATION_CHAR}'
h1_component_title = f'{required}{COMPONENT_TITLE}'
h1_component_description = f'{required}{COMPONENT_DESCRIPTION}'
h1_component_type = f'{required}{COMPONENT_TYPE}'
h1_rule_id = f'{required}{RULE_ID}'
h1_rule_description = f'{required}{RULE_DESCRIPTION}'
h1_profile_source = f'{required}{PROFILE_SOURCE}'
h1_profile_description = f'{required}{PROFILE_DESCRIPTION}'
h1_control_id_list = f'{required}{CONTROL_ID_LIST}'
h1_namespace = f'{required}{NAMESPACE}'
h1_check_id = f'{optional}{CHECK_ID}'
h1_check_description = f'{optional}{CHECK_DESCRIPTION}'
h1_target_component = f'{optional}{TARGET_COMPONENT}'

h2_component_title = 'A human readable name for the component.'  # noqa: E501
h2_component_description = 'A description of the component including information about its function.'  # noqa: E501
h2_component_type = 'A category describing the purpose of the component. ALLOWED VALUES interconnection:software:hardware:service:physical:process-procedure:plan:guidance:standard:validation.'  # noqa: E501
h2_rule_id = 'A textual label that uniquely identifies a policy (desired state) that can be used to reference it elsewhere in this or other documents.'  # noqa: E501
h2_rule_description = 'A description of the policy (desired state) including information about its purpose and scope.'  # noqa: E501
h2_profile_source = 'A URL reference to the source catalog or profile for which this component is implementing controls for. A profile designates a selection and configuration of controls from one or more catalogs.'  # noqa: E501
h2_profile_description = 'A description of the profile.'  # noqa: E501
h2_control_id_list = 'A list of textual labels that uniquely identify the controls or statements that the component implements.'  # noqa: E501
h2_namespace = 'A namespace qualifying the property\'s name. This allows different organizations to associate distinct semantics with the same name. Used in conjunction with "class" as the ontology concept.'  # noqa: E501
h2_check_id = 'A textual label that uniquely identifies a check of the policy (desired state) that can be used to reference it elsewhere in this or other documents.'  # noqa: E501
h2_check_description = 'A description of the check of the policy (desired state) including the method (interview or examine or test) and procedure details.'  # noqa: E501
h2_target_component = 'The name of the target component.'  # noqa: E501

row_h1s = [
    h1_component_title,
    h1_component_description,
    h1_component_type,
    h1_rule_id,
    h1_rule_description,
    h1_profile_source,
    h1_profile_description,
    h1_control_id_list,
    h1_namespace
]

row_h2s = [
    h2_component_title,
    h2_component_description,
    h2_component_type,
    h2_rule_id,
    h2_rule_description,
    h2_profile_source,
    h2_profile_description,
    h2_control_id_list,
    h2_namespace
]

row_h1v = [
    h1_component_title,
    h1_component_description,
    h1_component_type,
    h1_rule_id,
    h1_rule_description,
    h1_profile_source,
    h1_profile_description,
    h1_control_id_list,
    h1_namespace,
    h1_check_id,
    h1_check_description,
    h1_target_component
]

row_h2v = [
    h2_component_title,
    h2_component_description,
    h2_component_type,
    h2_rule_id,
    h2_rule_description,
    h2_profile_source,
    h2_profile_description,
    h2_control_id_list,
    h2_namespace,
    h2_check_id,
    h2_check_description,
    h2_target_component
]


class _NistCsvHelper():
    """NistCsv software helper."""

    def __init__(
        self,
        ipath: pathlib.Path,
        component_title: str,
        component_description: str,
    ) -> None:
        """Initialize."""
        self.ipath = ipath
        os.makedirs(self.ipath.parent, exist_ok=True)
        self.rows = []
        self.component_title = component_title
        self.component_description = component_description
        self.component_type = '?'
        self.namespace = 'https://oscal-compass/compliance-trestle/schemas/oscal/cd'

    def write_csv(self) -> None:
        """Write csv."""
        with open(self.ipath, 'w', newline='', encoding='utf8') as f:
            csv_writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            for row in self.rows:
                csv_writer.writerow(row)


class NistCsvSoftwareHelper(_NistCsvHelper):
    """NistCsv software helper."""

    def __init__(
        self,
        ipath: pathlib.Path,
        component_title: str,
        component_description: str,
        profile_source: str,
        profile_description: str
    ) -> None:
        """Initialize."""
        _NistCsvHelper.__init__(self, ipath, component_title, component_description)
        self.profile_source = profile_source
        self.profile_description = profile_description
        self.component_type = 'software'
        self.rows.append(row_h1s)
        self.rows.append(row_h2s)
        self._map = {}

    def add_control(self, label: str, rule_texts: List[str]) -> None:
        """Add control."""
        for rule_text in rule_texts:
            if rule_text not in self._map.keys():
                self._map[rule_text] = []
            statement = NisHelper.label_to_statement(label)
            if statement not in self._map[rule_text]:
                self._map[rule_text].append(statement)

    def generate_csv(self):
        """Generate csv."""
        for key in self._map.keys():
            rule_id = key
            rule_description = key
            control_id_list = ' '.join(self._map[key])
            row = [
                self.component_title,
                self.component_description,
                self.component_type,
                rule_id,
                rule_description,
                self.profile_source,
                self.profile_description,
                control_id_list,
                self.namespace
            ]
            self.rows.append(row)
        self.write_csv()


class NistCsvValidationHelper(_NistCsvHelper):
    """NistCsv validation helper."""

    def __init__(
        self,
        ipath: pathlib.Path,
        component_title: str,
        component_description: str,
        check_prefix: str,
        target_component: str
    ) -> None:
        """Initialize."""
        _NistCsvHelper.__init__(self, ipath, component_title, component_description)
        self.check_prefix = check_prefix
        self.target_component = target_component
        self.component_type = 'validation'
        self.rows.append(row_h1v)
        self.rows.append(row_h2v)
        self._map = {}

    def add_checks(self, label: str, rule_texts: List[str]) -> None:
        """Add checks."""
        for rule_text in rule_texts:
            if rule_text not in self._map.keys():
                self._map[rule_text] = []

    def generate_csv(self):
        """Generate csv."""
        rule_description = ''
        profile_source = ''
        profile_description = ''
        control_id_list = ''
        for key in self._map.keys():
            rule_id = key
            check_id = key
            check_description = key
            control_id_list = ' '.join(self._map[key])
            row = [
                self.component_title,
                self.component_description,
                self.component_type,
                rule_id,
                rule_description,
                profile_source,
                profile_description,
                control_id_list,
                self.namespace,
                f'{self.check_prefix}{check_id}',
                f'{self.check_prefix}{check_description}',
                self.target_component
            ]
            self.rows.append(row)
        self.write_csv()
