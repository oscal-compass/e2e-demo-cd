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
import json
import pathlib
from typing import List

from trestle.oscal.component import ImplementedRequirement


class CisCdHelper():
    """CisCd helper."""

    def __init__(self, ipath: pathlib.Path) -> None:
        """Initialize."""
        with open(ipath, 'r') as f:
            self.jdata = json.load(f)

    def get_version(self) -> str:
        """Get version."""
        component_definition = self.jdata['component-definition']
        metadata = component_definition['metadata']
        version = metadata['version']
        return version

    def get_controls(self) -> List[str]:
        """Get controls."""
        rval = []
        implemented_requirements = self.get_implemented_requirements()
        for implemented_requirement in implemented_requirements:
            control_id = implemented_requirement['control-id']
            if control_id not in rval:
                rval.append(control_id)
        return sorted(rval, key=CisCdHelper.ctl_id_key)

    def get_rules_for_control(self, control_id: str) -> List[str]:
        """Get rules for control."""
        rval = []
        implemented_requirements = self.get_implemented_requirements()
        for implemented_requirement in implemented_requirements:
            if control_id == implemented_requirement['control-id']:
                for prop in implemented_requirement['props']:
                    if prop['name'] == 'Rule_Id':
                        rule_id = prop['value'].replace('CIS-', '')
                        if rule_id not in rval:
                            rval.append(rule_id)
                break
        return rval

    def get_implemented_requirements(self) -> List[ImplementedRequirement]:
        """Get implemented requirements."""
        component_definition = self.jdata['component-definition']
        components = component_definition['components']
        component = components[0]
        control_implementations = component['control-implementations']
        control_implementation = control_implementations[0]
        implemented_requirements = control_implementation['implemented-requirements']
        return implemented_requirements

    @staticmethod
    def ctl_id_key(ctl_id):
        """Sort."""
        numeric_part = ctl_id.split('-')[1]
        return [int(part) for part in numeric_part.split('.')]
