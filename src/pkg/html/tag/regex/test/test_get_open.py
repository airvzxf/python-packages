#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest

from src.pkg.html.tag.regex.get_open import get_open


class TestPkgHtmlTagRegexOpen(unittest.TestCase):
    """Test the regex patterns for tags"""

    def test_return_the_reg_string(self):
        """Return the correct regex pattern with the tag"""
        expected_string = get_open("article")

        self.assertEqual(r"<article[^<]*?>", expected_string)


if __name__ == '__main__':
    unittest.main()