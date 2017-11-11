#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Test case for delete a file in the Operative System.
"""

from unittest import TestCase

from mock import patch

from pkg.os.file.delete import delete


class TestPkgOsFileDelete(TestCase):
    """
    Test to delete a file form the operative system.
    """

    # noinspection PyUnusedLocal
    @patch('pkg.os.file.delete.isfile')
    @patch('pkg.os.file.delete.exists')
    def patching_exists_isfile(*args: object) -> object:
        """
        This helper function create a decorator function with the required patches and
        then apply to the tester classes.

        :param args: Any parameter in this case: self, and patches for exists, isfile and remove.
        :return: Return the object which means the self function with the parameters.
        :rtype: object
        """
        return object

    # noinspection PyUnusedLocal
    @patch('pkg.os.file.delete.remove')
    @patch('pkg.os.file.delete.isfile')
    @patch('pkg.os.file.delete.exists')
    def patching_exists_isfile_remove(*args: object) -> object:
        """
        This helper function create a decorator function with the required patches and
        then apply to the tester classes.

        :param args: Any parameter in this case: self, and patches for exists, isfile and remove.
        :return: Return the object which means the self function with the parameters.
        :rtype: object
        """
        return object

    def test_the_default_parameters(self):
        """
        Return None if it send the default parameters that include file to none.
        """
        deleted = delete()

        self.assertFalse(deleted)

    @patch('pkg.os.file.delete.exists')
    def test_if_exists_file_is_not_called(self, mock_exists):
        """
        Return false because the exits method wasn't called.
        """
        _mock_delete_module(path=False,
                            mock_exists=(mock_exists, None))

        mock_exists.assert_not_called()

    @patching_exists_isfile
    def test_if_the_path_does_not_exist_and_it_is_not_a_file(self, mock_exists, mock_isfile):
        """
        Return false because the path doesn't exist and it isn't a file.
        """
        deleted = _mock_delete_module(mock_exists=(mock_exists, False),
                                      mock_isfile=(mock_isfile, False))

        self.assertEqual(False, deleted)

    @patching_exists_isfile
    def test_if_the_path_does_not_exist(self, mock_exists, mock_isfile):
        """
        Return false because the path doesn't exist and it isn't a file.
        """
        deleted = _mock_delete_module(mock_exists=(mock_exists, False),
                                      mock_isfile=(mock_isfile, True))

        self.assertEqual(False, deleted)

    @patching_exists_isfile
    def test_if_the_path_is_not_a_file(self, mock_exists, mock_isfile):
        """
        Return false because the path doesn't exist and it isn't a file.
        """
        deleted = _mock_delete_module(mock_exists=(mock_exists, True),
                                      mock_isfile=(mock_isfile, False))

        self.assertEqual(False, deleted)

    @patching_exists_isfile_remove
    def test_if_the_path_does_exist_and_it_is_a_file(self, mock_exists, mock_isfile, mock_remove):
        """
        Return true because the path does exist and it is a file.
        """
        mock_remove.return_value = None
        deleted = _mock_delete_module(mock_exists=(mock_exists, True),
                                      mock_isfile=(mock_isfile, True),
                                      mock_remove=(mock_remove, None))

        self.assertEqual(True, deleted)

    @patching_exists_isfile_remove
    def test_if_remove_is_called(self, mock_exists, mock_isfile, mock_remove):
        """
        Return true because the path does exist and it is a file.
        """
        _mock_delete_module(mock_exists=(mock_exists, True),
                            mock_isfile=(mock_isfile, True))

        mock_remove.assert_called_once_with('')


def _mock_delete_module(path=True, mock_exists=None, mock_isfile=None, mock_remove=None):
    """
    Helper function which set the mock values.

    :param mock_exists: Mock object for the exists method and its value.
    :param mock_isfile: Mock object for the isfile method and its value.
    :param mock_remove: Mock object for the remove method and its value.
    :return: True or false which is determined from the delete method.
    """

    path_string = None

    if path:
        path_string = ''

    _mock_method(mock_exists)
    _mock_method(mock_isfile)
    _mock_method(mock_remove)

    deleted = delete(path=path_string)

    return deleted


def _mock_method(mock):
    """
    Set a value to specific mock object.

    :param mock: Tuple with the mock object and value (object, value).
    """
    if mock is not None:
        mock_object, mock_value = mock
        mock_object.return_value = mock_value
