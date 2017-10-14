#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Search all HTML tags which start with a specific opened tag."""

import re

from src.pkg.html.tag.regex.get_open import get_open as get_opened_tag


def only_open(tag='', text=""):
    """Search HTML tags starting with a specific opened tag.

    :param tag: HTML tag like div, article, body, etc., looks like <div, <body.
    :param text: The HTML source code.
    :return: List with the matched tags.
    """
    if tag is None:
        return

    flags = re.RegexFlag.DOTALL

    regex_tag = re.compile(get_opened_tag(tag), flags)

    tags = re.findall(regex_tag, text)

    return tags
