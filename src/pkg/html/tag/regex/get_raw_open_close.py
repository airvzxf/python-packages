#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Returns the string pattern for search from opened HTML tag until the closed tag."""


def get_raw_open_close(tag=None):
    """Return RegEx pattern which find all the text inside of the opened HTML tag until the closed tag.

    :param tag: HTML tag like div, article, body, etc., looks like <div, <body.
    :return: String with the RegEx pattern.
    """
    if tag is None:
        return

    return r"<{0}[^<]*?>(.*)</{0}>".format(tag)
