#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Search a specific opened HTML tag and all the code inside until the last closed tag."""

import re

from src.pkg.html.tag.regex.get_raw_open_close import get_raw_open_close as get_raw_opened_closed_tag


def raw_content_from(tag=None, text="", ignore_case=True):
    """Search from opened HTML tag until the last closed tag.

    :param tag: HTML tag like div, article, body, etc., looks like <div, <body.
    :param text: The HTML source code.
    :param ignore_case: If is true, it should be search in lowercase and uppercase.
    :return: A string with the match.
    """
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
