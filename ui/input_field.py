from ui.ui_element import UIElement


class InputField(UIElement):
    """
    Class representing input fields, text areas, and range sliders.
    Provides specific methods for entering text and setting values.
    """

    def enter_text(self, text: str, timeout: int = 10) -> None:
        """
        Enters text into the input field.

        Args:
            text (str): The text to be entered into the element.
            timeout (int): Maximum time to wait for the element. Default is 10s.
        """
        self.logger.info(f"Entering text '{text}' into: {self.xpath}")
        try:
            self.controller.enter_text_safely(self.xpath, text, timeout)
        except Exception as e:
            self.logger.error(f"Failed to enter text. Error: {e}")
            raise

    def set_value(self, value: str, timeout: int = 10) -> None:
        """
        Sets the value of an element directly using JavaScript.
        Recommended for elements like range sliders (<input type="range">).

        Args:
            value (str): The value to set on the element.
            timeout (int): Maximum time to wait for the element. Default is 10s.
        """
        self.logger.info(f"Setting value '{value}' for: {self.xpath}")
        try:
            self.controller.set_element_value(self.xpath, value, timeout)
        except Exception as e:
            self.logger.error(f"Failed to set value. Error: {e}")
            raise
