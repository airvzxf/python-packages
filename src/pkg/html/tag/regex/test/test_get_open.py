#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Test case for get all the opened HTML tags.
"""

from unittest import TestCase

from pkg.html.tag.regex.get_open import get_open


class TestPkgHtmlTagRegexGetOpen(TestCase):
    """
    Test the regex patterns for tags.
    """

    def test_if_sent_none_tag_it_returns_the_regex_without_tag(self):
        """
        Return a regEx string without tag.
        """
        expected_string = get_open()

        self.assertEqual(r"<[^/]+?(?:\".*?\"|'.*?'|.*?)*?>", expected_string)

    def test_if_sent_empty_tag_it_returns_the_regex_without_tag(self):
        """
        Return a regEx string without tag.
        """
        expected_string = get_open(tag='')

        self.assertEqual(r"<[^/]+?(?:\".*?\"|'.*?'|.*?)*?>", expected_string)

    def test_return_the_regex_string(self):
        """
        Return the correct regex pattern with the tag.
        """
        expected_string = get_open("article")

        self.assertEqual(r"<article(?:\".*?\"|'.*?'|.*?)*?>", expected_string)
