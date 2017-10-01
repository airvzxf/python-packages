#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re


def get_from_tag(tag=None, text=""):
    if tag is None:
        return

    # RegEx
    # https://regex101.com/r/aYOgRZ/2
    reg_ex_string = r"<{0}[^<]+?>(.*)</{0}>".format(tag)
    pattern_get_from_tag = re.compile(reg_ex_string, re.MULTILINE)
    matches = re.search(pattern_get_from_tag, text)

    if matches is not None:
        # return matches.index(1)
        return matches.group(1)

    return


def get_from_comment(text=""):
    print("text: ", text)
    return
