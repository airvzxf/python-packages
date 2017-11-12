#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Test case for extract content from Gzip file.
"""

from unittest import TestCase

from mock import Mock, patch

from pkg.os.file.type.tar_gz.extract import TarError, extract


class TestPkgOsFileTypeTarGzExtract(TestCase):
    """
    Test to extract a tar gz file form the operative system.
    """

    def test_the_default_parameters(self):
        """
        Return false if it send the default parameters that include directory to none.
        """
        extracted = extract()

        self.assertEqual(False, extracted)

    def test_if_the_path_is_empty(self):
        """
        Return false if it path is empty.
        """
        extracted = extract(path='')

        self.assertEqual(False, extracted)

    def test_if_the_extract_path_is_empty(self):
        """
        Return false if it extract path is empty.
        """
        extracted = extract(path='fake_path', extract_path='')

        self.assertEqual(False, extracted)

    @patch('pkg.os.file.type.tar_gz.extract.open_tarfile')
    def test_if_the_open_file_raise_any_OSError(self, mock_open_tarfile):
        """
        Return false if the file does't exist or any OSError.
        """
        mock_open_tarfile.side_effect = OSError

        extracted = extract(path='fake_file.tar.gz')

        self.assertEqual(False, extracted)

    @patch('pkg.os.file.type.tar_gz.extract.open_tarfile')
    def test_if_the_file_exists_and_was_opened(self, mock_open_tarfile):
        """
        Check if the file exist and was opened that means the method open_tarfile was called.
        """
        extract(path='fake_file.tar.gz', extract_path='./')

        mock_open_tarfile.assert_called_once_with('fake_file.tar.gz', 'r:gz')

    @patch('pkg.os.file.type.tar_gz.extract.open_tarfile')
    def test_if_the_file_was_not_extracted(self, mock_open_tarfile):
        """
        Check if the file is empty, it's not a tar file or any Tar Error.
        """
        mocked_tar_gz = Mock()
        mock_open_tarfile.return_value.__enter__.side_effect = TarError

        extract(path='fake_file.tar.gz', extract_path='./')

        mocked_tar_gz.extractall.assert_not_called()

    @patch('pkg.os.file.type.tar_gz.extract.open_tarfile')
    def test_if_the_file_was_extracted(self, mock_open_tarfile):
        """
        Check if the file was extracted that means the method extractall was called.
        """
        mocked_tar_gz = Mock()
        mock_open_tarfile.return_value.__enter__.return_value = mocked_tar_gz

        extract(path='fake_file.tar.gz', extract_path='./')

        mocked_tar_gz.extractall.assert_called_once_with('./')

    @patch('pkg.os.file.type.tar_gz.extract.open_tarfile')
    def test_if_the_file_was_extracted_successful(self, mock_open_tarfile):
        """
        Return true if the file was extracted successful.
        """
        mock_open_tarfile.return_true = True

        extracted = extract(path='fake_file.tar.gz', extract_path='./')

        self.assertEqual(True, extracted)
