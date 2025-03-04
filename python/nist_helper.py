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


class NisHelper():
    """Nist helper."""

    @classmethod
    def _classify(cls, label: str) -> int:
        """Classify label."""
        return label.count('(')

    @classmethod
    def _is_number(cls, subject: str) -> bool:
        """Check if string is an integer."""
        try:
            int(subject)
            return True
        except ValueError:
            return False

    @staticmethod
    def _convert(label: str) -> str:
        """Control label to statement."""
        normalized_label = label.lower().replace(' ', '').strip()
        if normalized_label.endswith('(0)'):
            normalized_label = normalized_label.rsplit('(', 1)[0]
        class_ = NisHelper._classify(normalized_label)
        if class_ == 0:
            statement = f'{normalized_label}'
        elif class_ == 1:
            parts = normalized_label.split('(')
            p0 = parts[0]
            parts = parts[1].split(')')
            p1 = parts[0]
            if NisHelper._is_number(p1):
                statement = f'{p0}.{p1}'
            else:
                statement = f'{p0}_smt.{p1}'
        elif class_ == 2:
            parts = normalized_label.split('(')
            p0 = parts[0]
            p1 = parts[1].replace(')', '')
            p2 = parts[2].replace(')', '')
            statement = f'{p0}.{p1}_smt.{p2}'
        else:
            text = f'unexpceted classification {class_} for label {label}'
            raise RuntimeError(text)
        return statement

    @staticmethod
    def label_to_statement(label: str) -> str:
        """Label to statement."""
        normalized_label = label.lower().replace(' ', '').strip()
        value = NisHelper._convert(normalized_label)
        return value
