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
    flags = None

    if dot_all:
        flags = _add_flags(flags, DOTALL)

    if ignore_case:
        flags = _add_flags(flags, IGNORECASE)

    return flags


def _add_flags(flags=None, flag=None):
    """
    Private method which validate if the flags is None then it assign a new flag otherwise it append.

    :param flags: The list of RegEx flags.
    :param flag: The new RegEx flag which want to add.
    :return: The list of RegEx flags with the new flag.
    """
    if flags is None:
        flags = flag
    else:
        flags |= flag

    return flags
