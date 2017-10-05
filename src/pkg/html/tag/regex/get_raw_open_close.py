#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def get_raw_open_close(tag=None):
    if tag is None:
        return

    return r"<{0}[^<]*?>(.*)</{0}>".format(tag)
