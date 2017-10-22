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

    def test_if_sent_no_parameters_return_empty(self):
        """
        Return nil if we don't send parameters.
        """
        expected_string = get_close()

        self.assertIsNone(expected_string)

    def test_return_the_regex_string(self):
        """
        Return the correct regex pattern with the tag.
        """
        expected_string = get_close("article")

        self.assertEqual(r"</article[^<]*?>", expected_string)
