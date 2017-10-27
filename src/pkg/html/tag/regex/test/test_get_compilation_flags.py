#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Test the module about get the RegEx compilation flags filtered by params.
"""

from re import DOTALL, IGNORECASE
from unittest import TestCase

from pkg.html.tag.regex.get_compilation_flags import get_compilation_flags


class TestPkgHtmlTagRegexGetCompilationFlags(TestCase):
    """
    Test the regex returned the compilation flags.
    """

    def test_the_default_flags(self):
        """
        Return dot all flag.
        """
        expected_flag = get_compilation_flags()

        self.assertEqual(DOTALL, expected_flag)

    def test_if_any_flag_is_true_return_none(self):
        """
        Return dot all flag.
        """
        expected_flag = get_compilation_flags(dot_all=False)

        self.assertIsNone(expected_flag)

    def test_flag_dot_all_and_ignore_case(self):
        """
        Return dot all and ignore case flag.
        """
        expected_flag = get_compilation_flags(ignore_case=True)

        self.assertEqual(IGNORECASE | DOTALL, expected_flag)
