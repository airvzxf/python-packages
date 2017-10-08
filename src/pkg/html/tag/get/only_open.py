#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

from src.pkg.html.tag.regex.get_open import get_open as get_opened_tag


def only_open(tag='', text=""):
    if tag is None:
        return

    flags = re.RegexFlag.DOTALL

    regex_tag = re.compile(get_opened_tag(tag), flags)

    tags = []

    for tag in re.finditer(regex_tag, text):
        tags.append(tag.group())

    return tags
