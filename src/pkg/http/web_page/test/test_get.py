#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Test case for get the web page from the http protocol.
"""

from unittest import TestCase

from urllib3_mock import Responses

from pkg.http.web_page.get import get

responses = Responses('requests.packages.urllib3')


class TestPkgHttpWebPageGet(TestCase):
    """
    Test the get request from web page with the http protocol.
    """

    def test_if_url_is_none_return_none(self):
        """
        Return None if the parameter url is none.
        """
        result = get()

        self.assertIsNone(result)

    @responses.activate
    def test_the_response_calls(self):
        """
        The number of calls should be calls one time.
        """
        call_a_basic_response()

        self.assertEqual(1, len(responses.calls))

    @responses.activate
    def test_the_request_parameters(self):
        """
        Match the request parameters in the HTTP request.
        """
        call_a_basic_response()

        request = responses.calls[0].request
        self.assertEqual('GET', request.method)
        self.assertEqual('http', request.scheme)
        self.assertEqual('www.fake_url.com', request.host)
        self.assertEqual('/', request.url)

    @responses.activate
    def test_the_response_match_with_the_returned_dictionary(self):
        """
        Match the response dictionary from the HTTP request.
        """
        responses.add(
            method='GET',
            url='/',
            body='this is the body',
            status=299,
            content_type='text/html'
        )

        response = get(url='http://www.fake_url.com')

        self.assertEqual(299, response.get('status'))
        self.assertEqual('text/html', response.get('headers').getheaders('Content-Type')[0])
        self.assertEqual(b'this is the body', response.get('data'))
        self.assertEqual(None, response.get('reason'))
        self.assertEqual(True, response.get('decode_content'))


def call_a_basic_response():
    """
    Call a basic response and execute the get module for http web_page package.
    """
    responses.add(method='GET', url='/')

    get(url='http://www.fake_url.com')
