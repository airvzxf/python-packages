#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest

from src.pkg.html.tag.regex.get_raw_open_close import get_raw_open_close


class TestPkgHtmlTagRegexGetRawOpenClose(unittest.TestCase):
    """Test the regex patterns for tags"""

    def test_if_sent_no_parameters_return_empty(self):
        """Return nil if we don't send parameters"""
        expected_string = get_raw_open_close()

        self.assertIsNone(expected_string)

    def test_return_the_regex_string(self):
        """Return the correct regex pattern with the tag"""
        expected_string = get_raw_open_close("article")

        self.assertEqual(r"<article[^<]*?>(.*)</article>", expected_string)


if __name__ == '__main__':
    unittest.main()
