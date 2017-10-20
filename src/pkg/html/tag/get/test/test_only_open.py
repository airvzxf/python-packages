#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Test case for get only opened HTML tags which start with a specific tag."""

import unittest

from pkg.html.tag.get.only_open import only_open


class TestPkgHtmlTagGetOnlyOpen(unittest.TestCase):
    """Tests for extract only opened tags"""

    def test_when_tag_is_none_return_none(self):
        """Returns nil if we don't send the tag"""
        expected_property = only_open(None)

        self.assertIsNone(expected_property)

    def test_extract_specific_tag(self):
        """Extract tags and check the properties"""
        tags = only_open('article', '''<div id="a">a.1</div> <article class='b'>b.1</article>''')

        self.assertEqual(1, len(tags))
        self.assertEqual(tags[0], "<article class='b'>")

    def test_extract_all_tags(self):
        """Extract tags and check the properties"""
        tags = only_open(text='''<div id="a">a.1</div> <article class='b'>b.1</article><span>-</span>''')

        self.assertEqual(3, len(tags))
        self.assertEqual(tags[0], '<div id="a">')
        self.assertEqual(tags[1], "<article class='b'>")
        self.assertEqual(tags[2], "<span>")
