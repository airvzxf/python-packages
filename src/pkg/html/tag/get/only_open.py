#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Search all HTML tags which start with a specific opened tag.
"""

import re

from pkg.html.tag.regex.get_compilation_flags import get_compilation_flags
from pkg.html.tag.regex.get_open import get_open as get_opened_tag
from pkg.regex.get.compiled_list import compiled_list


def only_open(tag=None, text="", ignore_case=True):
    """
    Search HTML tags starting with a specific opened tag.

    :param tag: HTML tag like div, article, body, etc., looks like <div, <body.
    :param text: The HTML source code.
    :param ignore_case: If is true it should be search in lowercase and uppercase.
    :return: List with the matched tags.
    """
    flags = get_compilation_flags(ignore_case=ignore_case)

    pattern_list = [get_opened_tag(tag)]

    regex_tag = compiled_list(pattern_list, flags)

    tags = re.findall(regex_tag, text)

    return tags
