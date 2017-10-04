#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re


def raw_content_from(tag=None, text="", ignore_case=True):
    if tag is None:
        return

    return __regex_html_tag_started_at(tag, text, ignore_case)


def __regex_html_tag_started_at(tag=None, text="", ignore_case=True):
    if tag is None:
        return

    flags = re.RegexFlag.DOTALL
    if ignore_case:
        flags = flags | re.RegexFlag.IGNORECASE

    reg_ex_html_tag = r"<{0}[^<]*?>(.*)</{0}>".format(tag)

    pattern_get_from_tag = re.compile(reg_ex_html_tag, flags)

    matches = re.search(pattern_get_from_tag, text)

    if matches is not None:
        return matches.group(1)

    return
