from ui.ui_element import UIElement


class Dropdown(UIElement):
    """
    Class representing standard HTML select dropdowns (<select>).
    Provides methods for selecting and deselecting options.
    """

    def select_by_text(self, text: str, timeout: int = 10) -> None:
        """
        Selects an option from the dropdown by its visible text.

        Args:
            text (str): The visible text of the option to select.
            timeout (int): Maximum time to wait for the element. Default is 10s.
        """
        self.logger.info(f"Selecting '{text}' by text from: {self.xpath}")
        self.controller.select_option_by_text(self.xpath, text, timeout)

    def select_by_value(self, value: str, timeout: int = 10) -> None:
        """
        Selects an option from the dropdown by its 'value' attribute.

        Args:
            value (str): The value attribute of the option to select.
            timeout (int): Maximum time to wait for the element. Default is 10s.
        """
        self.logger.info(f"Selecting value '{value}' from: {self.xpath}")
        self.controller.select_option_by_value(self.xpath, value, timeout)

    def select_by_index(self, index: int, timeout: int = 10) -> None:
        """
        Selects an option from the dropdown by its index (0-based).

        Args:
            index (int): The index of the option to select.
            timeout (int): Maximum time to wait for the element. Default is 10s.
        """
        self.logger.info(f"Selecting index {index} from: {self.xpath}")
        self.controller.select_option_by_index(self.xpath, index, timeout)

    def deselect_all(self, timeout: int = 10) -> None:
        """
        Deselects all options in a multi-select dropdown.

        Args:
            timeout (int): Maximum time to wait for the element. Default is 10s.
        """
        self.logger.info(f"Deselecting all options from: {self.xpath}")
        self.controller.deselect_all_options(self.xpath, timeout)

    def deselect_by_text(self, text: str, timeout: int = 10) -> None:
        """
        Deselects an option from a multi-select dropdown by its visible text.

        Args:
            text (str): The visible text of the option to deselect.
            timeout (int): Maximum time to wait for the element. Default is 10s.
        """
        self.logger.info(f"Deselecting '{text}' by text from: {self.xpath}")
        self.controller.deselect_option_by_text(self.xpath, text, timeout)

    def get_selected_texts(self, timeout: int = 10) -> list[str]:
        """
        Gets the text of all selected options from the dropdown.

        Args:
            timeout (int): Maximum time to wait for the element. Default is 10s.

        Returns:
            list[str]: A list containing the visible text of all selected options.
        """
        self.logger.info(f"Getting selected texts from: {self.xpath}")
        return self.controller.get_all_selected_options_text(self.xpath, timeout)