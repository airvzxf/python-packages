#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Module: Download one file via HTTP.
"""

# noinspection PyCompatibility
from urllib.request import HTTPError, urlretrieve


def file_from(url=None, filename=None):
    """
    Download file from url via http.

    :param url: URL normally started with http(s).
    :param filename: Optional if you want move the temporal file to an specific directory with a specific name.
    :return: True if it was downloaded or false if it wasn't downloaded or some known error occurred. None if
    something was wrong.
    """
    if url is None:
        return None

    try:
        urlretrieve(url=url, filename=filename)
    except HTTPError:
        return False
    except FileNotFoundError:
        return False

    return True
