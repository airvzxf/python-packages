#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Test the helper module which return a regex flag based on parameters.
"""

from re import DOTALL, IGNORECASE
from unittest import TestCase

from pkg.html.tag.get.helper_regex_flags import helper_regex_flags


class TestPkgHtmlTagGetHelperRegExFlags(TestCase):
    """
    Test class for match the returned flags based on parameters.
    """

    def test_return_dot_all_flag(self):
        """
        Match the returned flag with the Dot All flag.
        """
        flags = helper_regex_flags()

        self.assertEqual(DOTALL, flags)

    def test_return_dot_all_flag_and_ignore_case(self):
        """
        Match the returned flag with the Dot All and Ignore Case flag.
        """
        flags = helper_regex_flags(ignore_case=True)

        self.assertEqual(DOTALL | IGNORECASE, flags)
