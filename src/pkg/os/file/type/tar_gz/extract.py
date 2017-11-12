#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Module: Extract content from the files Gzip or Tar Gz in the Operative System.
"""

from tarfile import TarError, open as open_tarfile


def extract(path: str = None, extract_path: str = None) -> bool:
    """
    Extract Tar Gz file in the operative system.

    :param path: The directory path where the tar gz file exists.
    :param extract_path: The directory path where the tar gz would be extracted.
    :return: True if it was extracted or false if it isn't.

    :rtype: bool
    """
    if not path or not extract_path:
        return False

    try:
        with open_tarfile(path, 'r:gz') as tar_gz_file:
            tar_gz_file.extractall(extract_path)
            return True
    except (OSError, TarError):
        return False
