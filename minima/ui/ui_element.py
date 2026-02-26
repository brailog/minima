import re
import time

from minima.engine.context import current_session
from minima.logs.logger_utils import initialize_logger
from minima.settings.exceptions import ElementNotVisibleException


class UIElement:
    """
    Base class representing a general UI element on the page.
    Provides core interaction methods like click, hover, drag, and scroll,
    as well as locator logic.
    """

    def __init__(self, controller: object = None, **kwargs: str) -> None:
        """
        Initializes the Widget with the specified controller and attributes for XPath construction.

        Args:
            controller (object, optional): The controller instance (e.g., BrowserController). Defaults to None.
            **kwargs (str): Keyword arguments representing the attributes of the element to build the XPath.

        Raises:
            RuntimeError: If no controller is provided and no active session is found in context.
        """
        if controller is not None:
            self.session = controller
        else:
            try:
                self.session = current_session.get()
            except LookupError:
                raise RuntimeError(
                    "No driver provided and no active browser session found in context. "
                    "Make sure you are running inside the @browser_session decorator or "
                    "explicitly pass a driver."
                )

        self.logger = initialize_logger(self.__class__.__name__)
        self.logger.debug(
            f"Initializing {self.__class__.__name__} with attributes: {kwargs}"
        )

        self.controller = self.session
        self.attrs = kwargs
        self.xpath = self._build_xpath()

        self.logger.debug(
            f"Constructed XPath for {self.__class__.__name__}: {self.xpath}"
        )

    def _build_xpath(self) -> str:
        """
        Constructs the XPath string based on the provided attributes.

        Returns:
            str: The constructed XPath for locating the element.
        """
        xpath = "//*"
        conditions = []
        for attr, value in self.attrs.items():
            attr = re.sub(r"_", "-", attr)
            if attr == "text":
                conditions.append(f"contains(text(), '{value}')")
            elif "class-" in attr:
                conditions.append(f"@class='{value}'")
            else:
                conditions.append(f"@{attr}='{value}'")

        if conditions:
            xpath += "[" + " and ".join(conditions) + "]"
        return xpath

    @staticmethod
    def _extract_element_properties(element: object) -> dict[str, object]:
        """
        Extracts properties from a single Selenium WebElement.

        Args:
            element (object): The WebElement to extract properties from.

        Returns:
            dict[str, object]: A dictionary containing properties for the given element.
        """
        attributes = {
            attr_name: element.get_attribute(attr_name)
            for attr_name in [
                "id",
                "class",
                "name",
                "type",
                "value",
                "href",
                "src",
                "alt",
                "aria-label",
            ]
            if element.get_attribute(attr_name) is not None
        }
        return {
            "text": element.text,
            "tag_name": element.tag_name,
            "attributes": attributes,
            "location": element.location,
            "size": element.size,
            "displayed": element.is_displayed(),
            "enabled": element.is_enabled(),
        }

    # Core Action Methods
    def click(self, timeout: int = 10) -> None:
        """
        Clicks on the element identified by the constructed XPath.

        Args:
            timeout (int): Maximum time to wait for the element to be present. Default is 10s.
        """
        self.logger.info(f"Attempting to click: {self.xpath} (Timeout: {timeout}s)")
        try:
            self.controller.click_element(self.xpath, timeout)
        except Exception as e:
            self.logger.error(f"Failed to click: {self.xpath}. Error: {e}")
            raise

    def double_click(self, delay: float = 0.1, timeout: int = 10) -> None:
        """
        Performs a double-click on the element.

        Args:
            delay (float): Time in seconds to wait between clicks. Default is 0.1s.
            timeout (int): Maximum time to wait for the element. Default is 10s.
        """
        self.logger.info(f"Performing double-click: {self.xpath}")
        try:
            for _ in range(2):
                self.click(timeout)
                time.sleep(delay)
        except Exception as e:
            self.logger.error(f"Failed to double-click. Error: {e}")
            raise

    def hover(self, timeout: int = 10) -> None:
        """
        Simulates a mouse hover action over the element.

        Args:
            timeout (int): Maximum time to wait for the element to be present. Default is 10s.
        """
        self.logger.info(f"Hovering over: {self.xpath}")
        try:
            self.controller.hover_element(self.xpath)
        except Exception as e:
            self.logger.error(f"Failed to hover. Error: {e}")
            raise

    def unhover(self, timeout: int = 10) -> None:
        """
        Moves the mouse away from the current element to remove the hover state.

        Args:
            timeout (int): Maximum time to wait for the action to complete. Default is 10s.
        """
        self.logger.info(f"Unhovering from: {self.xpath}")
        try:
            self.controller.unhover_element(timeout)
        except Exception as e:
            self.logger.error(f"Failed to unhover. Error: {e}")
            raise

    def scroll_to(self, timeout: int = 10) -> None:
        """
        Scrolls the browser view to the element.

        Args:
            timeout (int): Maximum time to wait for the element to be present. Default is 10s.
        """
        self.logger.info(f"Scrolling to: {self.xpath}")
        try:
            self.controller.scroll_to_element(self.xpath, timeout)
        except Exception as e:
            self.logger.error(f"Failed to scroll. Error: {e}")
            raise

    def drag_to(self, target_widget: "Widget", timeout: int = 10) -> None:
        """
        Drags the current widget and drops it onto the target widget.

        Args:
            target_widget (UIElement): The widget instance to drop onto.
            timeout (int): Maximum time to wait for the elements. Default is 10s.
        """
        self.logger.info(f"Dragging '{self.xpath}' to '{target_widget.xpath}'.")
        try:
            self.controller.drag_and_drop(self.xpath, target_widget.xpath, timeout)
        except Exception as e:
            self.logger.error(f"Failed to drag and drop. Error: {e}")
            raise

    # Core Data & Wait Methods
    def wait_for(self, timeout: int = 10) -> object:
        """
        Waits until the element identified by the XPath is visible.

        Args:
            timeout (int): Maximum time to wait for the element to become visible. Default is 10s.

        Returns:
            object: The WebElement if found and visible.

        Raises:
            ElementNotVisibleException: If the element is not visible within the timeout.
        """
        self.logger.info(f"Waiting for: {self.xpath}")
        try:
            return self.controller.wait_for_element(self.xpath, timeout)
        except Exception as e:
            self.logger.error(f"Failed to wait for: {self.xpath}. Error: {e}")
            raise ElementNotVisibleException(self.xpath, timeout, e)

    def properties(self, timeout: int = 10) -> dict[str, object]:
        """
        Extracts and returns properties of the first element identified by the XPath.

        Args:
            timeout (int): Maximum time to wait for the element. Default is 10s.

        Returns:
            dict[str, object]: A dictionary containing properties for the first matching element.
        """
        try:
            element = self.wait_for(timeout)
            return self._extract_element_properties(element)
        except Exception as e:
            self.logger.error(f"Failed to retrieve properties. Error: {e}")
            raise

    def get_attribute(self, attribute_name: str, timeout: int = 10) -> str:
        """
        Retrieves the value of a specific attribute from the element.

        Args:
            attribute_name (str): The name of the attribute to retrieve.
            timeout (int): Maximum time to wait for the element. Default is 10s.

        Returns:
            str: The value of the specified attribute.
        """
        try:
            element = self.wait_for(timeout)
            return element.get_attribute(attribute_name)
        except Exception as e:
            self.logger.error(f"Failed to get attribute '{attribute_name}'. Error: {e}")
            raise

    def _all_properties(self, timeout: int = 10) -> list[dict[str, object]]:
        """
        Extracts and returns properties of all elements that match the XPath.

        Args:
            timeout (int): Maximum time to wait for the elements. Default is 10s.

        Returns:
            list[dict[str, object]]: A list of dictionaries containing properties for each matching element.
        """
        try:
            elements = self.controller.wait_for_all_elements(self.xpath)
            return [self._extract_element_properties(el) for el in elements]
        except Exception as e:
            self.logger.error(f"Failed to retrieve all properties. Error: {e}")
            raise
