#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Get a list of RegEx patterns and return a compiled list.
"""

from re import compile


def compiled_list(patterns=None, flags=0):
    """
    Return a list with the compiled patterns.

    :param patterns: List with the patterns.
    :param flags: Flags options for the compile function.
    :return: List with the compiled patterns.
    """
    if patterns is None:
        return []

    result_list = []

    for pattern in patterns:
        result_list.append(compile(pattern=pattern, flags=flags))

    return result_list
