#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Get the RegEx compilation flags filtered by params.
"""

from re import DOTALL, IGNORECASE


def get_compilation_flags(dot_all=True, ignore_case=False):
    """
    Return the compilation flags for RegEx.

    :param dot_all: Make . match any character, including newlines.
    :param ignore_case: Do case-insensitive matches
    :return: The list with the RegEx compilation flags.
    """
    flags = 0

    if dot_all:
        flags |= DOTALL

    if ignore_case:
        flags |= IGNORECASE

    return flags
