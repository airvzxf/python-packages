#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Get a list of RegEx patterns and return a compiled list.
"""


def compiled_list(patterns=None, flags=None):
    """
    Return a list with the compiled patterns.

    :param patterns: List with the patterns.
    :param flags: Flags options for the compile function.
    :return: List with the compiled patterns.
    """
    if patterns is None:
        patterns = []
