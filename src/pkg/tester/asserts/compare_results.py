#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Test case for search all tags from HTML code.
"""


def compare_results(self=None, total_results=0, expected_results=None, results=None):
    """
    Assert the expected results versus the results.

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

    for index in range(total_results):
        self.assertEqual(expected_results[index], results[index])
