#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def get_properties(trim=True):
    if trim:
        return r"(\S+)\s*=\s*([']|[\"])\s*([\W\w]*?)\s*\2"
    else:
        return r"(\S+)\s*=\s*([']|[\"])([\W\w]*?)\2"
