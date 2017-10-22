#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Module: Get web page from http protocol."""

from urllib3 import PoolManager


def get(url=None):
    """Request the method GET to the http protocol."""
    if url is None:
        return None

    http = PoolManager()
    response = http.urlopen(method='GET', url=url)

    return {
        'status': response.status,
        'headers': response.headers,
        'data': response.data,
        'reason': response.reason,
        'decode_content': response.decode_content
    }
