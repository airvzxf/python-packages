#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest

from src.pkg.regEx.html.extract_tags import get_all_tags_from


class TestGetFromTag(unittest.TestCase):
    """Tests for extract html tags"""

    def test_when_text_has_break_lines_and_should_be_return_two_results(self):
        """Returns two results"""
        text, expected_text_1, expected_text_2 = get_two_expected_matches()

        result = get_all_tags_from('div', text, True)

        self.assertEqual(2, len(result))
        self.assertEqual(result[0], expected_text_1)
        self.assertEqual(result[1], expected_text_2)

    # def test_when_text_has_break_lines_and_should_be_return_two_results_and_only_the_content_inside_of_the_tag(self):
    #     """Returns two results"""
    #     text, expected_text_1, expected_text_2 = get_two_expected_matches_and_only_the_content_inside_of_the_tag()
    #
    #     result = get_all_tags_from('div', text, True, True, True)
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

        result = get_all_tags_from('article', text, True)

        self.assertEqual(3, len(result))
        self.assertEqual(result[0], expected_text_1)
        self.assertEqual(result[1], expected_text_2)
        self.assertEqual(result[2], expected_text_3)

        # def test_when_text_has_break_lines_and_should_be_return_three_results_and_only_the_content_inside_of_the_tag(self):
        #     """Return the three articles"""
        #     text, expected_text_1, expected_text_2, expected_text_3 = get_three_expected_matches_and_only_the_content_inside_of_the_tag()
        #
        #     result = get_all_tags_from('article', text, True, True, True)
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
