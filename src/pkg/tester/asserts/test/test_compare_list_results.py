#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Test case to assert the list of the expected results.
"""

from unittest import TestCase

from pkg.tester.asserts.compare_list_results import compare_list_results


class TestPkgTesterAssertsCompareResults(TestCase):
    """
    Compare the results with the expected results and assert them.
    """

    def test_the_default_values(self):
        """
        Test the defaults values and the test assert.
        """
        compare_list_results(self)

    def test_when_total_results_is_one(self):
        """
        Test when we send one result and the test assert.
        """
        compare_list_results(self, total_results=1, expected_results=['a'], results=['a'])

    def test_when_total_results_is_three(self):
        """
        Test when we send two results and the test assert.
        """
        compare_list_results(self, total_results=3, expected_results=[9, 8, 7], results=[9, 8, 7])

    def test_when_not_send_parameters(self):
        """
        Test when the self parameter is not send and assert fails.
        """
        try:
            compare_list_results()
        except AttributeError as error:
            expected_error = "'NoneType' object has no attribute 'assertEqual'"
            self.assertEqual(expected_error, str(error))

    def test_when_number_of_results_is_lower_to_results(self):
        """
        Test when the total results is less than the results and assert fails.
        """
        try:
            compare_list_results(self, total_results=1, results=[9, 8, 7])
        except AssertionError as error:
            expected_error = "1 != 3"
            self.assertEqual(expected_error, str(error))

    def test_when_number_of_results_is_greater_to_results(self):
        """
        Test when the total results is greater than the results and assert fails.
        """
        try:
            compare_list_results(self, total_results=3, results=[9])
        except AssertionError as error:
            expected_error = "3 != 1"
            self.assertEqual(expected_error, str(error))

    def test_when_the_result_is_different_of_the_expected(self):
        """
        Test when the results different to the expected results and assert fails.
        """
        try:
            compare_list_results(self, total_results=1, expected_results=['b'], results=['c'])
        except AssertionError as error:
            expected_error = "Lists differ: ['b'] != ['c']"
            self.assertTrue(expected_error in str(error))
