#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Helps to handle the tag validation.
"""

import re


def helper_tag_validation(tag=None, ignore_case=False):
    """
    Handle the regEx flags and return the flags enum.

    :param tag:
    :param ignore_case: If is true, it should be search in lowercase and uppercase.
    :return: re.RegexFlag Enum
    """
    if tag is None:
        raise AttributeError("Tag shouldn't be None.")

    flags = re.RegexFlag.DOTALL

    if ignore_case:
        flags |= re.RegexFlag.IGNORECASE

    return flags
