#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Test case for get raw content from HTML tag."""

import unittest

from src.pkg.html.tag.get.raw_content_from import raw_content_from


class TestPkgHtmlTagGetRawContentFrom(unittest.TestCase):
    """Tests for extract test tags"""

    def test_when_the_tag_param_is_nil(self):
        """Returns nothing"""
        self.assertIsNone(raw_content_from())

    def test_when_sent_html_code(self):
        """Returns the code inside of the tag <div...>...</div>"""
        actual_text = raw_content_from('div', '<div name="test">This is a test</div>')
        expected_text = 'This is a test'

        self.assertEqual(actual_text, expected_text)

    def test_when_sent_html_code_ignore_case(self):
        """Returns the code inside of the tag <dIV...>...</dIV>"""
        actual_text = raw_content_from('div', '<dIV name="test">This is a test</dIV>')
        expected_text = 'This is a test'

        self.assertEqual(actual_text, expected_text)

    def test_when_sent_html_code_without_ignore_case(self):
        """Returns None"""
        actual_text = raw_content_from('div', '<dIV name="test">This is a test</dIV>', False)

        self.assertIsNone(actual_text)

    def test_when_the_html_code_not_contain_the_tag(self):
        """Returns None"""
        actual_text = raw_content_from('div', '<span name="test">This is a test</span>')

        self.assertIsNone(actual_text)

    def test_when_exists_other_tags_with_the_same_name_inside_the_text(self):
        """Returns the content for the first and the last tag"""
        text = '<article><div name="my"><span>My test</span><div name="f"><span>footer<span></div></div></article>'
        expected_text = '<span>My test</span><div name="f"><span>footer<span></div>'

        actual_text = raw_content_from('div', text)

        self.assertEqual(actual_text, expected_text)

    def test_when_the_text_has_break_lines(self):
        """Returns the content for the first and the last tag"""
        text = """
                <article>
                    <div name="my">
                        <span>My test</span>
                        <div name="f">
                            <span>footer<span>
                        </div>
                    </div>
                </article>"""

        expected_text = """
                        <span>My test</span>
                        <div name="f">
                            <span>footer<span>
                        </div>
                    """

        actual_text = raw_content_from('div', text)

        self.assertEqual(actual_text, expected_text)


if __name__ == '__main__':
    unittest.main()
