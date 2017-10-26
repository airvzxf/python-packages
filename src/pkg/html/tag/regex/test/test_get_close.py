#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Test case for get all the closed HTML tags.
"""

from unittest import TestCase

from pkg.html.tag.regex.get_close import get_close


class TestPkgHtmlTagRegexGetClose(TestCase):
    """
    Test the regex patterns for tags.
    """

    def test_if_sent_none_tag_it_returns_the_regex_without_tag(self):
        """
        Return a regEx string without tag.
        """
        expected_string = get_close()

        self.assertEqual(r"</[^<]*?>", expected_string)

    def test_if_sent_empty_tag_it_returns_the_regex_without_tag(self):
        """
        Return a regEx string without tag.
        """
        expected_string = get_close(tag='')

        self.assertEqual(r"</[^<]*?>", expected_string)

    def test_return_the_regex_string(self):
        """
        Return the correct regex pattern with the tag.
        """
        expected_string = get_close("article")

        self.assertEqual(r"</article[^<]*?>", expected_string)
