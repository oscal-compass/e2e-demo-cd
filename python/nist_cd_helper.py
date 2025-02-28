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
import datetime
import os
import pathlib
import uuid
from math import log10
from typing import List

from cis_yml_helper import CisYmlHelper

from oscal_helper import OscalHelper

from trestle.oscal import OSCAL_VERSION
from trestle.oscal.common import Metadata
from trestle.oscal.common import Property
from trestle.oscal.component import ComponentDefinition
from trestle.oscal.component import ControlImplementation
from trestle.oscal.component import DefinedComponent
from trestle.oscal.component import ImplementedRequirement


class NistCdSoftwareHelper():
    """NistCd software helper."""

    timestamp = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
    ns = 'https://oscal-compass/compliance-trestle/schemas/oscal/cd'
    prefix_rule_set = 'rule_set_'

    def __init__(self, ipath: pathlib.Path, title: str, version: str, source: str) -> None:
        """Initialize."""
        self.ipath = ipath
        os.makedirs(self.ipath.parent, exist_ok=True)
        self.title = title
        self.version = version
        self.component_type = 'software'
        self.component_title = title
        self.component_description = title
        self.source = source
        self.source_description = source.replace('catalogs', '').replace('catalog.json', '').replace('/', '')
        self.implemented_requirements = {}
        self.component_props = []
        self.rule_text_list = []

    def add_control(self, control_id: str, rule_texts: list[str]) -> None:
        """Add control."""
        normalized_control_id = OscalHelper.normalize_control(control_id)
        if normalized_control_id not in self.implemented_requirements.keys():
            implemented_requirement = ImplementedRequirement(
                uuid=str(uuid.uuid4()),
                control_id=normalized_control_id,
                description='',
            )
            implemented_requirement.props = []
            for rule_text in rule_texts:
                prop = Property(
                    name='Rule_Id',
                    value=rule_text,
                    ns=NistCdSoftwareHelper.ns,
                )
                implemented_requirement.props.append(prop)
                if rule_text not in self.rule_text_list:
                    self.rule_text_list.append(rule_text)
            self.implemented_requirements[control_id] = implemented_requirement

    def add_rule_sets(self, cis_yml_helper: CisYmlHelper):
        """Add rule sets."""
        rule_set_number_digits = len(self.rule_text_list) + 1
        fill_size = int(log10(rule_set_number_digits)) + 1
        for index, rule_text in enumerate(self.rule_text_list):
            rule_set_id = f'{NistCdSoftwareHelper.prefix_rule_set}{str(index).zfill(fill_size)}'
            #
            prop = Property(name='Rule_Id', value=rule_text, ns=NistCdSoftwareHelper.ns, remarks=rule_set_id)
            self.component_props.append(prop)
            #
            rule_description = cis_yml_helper.get_rule_description_for_rule_text(rule_text)
            prop = Property(
                name='Rule_Description', value=rule_description, ns=NistCdSoftwareHelper.ns, remarks=rule_set_id
            )
            self.component_props.append(prop)
            #
            rule_status = cis_yml_helper.get_rule_status_for_rule_text(rule_text)
            prop = Property(name='Rule_Status', value=rule_status, ns=NistCdSoftwareHelper.ns, remarks=rule_set_id)
            self.component_props.append(prop)
            #
            rule_levels = cis_yml_helper.get_rule_levels_for_rule_text(rule_text)
            prop = Property(name='Rule_Levels', value=rule_levels, ns=NistCdSoftwareHelper.ns, remarks=rule_set_id)
            self.component_props.append(prop)

    def get_metadata(self) -> None:
        """Metadata."""
        metadata = Metadata(
            title=self.title,
            last_modified=NistCdSoftwareHelper.timestamp,
            oscal_version=OSCAL_VERSION,
            version=self.version,
        )
        return metadata

    def get_component(self) -> DefinedComponent:
        """Get component."""
        component = DefinedComponent(
            uuid=str(uuid.uuid4()),
            type=self.component_type,
            title=self.component_title,
            description=self.component_description,
            props=self.component_props,
            control_implementations=[self.get_control_implementation()],
        )
        return component

    def get_implemented_requirements(self) -> List[ImplementedRequirement]:
        """Get implemented requirements."""
        rval = []
        keys = sorted(self.implemented_requirements.keys())
        for key in keys:
            rval.append(self.implemented_requirements[key])
        return rval

    def get_control_implementation(self) -> List[ControlImplementation]:
        """Get control implementations."""
        control_implementation = ControlImplementation(
            uuid=str(uuid.uuid4()),
            source=self.source,
            description=self.source_description,
            implemented_requirements=self.get_implemented_requirements(),
        )
        return control_implementation

    def write_component_definition(self) -> None:
        """Write component definition."""
        self.component_definition = ComponentDefinition(
            uuid=str(uuid.uuid4()),
            metadata=self.get_metadata(),
            components=[self.get_component()],
        )
        self.component_definition.oscal_write(pathlib.Path(self.ipath))
