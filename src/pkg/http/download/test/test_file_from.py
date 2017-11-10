#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Test case for download a single file from some URL via HTTP.
"""

from unittest import TestCase

from mock import patch

from pkg.http.download.file_from import HTTPError, file_from


class TestPkgHttpDownloadFileFrom(TestCase):
    """
    Test to download a single file from some URL via HTTP.
    """

    def test_the_default_parameters(self):
        """
        Return None if it send the default parameters that include url equal to none.
        """
        downloaded = file_from()

        self.assertIsNone(downloaded)

    @patch('pkg.http.download.file_from.urlretrieve')
    def test_if_urlretrieve_is_not_called(self, mock_urlretrieve):
        """
        Returns false if not calls the urlretrieve packages which is imported from urllib.request.
        """
        file_from()

        mock_urlretrieve.assert_not_called()

    @patch('pkg.http.download.file_from.urlretrieve')
    def test_if_urlretrieve_is_called(self, mock_urlretrieve):
        """
        Returns true if calls the urlretrieve packages which is imported from urllib.request.
        """
        file_from(url='')

        mock_urlretrieve.assert_called()

    @patch('pkg.http.download.file_from.urlretrieve')
    def test_if_urlretrieve_calls_once(self, mock_urlretrieve):
        """
        Returns 1 if calls the urlretrieve packages.
        """
        file_from(url='')

        mock_urlretrieve.assert_called_once()

    @patch('pkg.http.download.file_from.urlretrieve')
    def test_if_urlretrieve_send_only_the_url_parameter(self, mock_urlretrieve):
        """
        Validate the parameter url that was sent in the urlretrieve method.
        """
        expected_url = 'http://anything.com/my_file.txt'

        file_from(url=expected_url)

        mock_urlretrieve.assert_called_once_with(filename=None, url=expected_url)

    @patch('pkg.http.download.file_from.urlretrieve')
    def test_if_urlretrieve_send_only_the_filename_parameter(self, mock_urlretrieve):
        """
        Validate the parameter file name that was sent in the urlretrieve method.
        """
        expected_filename = 'fake_file.txt'

        file_from(url='', filename=expected_filename)

        mock_urlretrieve.assert_called_once_with(filename=expected_filename, url='')

    @patch('pkg.http.download.file_from.urlretrieve')
    def test_if_the_url_is_correct_returns_true(self, mock_urlretrieve):
        """
        If the url is correct it returns false and checks urlretrieve was called.
        """
        mock_urlretrieve.return_value = None

        downloaded = file_from(url='')

        self.assertEqual(True, downloaded)

    @patch('pkg.http.download.file_from.urlretrieve')
    def test_if_the_url_is_not_correct_returns_false(self, mock_urlretrieve):
        """
        If the url is not correct it returns false and checks urlretrieve was called.
        """
        mock_urlretrieve.side_effect = HTTPError(url=None, code=None, msg=None, hdrs=None, fp=None)

        downloaded = file_from(url='')

        self.assertEqual(False, downloaded)

    @patch('pkg.http.download.file_from.urlretrieve')
    def test_when_the_file_is_not_stored_in_the_hard_disk(self, mock_urlretrieve):
        """
        Validate when the file is not stored in the hard disk.
        """
        mock_urlretrieve.side_effect = FileNotFoundError

        downloaded = file_from(url='', filename='~/DirectoryNotExist/fake_file.txt')

        self.assertEqual(False, downloaded)
