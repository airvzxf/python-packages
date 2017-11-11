#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Module: Delete files in the Operative System.
"""

from os import remove
from os.path import exists, isfile


def delete(path: str = None) -> bool:
    """
    Delete a specific file.

    :param path: Path in the operative system which needs to delete.
    :return: True if it was deleted or false if it isn't. None if something was wrong.

    :rtype: bool
    """
    if path is None:
        return False

    if exists(path) and isfile(path):
        remove(path)
        return True

    return False
