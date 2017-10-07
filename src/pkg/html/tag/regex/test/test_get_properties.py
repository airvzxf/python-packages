#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest

from src.pkg.html.tag.regex.get_properties import get_properties


class TestPkgHtmlTagRegexGetProperties(unittest.TestCase):
    """Test the regex patterns for properties"""

    def test_return_the_regex_string(self):
        """Return the correct regex pattern"""
        expected_string = get_properties()

        self.assertEqual(r"(\S+)\s*=\s*[\"']?((?:.(?![\"']?\s+(?:\S+)=|[>\"']))?[^\"']*)[\"']?", expected_string)


if __name__ == '__main__':
    unittest.main()
