#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Get get all properties inside of the HTML tag.
"""

import re

from pkg.html.tag.regex.get_compilation_flags import get_compilation_flags
from pkg.html.tag.regex.get_open import get_open as get_opened_tag
from pkg.html.tag.regex.get_properties import get_properties
from pkg.regex.get.compiled_list import compiled_list


def all_properties(tag=None, text="", trim=True, ignore_case=True):
    """
    Get get all properties inside of the HTML tag.

    :param tag: HTML tag like div, article, body, etc., looks like <div, <body.
    :param text: The HTML source code.
    :param trim: If is true, it delete all the white spaces before and after the text.
    :param ignore_case: If is true it should be search in lowercase and uppercase.
    :return: List with the matched tags.
    """
    flags = get_compilation_flags(ignore_case=ignore_case)

    pattern_list = [get_opened_tag(tag),
                    get_properties(trim)]

    regex_tag, regex_properties = compiled_list(pattern_list, flags)

    tags = []

    for tag in re.finditer(regex_tag, text):
        extracted_properties = re.findall(regex_properties, tag.group())

        properties = []

        for tag_property in extracted_properties:
            properties.append((tag_property[0], tag_property[2]))

        tags.append(properties)

    return tags
