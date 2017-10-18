#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Test case for return the RegEx pattern to find all properties inside of the HTML tag."""

import unittest

from src.pkg.html.tag.regex.get_properties import get_properties


class TestPkgHtmlTagRegexGetProperties(unittest.TestCase):
    """Test the regex patterns for properties"""

    def test_return_the_regex_string(self):
        """Return the correct regex pattern"""
        expected_string = get_properties()

        self.assertEqual(r"(\S+)\s*=\s*([']|[\"])\s*([\W\w]*?)\s*\2", expected_string)

    def test_return_the_regex_string_without_trim(self):
        """Return the correct regex pattern"""
        expected_string = get_properties(trim=False)

        self.assertEqual(r"(\S+)\s*=\s*([']|[\"])([\W\w]*?)\2", expected_string)
