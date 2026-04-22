import logging

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Mouse:
    """
    Controla interações de baixo nível do mouse usando ActionChains nativo do Selenium.
    """

    def __init__(self, driver: WebDriver) -> None:
        """Inicializa o Mouse recebendo o driver atual do navegador."""
        self.driver: WebDriver = driver
        self.logger: logging.Logger = logging.getLogger(self.__class__.__name__)

    def _get_actions(self) -> ActionChains:
        """Gera uma nova instância de ActionChains para encadear eventos."""
        return ActionChains(self.driver)

    def click(self, web_element: WebElement) -> None:
        """Clica em um elemento físico (WebElement) da página."""
        self.logger.debug("Executando click nativo do mouse.")
        self._get_actions().click(web_element).perform()

    def double_click(self, web_element: WebElement) -> None:
        """Dá um duplo clique nativo em um WebElement."""
        self.logger.debug("Executando duplo clique nativo do mouse.")
        self._get_actions().double_click(web_element).perform()

    def hover(self, web_element: WebElement) -> None:
        """Move o ponteiro do mouse para cima do WebElement."""
        self.logger.debug("Executando hover (move_to_element).")
        self._get_actions().move_to_element(web_element).perform()

    def unhover(self) -> None:
        """Move o mouse para o canto superior esquerdo do <body> para tirar o hover."""
        self.logger.debug("Removendo o hover do mouse.")
        body: WebElement = self.driver.find_element("tag name", "body")
        self._get_actions().move_to_element_with_offset(body, 0, 0).perform()

    def drag_and_drop(
        self, source_element: WebElement, target_element: WebElement
    ) -> None:
        """Clica e segura um WebElement e o solta em cima de outro WebElement."""
        self.logger.debug("Executando drag and drop.")
        self._get_actions().drag_and_drop(source_element, target_element).perform()
