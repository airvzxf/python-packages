#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Module which compare a list of results to assert the test.
"""


def compare_list_results(self=None, total_results=0, expected_results=None, results=None):
    """
    Assert the list of the expected results versus the results.

    :param self: Unit test object.
    :param total_results:  Number of result to needs to match.
    :param expected_results: List with the expected results.
    :param results: List with the results which needs compare.
    """
    if results is None:
        results = []

    if expected_results is None:
        expected_results = []

    self.assertEqual(total_results, len(results))

    self.assertEqual(expected_results, results)