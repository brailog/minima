import os
import random
import time

from pyminima.engine.context import browser_session
from pyminima.ui.browser import Browser
from pyminima.ui.button import Button
from pyminima.ui.dropdown import Dropdown
from pyminima.ui.file_manager import FileManager
from pyminima.ui.input_field import InputField
from pyminima.ui.text import Text, Textlink
from pyminima.ui.ui_element import UIElement

base_dir = os.path.dirname(os.path.abspath(__file__))
MOCKUP_TEST_URL_FILE = "http://localhost:5173/playground"


# ── NAVIGATION ──
def select_full_mode():
    Button(text="Jornada Completa").click()


def skip_intro():
    Button(text="Começar").click()


def navigate_next():
    Button(text="Próximo").click()


# ── BUTTONS SECTION ──
def test_botoes():
    Button(id="primary-btn", text="Botão Primário").click()
    mensagem = Text(id="button-click-message").properties().get("text")
    assert "Primário" in mensagem

    Button(id="secondary-btn", text="Botão Secundário").click()
    mensagem = Text(id="button-click-message").properties().get("text")
    assert "Secundário" in mensagem

    Button(id="danger-btn", text="Botão Perigo").click()
    mensagem = Text(id="button-click-message").properties().get("text")
    assert "Perigo" in mensagem

    disabled_btn = Button(id="disabled-btn")
    assert disabled_btn.properties().get("enabled") is False

    navigate_next()


# ── LINKS SECTION ──
def test_links():
    Textlink(id="simple-link", text="Simples").click()
    Browser.accept_alert()

    Textlink(id="new-tab-link", text="Nova Aba").click()
    Browser.switch_to_new_tab()
    Browser.close_current_tab()

    Textlink(id="download-link", text="Download").click()
    time.sleep(0.5)

    navigate_next()


# ── HOVER SECTION ──
def test_hover():
    hover_div = UIElement(id="hover-div")
    hover_status = Text(id="hover-status")

    assert "não está" in hover_status.properties().get("text")
    for _ in range(3):
        hover_div.hover()
        assert "está sobre" in hover_status.properties().get("text")
        time.sleep(0.5)
        hover_div.unhover()
        assert "não está" in hover_status.properties().get("text")

    navigate_next()


# ── TABS SECTION ──
def test_tabs():
    tab1_content = Text(id="tab1")
    assert "primeira" in tab1_content.properties().get("text")

    UIElement(data_tab="tab2").click()
    tab2_content = Text(id="tab2")
    assert "segunda" in tab2_content.properties().get("text")

    UIElement(data_tab="tab3").click()
    tab3_content = Text(id="tab3")
    assert "terceira" in tab3_content.properties().get("text")

    navigate_next()


# ── MODAL SECTION ──
def test_modal():
    Button(id="open-modal-btn", text="Abrir Modal").click()
    modal = UIElement(id="test-modal")

    assert "modal simples" in modal.properties().get("text")
    assert modal.properties().get("displayed")

    close_btn = Button(id="modal-close-btn", text="Fechar")
    assert close_btn.properties().get("displayed")
    close_btn.click()

    navigate_next()


# ── ALERTS SECTION ──
def test_alertas():
    Button(id="success-alert-btn", text="Sucesso").click()
    alert_success = Text(class_="pg-alert pg-alert--success")
    assert "Sucesso" in alert_success.properties().get("text")

    Button(id="info-alert-btn", text="Info").click()
    alert_info = Text(class_="pg-alert pg-alert--info")
    assert "Info" in alert_info.properties().get("text")

    Button(id="error-alert-btn", text="Erro").click()
    alert_error = Text(class_="pg-alert pg-alert--danger")
    assert "Erro" in alert_error.properties().get("text")

    Button(id="toast-btn", text="Toast").click()
    toast = Text(class_="pg-toast show")
    assert "Toast" in toast.properties().get("text")

    navigate_next()


# ── DRAG AND DROP SECTION ──
def test_drag_and_drop():
    source_drag = UIElement(id="drag-source", draggable="true")
    target_drop = UIElement(id="drop-target")
    status = Text(id="dragdrop-status")

    assert "Nenhuma" in status.properties().get("text")
    source_drag.drag_to(target_drop)
    time.sleep(5)
    assert "Solto" in status.properties().get("text")

    navigate_next()


# ── FORMS SECTION ──
def test_formularios():
    dummy_file_path = os.path.abspath(os.path.join(base_dir, "dummy_upload.txt"))
    with open(dummy_file_path, "w") as f:
        f.write("This is a dummy text file to test file upload.")

    try:
        InputField(name="text-input").enter_text("Texto de teste")
        InputField(name="email-input").enter_text("teste@exemplo.com")
        InputField(name="password-input").enter_text("senha123")

        file_input = FileManager(name="file-input")
        file_input.upload_file(dummy_file_path)

        range_input = InputField(name="range-input")
        new_range_value = str(random.randint(1, 100))
        range_input.set_value(new_range_value)
        assert range_input.get_attribute("value") == new_range_value

        InputField(type="checkbox", name="c1").click()

        single_dropdown = Dropdown(name="dropdown")
        single_dropdown.scroll_to()
        single_dropdown.select_by_text("Opção 2")
        assert single_dropdown.get_selected_texts() == ["Opção 2"]

        Button(type="submit", text="Enviar").click()

    finally:
        if os.path.exists(dummy_file_path):
            os.remove(dummy_file_path)

    navigate_next()


@browser_session(MOCKUP_TEST_URL_FILE, maximize=True, headless=False)
def full_execution():
    select_full_mode()
    skip_intro()

    # Game section: skip by navigating to next
    navigate_next()

    # Card sections in order
    test_botoes()
    test_links()
    test_hover()
    test_tabs()
    test_modal()
    test_alertas()
    test_drag_and_drop()

    # Forms
    test_formularios()


if __name__ == "__main__":
    full_execution()
    print("Todos os testes do minima foram executados com sucesso!")
