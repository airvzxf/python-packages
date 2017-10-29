#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Test case for get a compiled list of RegEx patterns.
"""

from unittest import TestCase

from pkg.regex.get.compiled_list import compiled_list


class TestPkgHtmlTagAllFrom(TestCase):
    """
    Test compile a list of RegEx.
    """

    def test_default_values(self):
        """
        Test the default values for the method.
        """
        compiled_list()
