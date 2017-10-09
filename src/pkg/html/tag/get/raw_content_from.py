#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

from src.pkg.html.tag.regex.get_raw_open_close import get_raw_open_close as get_raw_opened_closed_tag


def raw_content_from(tag=None, text="", ignore_case=True):
    if tag is None:
        return

    return __regex_html_tag_started_at(tag, text, ignore_case)


def __regex_html_tag_started_at(tag=None, text="", ignore_case=True):
    if tag is None:
        return

    flags = re.RegexFlag.DOTALL

    if ignore_case:
        flags = re.RegexFlag.DOTALL | re.RegexFlag.IGNORECASE

    pattern_get_from_tag = re.compile(get_raw_opened_closed_tag(tag), flags)

    matches = re.search(pattern_get_from_tag, text)

    if matches is not None:
        return matches.group(1)

    return
