from django.test import TestCase

import mock
import dropbox
from service.bookturks.dropbox_adapter.DropboxClient import DropboxClient
from service.bookturks.Constants import QUIZ_HOME
from service.tests.dropbox_tools import MockFileList


class DropboxClientTest(TestCase):
    """
    Test case for the DropBox Client
    """

    @mock.patch('dropbox.Dropbox', autospec=True)
    def setUp(self, mock_dbx):
        """
        Initialization for all tests
        :return:
        """
        dbx = mock_dbx.return_value
        dbx.files_upload.return_value = "mock_id"
        self.dbx = dbx
        self.client = DropboxClient(dbx)

    def test_dropbox_upload_file(self):
        """
        Testing the dropbox client
        :return:
        """
        result = self.client.upload_file(content="mock_content", filename="mock_filename")
        self.assertEqual("mock_id", result)
        self.dbx.files_upload.assert_called_once_with("mock_content", "mock_filename",
                                                      mode=dropbox.files.WriteMode.overwrite)
