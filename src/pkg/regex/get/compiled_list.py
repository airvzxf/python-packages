#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Get a list of RegEx patterns and return a compiled list.
"""

from re import compile


def compiled_list(patterns=None, flags=0, is_only_one=True):
    """
    Return a list with the compiled patterns.

    :param patterns: List with the patterns.
    :param flags: Flags options for the compile function.
    :param is_only_one: If the result is only one object it returns the object versus the list with one element.
    :return: List with the compiled patterns.
    """
    result_list = []

    if patterns is None:
        return result_list

    for pattern in patterns:
        result_list.append(compile(pattern=pattern, flags=flags))

    if is_only_one and len(result_list) == 1:
        return result_list[0]

    return result_list
