#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Test case for delete a directory in the Operative System.
"""

from unittest import TestCase

from mock import patch

from pkg.os.directory.delete import delete


class TestPkgOsDirectoryDelete(TestCase):
    """
    Test to delete a directory form the operative system.
    """

    def test_the_default_parameters(self):
        """
        Return false if it send the default parameters that include directory to none.
        """
        deleted = delete()

        self.assertIsNone(deleted)

    @patch('pkg.os.directory.delete.exists')
    def test_if_exists_directory_is_not_called(self, mock_exists):
        """
        Return false because the exits method wasn't called.
        """
        _mock_delete_module(
            path=False,
            mocks=(
                (mock_exists, None),
            )
        )

        mock_exists.assert_not_called()

    @patch('pkg.os.directory.delete.isdir')
    @patch('pkg.os.directory.delete.exists')
    def test_if_the_path_does_not_exist_and_it_is_not_a_directory(self, mock_exists, mock_isdir):
        """
        Return false because the path doesn't exist and it isn't a directory.
        """
        deleted = _mock_delete_module(
            mocks=(
                (mock_exists, False),
                (mock_isdir, False)
            )
        )

        self.assertEqual(False, deleted)

    @patch('pkg.os.directory.delete.isdir')
    @patch('pkg.os.directory.delete.exists')
    def test_if_the_path_does_not_exist(self, mock_exists, mock_isdir):
        """
        Return false because the path doesn't exist and it isn't a directory.
        """
        deleted = _mock_delete_module(
            mocks=(
                (mock_exists, False),
                (mock_isdir, True)
            )
        )

        self.assertEqual(False, deleted)

    @patch('pkg.os.directory.delete.isdir')
    @patch('pkg.os.directory.delete.exists')
    def test_if_the_path_is_not_a_directory(self, mock_exists, mock_isdir):
        """
        Return false because the path doesn't exist and it isn't a directory.
        """
        deleted = _mock_delete_module(
            mocks=(
                (mock_exists, True),
                (mock_isdir, False)
            )
        )

        self.assertEqual(False, deleted)

    @patch('pkg.os.directory.delete.rmtree')
    @patch('pkg.os.directory.delete.isdir')
    @patch('pkg.os.directory.delete.exists')
    def test_if_the_path_does_exist_and_it_is_a_directory(self, mock_exists, mock_isdir, mock_rmtree):
        """
        Return true because the path does exist and it is a directory.
        """
        mock_rmtree.return_value = None

        deleted = _mock_delete_module(
            mocks=(
                (mock_exists, True),
                (mock_isdir, True),
                (mock_rmtree, None)
            )
        )

        self.assertEqual(True, deleted)

    @patch('pkg.os.directory.delete.rmtree')
    @patch('pkg.os.directory.delete.isdir')
    @patch('pkg.os.directory.delete.exists')
    def test_if_rmtree_is_called(self, mock_exists, mock_isdir, mock_rmtree):
        """
        Return true because the path does exist and it is a directory.
        """
        _mock_delete_module(
            mocks=(
                (mock_exists, True),
                (mock_isdir, True)
            )
        )

        mock_rmtree.assert_called_once_with('')


def _mock_delete_module(mocks: tuple, path: bool = True) -> bool:
    """
    Helper function which set the mock values.

    :param mocks: List with the mock tuple (mock object and boolean value).
    :param path: The path in the system for example '/home/user/personal/file.txt'
    :return: True or false which is determined from the delete method.

    :rtype: bool
    """
    path_string = None

    if path:
        path_string = ''

    for mock_values in mocks:
        _mock_method(mock_values=mock_values)

    deleted = delete(path=path_string)

    return deleted


def _mock_method(mock_values: tuple = None):
    """
    Set a value to specific mock object.

    :param mock_values: Tuple with the mock object and value (object, value).
    """
    if mock_values is not None:
        mock_object, mock_value = mock_values
        mock_object.return_value = mock_value
