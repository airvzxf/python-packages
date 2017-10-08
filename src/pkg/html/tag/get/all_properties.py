#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

from src.pkg.html.tag.regex.get_open import get_open as get_opened_tag
from src.pkg.html.tag.regex.get_properties import get_properties


def all_properties(tag=None, text="", trim=True):
    if tag is None:
        return

    flags = re.RegexFlag.DOTALL

    regex_tag = re.compile(get_opened_tag(tag), flags)
    regex_properties = re.compile(get_properties(trim), flags)

    tags = []

    for tag in re.finditer(regex_tag, text):
        extracted_properties = re.findall(regex_properties, tag.group())

        properties = []

        for tag_property in extracted_properties:
            properties.append((tag_property[0], tag_property[2]))

        tags.append(properties)

    return tags
