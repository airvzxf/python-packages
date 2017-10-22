#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Get get all properties inside of the HTML tag.
"""

import re

from pkg.html.tag.regex.get_open import get_open as get_opened_tag
from pkg.html.tag.regex.get_properties import get_properties


def all_properties(tag=None, text="", trim=True):
    """
    Get get all properties inside of the HTML tag.

    :param tag: HTML tag like div, article, body, etc., looks like <div, <body.
    :param text: The HTML source code.
    :param trim: If is true, it delete all the white spaces before and after the text.
    :return: List with the matched tags.
    """
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
