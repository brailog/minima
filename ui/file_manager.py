from ui.ui_element import UIElement


class FileManager(UIElement):
    """
    Class representing file upload inputs (e.g., <input type="file">).
    """

    def upload_file(self, file_path: str, timeout: int = 10) -> None:
        """
        Uploads a file to the element.

        Args:
            file_path (str): The absolute path of the file to upload.
            timeout (int): Maximum time to wait for the element. Default is 10s.
        """
        self.logger.info(f"Uploading file '{file_path}' to: {self.xpath}")
        try:
            self.controller.upload_file(self.xpath, file_path, timeout)
        except Exception as e:
            self.logger.error(f"Failed to upload file. Error: {e}")
            raise
