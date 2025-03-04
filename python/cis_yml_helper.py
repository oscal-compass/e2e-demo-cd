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
import pathlib
from typing import List

from ruamel.yaml import YAML


class CisYmlHelper():
    """CisYml helper."""

    def __init__(self, path: pathlib.Path) -> None:
        """Initialize."""
        yaml = YAML(typ='safe')
        self.ydata = yaml.load(path)

    def get_rule_texts_for_rule_id(self, rule_id: str) -> List[str]:
        """Get rule texts for rule_id."""
        rval = []
        control_list = self.ydata['controls']
        for control in control_list:
            if control['id'] != rule_id:
                continue
            rule_texts = control.get('rules', '')
            for rule_text in rule_texts:
                if rule_text in rval:
                    continue
                if '=' in rule_text:
                    continue
                rval.append(rule_text)
        return rval

    def get_rule_texts_for_rule_id_list(self, rule_id_list: List[str]):
        """Get rule texts for rule_id list."""
        rval = []
        for rule_id in rule_id_list:
            rule_texts = self.get_rule_texts_for_rule_id(rule_id)
            for rule_text in rule_texts:
                if rule_text in rval:
                    continue
                if '=' in rule_text:
                    continue
                rval.append(rule_text)
        return sorted(rval)

    def get_rule_description_for_rule_text(self, rule_text: str) -> str:
        """Get rule description for rule_text."""
        return self._get_control_key_value_for_rule_text(rule_text, 'title')

    def get_rule_status_for_rule_text(self, rule_text: str) -> str:
        """Get rule status for rule_text."""
        return self._get_control_key_value_for_rule_text(rule_text, 'status')

    def get_rule_levels_for_rule_text(self, rule_text: str) -> str:
        """Get rule levels for rule_text."""
        return self._get_control_key_value_for_rule_text(rule_text, 'levels')

    def _get_control_key_value_for_rule_text(self, rule_text: str, control_key: str) -> str:
        """Get rule descriptions for rule_text."""
        value_list = []
        control_list = self.ydata['controls']
        for control in control_list:
            rule_texts = control.get('rules', '')
            if rule_text not in rule_texts:
                continue
            value = control[control_key]
            if isinstance(value, list):
                value = '; '.join(value).strip()
            if value not in value_list:
                value_list.append(value)
        rval = '; '.join(value_list).strip()
        return rval
