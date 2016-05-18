from service.bookturks.Constants import QUIZ_HOME


class DropboxClient:
    """
     DropBox client
        Quiz related functions
    """

    def __init__(self, client):
        """
        Create a DropBox Client object
        """
        self.client = client

    def upload_file(self, content, filename):
        """
        Uploads content creating a new file
        :param content: content of file
        :param filename: create a file with this name on dropbox
        :return: file id from dropbox
        """

        return self.client.files_upload(content, filename)

    def list_quiz_files(self, filters=None):
        """
        Lists the quiz files filtering out required quiz results
        :param filters: filters to be provided in future
        :return: List of File objects of all quizzes matching the filter
        """
        result_list = list()
        list_of_files = self.client.files_list_folder(QUIZ_HOME)
        if not filters:
            while True:
                for entry in list_of_files.entries:
                    result_list.append(entry)
                if not list_of_files.has_more:
                    break
                else:
                    list_of_files = self.client.files_list_folder_continue(list_of_files.cursor)
        return result_list
