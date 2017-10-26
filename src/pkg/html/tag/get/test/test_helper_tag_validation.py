#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Test the helper module which validate the tag.
"""

from re import DOTALL, IGNORECASE
from unittest import TestCase

from pkg.html.tag.get.helper_tag_validation import helper_tag_validation


class TestPkgHtmlTagGetHelperTagValidation(TestCase):
    """
    Test class for validate the tags.
    """

    def test_return_dot_all_flag(self):
        """
        Match the returned flag with the Dot All flag.
        """
        flags = helper_tag_validation(tag='')

        self.assertEqual(DOTALL, flags)

    def test_return_dot_all_flag_and_ignore_case(self):
        """
        Match the returned flag with the Dot All and Ignore Case flag.
        """
        flags = helper_tag_validation(tag='', ignore_case=True)

        self.assertEqual(DOTALL | IGNORECASE, flags)
