#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Helps to handle the python regEx flags filtering by parameters.
"""

import re


def helper_regex_flags(ignore_case=False):
    """
    Handle the regEx flags and return the flags enum.

    :param ignore_case: If is true, it should be search in lowercase and uppercase.
    :return: re.RegexFlag Enum
    """
    flags = re.RegexFlag.DOTALL

    if ignore_case:
        flags |= re.RegexFlag.IGNORECASE

    return flags
