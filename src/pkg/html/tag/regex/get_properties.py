#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Returns the string pattern for search properties inside of the HTML tag.
"""


def get_properties(trim=True):
    """
    Return RegEx pattern which find all the properties inside of the HTML tag.

    :param trim: If is true, it delete all the white spaces before and after the text.
    :return: String with the RegEx pattern.
    """
    if trim:
        return r"(\S+)\s*=\s*([']|[\"])\s*([\W\w]*?)\s*\2"
    else:
        return r"(\S+)\s*=\s*([']|[\"])([\W\w]*?)\2"
