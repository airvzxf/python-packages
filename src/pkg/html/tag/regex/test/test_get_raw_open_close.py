#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Test case for get the raw content inside of a specific HTML tag."""

from unittest import TestCase

from pkg.html.tag.regex.get_raw_open_close import get_raw_open_close


class TestPkgHtmlTagRegexGetRawOpenClose(TestCase):
    """Test the regex patterns for tags"""

    def test_if_sent_no_parameters_return_empty(self):
        """Return nil if we don't send parameters"""
        expected_string = get_raw_open_close()

        self.assertIsNone(expected_string)

    def test_return_the_regex_string(self):
        """Return the correct regex pattern with the tag"""
        expected_string = get_raw_open_close("article")

        self.assertEqual(r"<article[^<]*?>(.*)</article>", expected_string)
