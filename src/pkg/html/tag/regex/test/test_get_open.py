#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Test case for get all the opened HTML tags."""

import unittest

from pkg.html.tag.regex.get_open import get_open


class TestPkgHtmlTagRegexGetOpen(unittest.TestCase):
    """Test the regex patterns for tags"""

    def test_if_sent_none_it_returns_the_same(self):
        """Return nil if we don't send parameters"""
        expected_string = get_open(None)

        self.assertIsNone(expected_string)

    def test_if_sent_no_parameters_return_empty(self):
        """Return nil if we don't send parameters"""
        expected_string = get_open()

        self.assertEqual(r"<[^/]+?(?:\".*?\"|'.*?'|.*?)*?>", expected_string)

    def test_return_the_regex_string(self):
        """Return the correct regex pattern with the tag"""
        expected_string = get_open("article")

        self.assertEqual(r"<article(?:\".*?\"|'.*?'|.*?)*?>", expected_string)
