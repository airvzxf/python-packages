#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Returns the string pattern for closed HTML tags.
"""


def get_close(tag=None):
    """
    Returns the RegEx pattern which find all the closed HTML tags.

    :param tag: HTML tag like div, article, body, etc., looks like <div, <body.
    :return: String with the RegEx pattern.
    """
    if tag is None:
        return

    return r"</{0}[^<]*?>".format(tag)
