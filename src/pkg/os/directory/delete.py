#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Module: Delete directories in the Operative System.
"""

from os.path import exists, isdir

from shutil import rmtree


def delete(path=None):
    """
    Delete a specific directory.

    :param path: Path in the operative system which needs to delete.
    :return: True if it was deleted or false if it isn't. None if something was wrong.
    """
    if path is None:
        return None

    if exists(path) and isdir(path):
        rmtree(path)
        return True

    return False
