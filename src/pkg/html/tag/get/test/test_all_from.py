#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Test case for search all tags from HTML code.
"""

from unittest import TestCase

from pkg.html.tag.get.all_from import all_from


class TestPkgHtmlTagAllFrom(TestCase):
    """
    Tests for extract test tags.
    """

    def test_when_tag_is_none_return_empty(self):
        """
        Returns an emtpy list if we don't send the tag.
        """
        actual_text = all_from()

        self.assertEqual([], actual_text)

    def test_when_sent_html_code_ignore_case(self):
        """
        Returns the code inside of the tag <dIV...>...</dIV>.
        """
        actual_text = all_from(tag='div', text='<dIV name="test">This is a test</dIV>')[0]
        expected_text = '<dIV name="test">This is a test</dIV>'

        self.assertEqual(actual_text, expected_text)

    def test_when_sent_html_code_without_ignore_case(self):
        """
        Returns None.
        """
        actual_text = all_from(tag='div', text='<dIV name="test">This is a test</dIV>', ignore_case=False)

        self.assertEqual(0, len(actual_text))

    def test_when_text_has_break_lines_and_should_be_return_two_results(self):
        """
        Returns two results.
        """
        text, expected_text_1, expected_text_2 = get_two_matches()

        result = all_from(tag='div', text=text, ignore_case=True)

        self.assertEqual(2, len(result))
        self.assertEqual(result[0], expected_text_1)
        self.assertEqual(result[1], expected_text_2)

    def test_when_text_has_break_lines_and_should_be_return_two_results_and_the_content_inside_of_the_tag(self):
        """
        Returns two results.
        """
        text, expected_text_1, expected_text_2 = get_two_matches_and_the_content_inside_of_the_tag()

        result = all_from(tag='div', text=text, ignore_case=True, get_only_content_inside=True)

        self.assertEqual(2, len(result))
        self.assertEqual(result[0], expected_text_1)
        self.assertEqual(result[1], expected_text_2)

    def test_when_text_has_break_lines_and_should_be_return_three_results(self):
        """
        Return the three articles.
        """
        text, expected_text_1, expected_text_2, expected_text_3 = get_three_matches()

        result = all_from(tag='article', text=text, ignore_case=True)

        self.assertEqual(3, len(result))
        self.assertEqual(result[0], expected_text_1)
        self.assertEqual(result[1], expected_text_2)
        self.assertEqual(result[2], expected_text_3)

    def test_when_text_has_break_lines_and_should_be_return_three_results_and_the_content_inside_of_the_tag(self):
        """
        Return the three articles.
        """
        text, expected_text_1, expected_text_2, expected_text_3 = get_three_matches_and_the_content_inside_of_the_tag()

        result = all_from(tag='article', text=text, ignore_case=True, get_only_content_inside=True)

        self.assertEqual(3, len(result))
        self.assertEqual(result[0], expected_text_1)
        self.assertEqual(result[1], expected_text_2)
        self.assertEqual(result[2], expected_text_3)


def get_two_matches():
    """
    Returns the text and the two expected strings.
    """
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


def get_two_matches_and_the_content_inside_of_the_tag():
    """
    Returns the text and the two expected strings but this strings are the content inside of the matcher tag.
    """
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
                    <div class="line-red">Line #1</div>"""

    expected_text_2 = """
                <span>My footer<span>
                <div class="line-green">Line #2</div>"""

    return text, expected_text_1, expected_text_2


def get_three_matches():
    """
    Returns the text and the three expected strings.
    """
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


def get_three_matches_and_the_content_inside_of_the_tag():
    """
    Returns the text and the three expected strings.
    """
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
            <span>Article #1</span>"""

    expected_text_2 = """
            <span>Article #2</span>
            <div class="line-red">Line red</div>"""

    expected_text_3 = """
            <span>Article #3</span>"""

    return text, expected_text_1, expected_text_2, expected_text_3
