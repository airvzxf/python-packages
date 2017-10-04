#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest

from src.pkg.regEx.html.extract_tags import get_from_tag


class TestGetFromTag(unittest.TestCase):
    """Tests for extract html tags"""

    # Test get_from_tag
    def test_when_the_tag_param_is_nil(self):
        """Returns nothing"""
        self.assertIsNone(get_from_tag(None))

    def test_when_sent_html_code(self):
        """Returns the code inside of the tag <div...>...</div>"""
        actual_text = get_from_tag('div', '<div name="test">This is a test</div>')
        expected_text = 'This is a test'
        self.assertEqual(actual_text, expected_text)

    def test_when_sent_html_code_ignore_case(self):
        """Returns the code inside of the tag <dIV...>...</dIV>"""
        actual_text = get_from_tag('div', '<dIV name="test">This is a test</dIV>')
        expected_text = 'This is a test'
        self.assertEqual(actual_text, expected_text)

    def test_when_sent_html_code_without_ignore_case(self):
        """Returns None"""
        actual_text = get_from_tag('div', '<dIV name="test">This is a test</dIV>', False)
        self.assertIsNone(actual_text)

    def test_when_the_html_code_not_contain_the_tag(self):
        """Returns None"""
        actual_text = get_from_tag('div', '<span name="test">This is a test</span>')
        self.assertIsNone(actual_text)

    def test_when_exists_other_tags_with_the_same_name_inside_the_text(self):
        """Returns the content for the first and the last tag"""
        text = '<article><div name="my"><span>My test</span><div name="f"><span>footer<span></div></div></article>'
        expected_text = '<span>My test</span><div name="f"><span>footer<span></div>'
        actual_text = get_from_tag('div', text)

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

        actual_text = get_from_tag('div', text)

        self.assertEqual(actual_text, expected_text)

    def test_when_text_has_break_lines_and_should_be_return_two_results(self):
        """Returns two results"""
        text, expected_text_1, expected_text_2 = get_two_expected_matches()

        result = get_from_tag('div', text, True, True)

        self.assertEqual(2, len(result))
        self.assertEqual(result[0], expected_text_1)
        self.assertEqual(result[1], expected_text_2)

    # def test_when_text_has_break_lines_and_should_be_return_two_results_and_only_the_content_inside_of_the_tag(self):
    #     """Returns two results"""
    #     text, expected_text_1, expected_text_2 = get_two_expected_matches_and_only_the_content_inside_of_the_tag()
    #
    #     result = get_from_tag('div', text, True, True, True)
    #
    #     print("len(result): ", len(result))
    #     print("#1:")
    #     print("--------------------------------------------------------------------------------------------------")
    #     print(result[0])
    #     print("--------------------------------------------------------------------------------------------------")
    #     print(expected_text_1)
    #     print("--------------------------------------------------------------------------------------------------")
    #     print("#2:")
    #     print("-------------------------------------------------")
    #     print(result[1])
    #     print("-------------------------------------------------")
    #     print(expected_text_2)
    #     print("-------------------------------------------------")
    #
    #     self.assertEqual(2, len(result))
    #     self.assertEqual(result[0], expected_text_1)
    #     self.assertEqual(result[1], expected_text_2)

    def test_when_text_has_break_lines_and_should_be_return_three_results(self):
        """Return the three articles"""
        text, expected_text_1, expected_text_2, expected_text_3 = get_three_expected_matches()

        result = get_from_tag('article', text, True, True)

        self.assertEqual(3, len(result))
        self.assertEqual(result[0], expected_text_1)
        self.assertEqual(result[1], expected_text_2)
        self.assertEqual(result[2], expected_text_3)

        # def test_when_text_has_break_lines_and_should_be_return_three_results_and_only_the_content_inside_of_the_tag(self):
        #     """Return the three articles"""
        #     text, expected_text_1, expected_text_2, expected_text_3 = get_three_expected_matches_and_only_the_content_inside_of_the_tag()
        #
        #     result = get_from_tag('article', text, True, True, True)
        #
        #     self.assertEqual(3, len(result))
        #     self.assertEqual(result[0], expected_text_1)
        #     self.assertEqual(result[1], expected_text_2)
        #     self.assertEqual(result[2], expected_text_3)


def get_two_expected_matches():
    """Returns the text and the two expected strings"""
    text = """
            <article>
                <div name="div1">
                    <span name="test">This is a test</span>
                    <div class="line-red">Line #1</div>
                </div>
            </article>
            <div name="footer">
                <span>My footer<span>
                <div class="line-green">Line #2</div>
            </div>"""

    expected_text_1 = """<div name="div1">
                    <span name="test">This is a test</span>
                    <div class="line-red">Line #1</div>
                </div>"""

    expected_text_2 = """<div name="footer">
                <span>My footer<span>
                <div class="line-green">Line #2</div>
            </div>"""

    return text, expected_text_1, expected_text_2


def get_two_expected_matches_and_only_the_content_inside_of_the_tag():
    """Returns the text and the two expected strings but this strings are the content inside of the matcher tag"""
    text = """
            <article>
                <div name="div1">
                    <span name="test">This is a test</span>
                    <div class="line-red">Line #1</div>
                </div>
            </article>
            <div name="footer">
                <span>My footer<span>
                <div class="line-green">Line #2</div>
            </div>"""

    expected_text_1 = """
                    <span name="test">This is a test</span>
                    <div class="line-red">Line #1</div>
                """

    expected_text_2 = """
                    <span>My footer<span>
                    <div class="line-green">Line #2</div>
                """

    return text, expected_text_1, expected_text_2


def get_three_expected_matches():
    """Returns the text and the three expected strings"""
    text = """
        <article>
            <span>Article #1</span>
        </article>
        <div>Other:</div>
        <br>
        <article>
            <span>Article #2</span>
            <div class="line-red">Line red</div>
        </article>
        <div>Other:</div>
        <br>
        <article>
            <span>Article #3</span>
        </article>
    """

    expected_text_1 = """<article>
            <span>Article #1</span>
        </article>"""

    expected_text_2 = """<article>
            <span>Article #2</span>
            <div class="line-red">Line red</div>
        </article>"""

    expected_text_3 = """<article>
            <span>Article #3</span>
        </article>"""

    return text, expected_text_1, expected_text_2, expected_text_3


def get_three_expected_matches_and_only_the_content_inside_of_the_tag():
    """Returns the text and the three expected strings"""
    text = """
        <article>
            <span>Article #1</span>
        </article>
        <div>Other:</div>
        <br>
        <article>
            <span>Article #2</span>
            <div class="line-red">Line red</div>
        </article>
        <div>Other:</div>
        <br>
        <article>
            <span>Article #3</span>
        </article>
    """

    expected_text_1 = """
            <span>Article #1</span>
        """

    expected_text_2 = """
            <span>Article #2</span>
            <div class="line-red">Line red</div>
        """

    expected_text_3 = """
            <span>Article #3</span>
        """

    return text, expected_text_1, expected_text_2, expected_text_3


if __name__ == '__main__':
    unittest.main()
