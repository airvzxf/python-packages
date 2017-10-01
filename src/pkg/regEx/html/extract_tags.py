#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re


def get_from_tag(tag=None, text="", ignore_case=True, multi_matches=False):
    if tag is None:
        return

    if multi_matches:
        return []
    else:
        return __search_from_tag_reg_ex(tag, text, ignore_case)

    return


def __search_from_tag_reg_ex(tag=None, text="", ignore_case=True):
    if tag is None:
        return

    reg_ex_string = r"<{0}[^<]+?>(.*)</{0}>".format(tag)

    if ignore_case:
        pattern_get_from_tag = re.compile(reg_ex_string, re.DOTALL | re.IGNORECASE)
    else:
        pattern_get_from_tag = re.compile(reg_ex_string, re.DOTALL)

    matches = re.search(pattern_get_from_tag, text)

    if matches is not None:
        return matches.group(1)

    return


def get_from_comment(text=""):
    print("text: ", text)
    return
