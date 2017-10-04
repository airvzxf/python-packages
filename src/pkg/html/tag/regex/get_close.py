#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def get_close(tag=None):
    if tag is None:
        return

    return r"</{0}[^<]*?>".format(tag)
