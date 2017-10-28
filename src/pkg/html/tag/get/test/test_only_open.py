#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Test case for get only opened HTML tags which start with a specific tag.
"""

from unittest import TestCase

from pkg.html.tag.get.only_open import only_open


class TestPkgHtmlTagGetOnlyOpen(TestCase):
    """
    Tests for extract only opened tags.
    """

    def test_when_tag_is_none_return_empty(self):
        """
        Returns an emtpy list if we don't send the tag.
        """
        expected_property = only_open()

        self.assertEqual([], expected_property)

    def test_extract_specific_tag(self):
        """
        Extract tags and check the properties.
        """
        tags = only_open(tag='article', text='''<div id="a">a.1</div> <article class='b'>b.1</article>''')

        expected_tad = ["<article class='b'>"]

        self.assertEqual(expected_tad, tags)

    def test_extract_specific_tag_and_ignore_case(self):
        """
        Extract tags and check the properties.
        """
        tags = only_open(tag='aRtIcLe',
                         text='''<div id="a">a.1</div> <article class='b'>b.1</article>''',
                         ignore_case=True)

        expected_tad = ["<article class='b'>"]

        self.assertEqual(expected_tad, tags)

    def test_extract_specific_tag_and_not_ignore_case(self):
        """
        Extract tags and check the properties.
        """
        tags = only_open(tag='aRtIcLe',
                         text='''<div id="a">a.1</div> <article class='b'>b.1</article>''',
                         ignore_case=False)

        self.assertEqual([], tags)

    def test_extract_all_tags(self):
        """
        Extract tags and check the properties.
        """
        tags = only_open(text='''<div id="a">a.1</div> <article class='b'>b.1</article><span>-</span>''')

        expected_tags = ['<div id="a">', "<article class='b'>", '<span>']

        self.assertEqual(expected_tags, tags)
