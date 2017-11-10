#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Module: Download one file via HTTP.
"""

# noinspection PyCompatibility
from urllib.request import HTTPError, urlretrieve


def file_from(url=None, filename=None):
    if url is None:
        return None

    try:
        urlretrieve(url=url, filename=filename)
    except HTTPError:
        return False
    except FileNotFoundError:
        return False

    return True
