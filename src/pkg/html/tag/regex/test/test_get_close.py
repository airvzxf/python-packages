#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest

from src.pkg.html.tag.regex.get_close import get_close


class TestPkgHtmlTagRegexGetClose(unittest.TestCase):
    """Test the regex patterns for tags"""

    def test_if_sent_no_parameters_return_empty(self):
        """Return nil if we don't send parameters"""
        expected_string = get_close()

        self.assertIsNone(expected_string)

    def test_return_the_regex_string(self):
        """Return the correct regex pattern with the tag"""
        expected_string = get_close("article")

        self.assertEqual(r"</article[^<]*?>", expected_string)


if __name__ == '__main__':
    unittest.main()
