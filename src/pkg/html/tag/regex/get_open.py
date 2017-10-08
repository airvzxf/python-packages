#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def get_open(tag=''):
    if tag is None:
        return

    if tag is '':
        return r"<[^/]+?(?:\".*?\"|'.*?'|.*?)*?>"
    else:
        return r"<{0}(?:\".*?\"|'.*?'|.*?)*?>".format(tag)
