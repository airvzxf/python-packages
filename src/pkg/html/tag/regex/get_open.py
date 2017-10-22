#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Returns the string pattern for search opened HTML tag."""


def get_open(tag=''):
    """Return RegEx pattern which find all opened HTML tag.

    If tag is empty return a different RegEx pattern.

    :param tag: HTML tag like div, article, body, etc., looks like <div, <body.
    :return: String with the RegEx pattern.
    """
    if tag is None:
        return

    if tag is '':
        return r"<[^/]+?(?:\".*?\"|'.*?'|.*?)*?>"
    else:
        return r"<{0}(?:\".*?\"|'.*?'|.*?)*?>".format(tag)
