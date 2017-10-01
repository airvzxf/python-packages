#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest

from src.pkg.regEx.html.extract_tags import get_from_tag


class TestGetFromTag(unittest.TestCase):
    """Tests for `extract_tags.py`."""

    # Test get_from_tag
    def test_when_tag_param_is_nil(self):
        """Returns nothing"""
        self.assertIsNone(get_from_tag(None))

    def test_when_sent_html_code(self):
        """Returns the code inside of the tag <div...>...</div>"""
        actual_text = get_from_tag('div', '<div name="test">This is a test</div>')
        expected_text = 'This is a test'
        self.assertEqual(actual_text, expected_text)

    def test_when_html_code_not_contain_the_tag(self):
        """Returns None"""
        actual_text = get_from_tag('div', '<span name="test">This is a test</span>')
        self.assertIsNone(actual_text)

    def test_when_exists_other_tags_with_the_same_name(self):
        """Returns the content for the first and the last tag"""
        text = '<article><div name="my"><span>My test</span><div name="f"><span>footer<span></div></div></article>'
        expected_text = '<span>My test</span><div name="f"><span>footer<span></div>'
        actual_text = get_from_tag('div', text)

        self.assertEqual(actual_text, expected_text)

    # def test_when_text_has_breaklines(self):
    #     """Returns the content for the first and the last tag"""
    #     text = """
    #         <article>
    #             <div name="my">
    #                 <span>My test</span>
    #                 <div name="f">
    #                     <span>footer<span>
    #                 </div>
    #             </div>
    #         </article>
    #     """
    #     expected_text = """<span>My test</span>
    #                 <div name="f">
    #                     <span>footer<span>
    #                 </div>"""
    #     actual_text = get_from_tag('div', text)
    #
    #     self.assertEqual(actual_text, expected_text)

    # def test_when_text_has_breaklines(self):
    #     """Returns the content for the first and the last tag"""
    #     text = """
    #         <article>
    #             <div name="div1">
    #                 <span name="test">This is a test</span>
    #             </div>
    #         </article>
    #         <div name="footer">
    #             <span>My footer<span>
    #         </div>
    #     """
    #     expected_text = """
    #                 <span name="test">This is a test</span>
    #             </div>
    #         </article>
    #         <div name="footer">
    #             <span>My footer<span>
    #     """
    #     actual_text = get_from_tag('div', text)
    #
    #     self.assertEqual(actual_text, expected_text)


if __name__ == '__main__':
    unittest.main()
