#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Test case for show methods when you need debug."""

import contextlib
import re
import unittest
from io import StringIO

from src.pkg.debug.method.show_available import show_available


class TestPkgDebugMethodShowAvailable(unittest.TestCase):
    """Tests for show methods in debug mode"""

    def setUp(self):
        """Always check if the method crash with any error, it shouldn't crash"""
        _catch_any_exception_error(self)

    def test_when_main_object_is_none_not_execute_the_statements(self):
        """"Not print anything in the console"""

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            show_available(print_all=True, print_available=True)
        output = _output_formatter(temp_stdout)

        self.assertEqual('', output)

    def test_show_all_but_not_show_available(self):
        """Catch the print output"""
        # Uncomment this to show the values in the console
        # show_available(main_object=[], show_all=True, show_available=False)

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            show_available(main_object=[], print_all=True, print_available=False)
        output = _output_formatter(temp_stdout)

        expected_output = '[]\n'
        expected_output += "['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', "
        expected_output += "'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', "
        expected_output += "'__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', "
        expected_output += "'__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', "
        expected_output += "'__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', "
        expected_output += "'__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', "
        expected_output += "'insert', 'pop', 'remove', 'reverse', 'sort']"

        self.assertEqual(expected_output, output)

    def test_show_available_but_not_show_all(self):
        """Catch the print output"""
        # Uncomment this to show the values in the console
        # show_available(main_object=[], show_all=False, show_available=True)

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            show_available(main_object=[], print_all=False, print_available=True)
        output = _output_formatter(temp_stdout)

        expected_output = '[]\n'
        expected_output += "object.__class__(): []\n"
        expected_output += "object.__init__(): None\n"
        expected_output += "object.__init_subclass__(): None\n"
        expected_output += "object.__iter__(): <list_iterator object at 0x0>\n"
        expected_output += "object.__len__(): 0\n"
        expected_output += "object.__repr__(): []\n"
        expected_output += "object.__reversed__(): <list_reverseiterator object at 0x0>\n"
        expected_output += "object.__sizeof__(): 40\n"
        expected_output += "object.__str__(): []\n"
        expected_output += "object.__subclasshook__(): NotImplemented\n"
        expected_output += "object.clear(): None\n"
        expected_output += "object.copy(): []\n"
        expected_output += "object.reverse(): None\n"
        expected_output += "object.sort(): None"

        self.assertEqual(expected_output, output)


def _catch_any_exception_error(self):
    method_returned = False

    # noinspection PyBroadException
    try:
        with contextlib.redirect_stdout(StringIO()):
            method_returned = show_available(main_object={}, print_all=False, print_available=True)
    except Exception:
        pass

    self.assertIsNone(method_returned, "It shouldn't crash wit any exception error. All the error should be pass.")


def _output_formatter(stdout_string=None):
    if stdout_string is None:
        return

    get_value = stdout_string.getvalue().strip()
    output = re.sub(r"0x\w+", "0x0", get_value)

    return output


if __name__ == '__main__':
    unittest.main()
