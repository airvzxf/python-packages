#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Test case for get a compiled list of RegEx patterns.
"""

from re import DOTALL, IGNORECASE, compile
from unittest import TestCase

from pkg.regex.get.compiled_list import compiled_list


class TestPkgRegExGetCompiledList(TestCase):
    """
    Test compile a list of RegEx.
    """

    def test_default_values(self):
        """
        Test the default values for the method.
        """
        result_list = compiled_list()
        expected_list = []
        self.assertEqual(expected_list, result_list)

    def test_sending_patterns_but_not_flags(self):
        """
        Returns a basic list and doesn't send any flags.
        """
        result_list = compiled_list(patterns=[".*", "[A-Z]"])

        expected_list = [compile(".*"),
                         compile("[A-Z]")]

        self.assertEqual(expected_list, result_list)

    def test_sending_patterns_with_flags(self):
        """
        Returns a basic list and the RegEx flags were sent.
        """
        result_list = compiled_list(patterns=[".*", "[A-Z]"],
                                    flags=DOTALL | IGNORECASE)

        expected_list = [compile(".*", DOTALL | IGNORECASE),
                         compile("[A-Z]", DOTALL | IGNORECASE)]

        self.assertEqual(expected_list, result_list)

    def test_sending_one_pattern_return_object_vs_list(self):
        """
        Returns the one compiled RegEx object.
        """
        result_list = compiled_list(patterns=[".*"])

        expected_list = compile(".*")

        self.assertEqual(expected_list, result_list)

    def test_sending_one_pattern_return_list_with_one_compiled_regex(self):
        """
        Returns a list with one compiled RegEx.
        """
        result_list = compiled_list(patterns=[".*"], is_only_one=False)

        expected_list = [compile(".*")]

        self.assertEqual(expected_list, result_list)
