import os
import random
import time

from minima.engine.context import browser_session
from minima.ui.browser import Browser
from minima.ui.button import Button
from minima.ui.dropdown import Dropdown
from minima.ui.file_manager import FileManager
from minima.ui.input_field import InputField
from minima.ui.text import Text, Textlink
from minima.ui.ui_element import UIElement

base_dir = os.path.dirname(os.path.abspath(__file__))
MOCKUP_TEST_URL_FILE = "https://ui-playground.xyz/"


def start():
    botao_comecar = Button(id="start-btn", text="Começar")
    botao_comecar.click()


def test_botoes():
    Button(id="primary-btn", text="Botão Primário").click()
    mensagem_depois_click = Text(id="button-click-message").properties().get("text")
    assert "Botão Primário" in mensagem_depois_click

    Button(id="secondary-btn", text="Botão Secundário").click()
    mensagem_depois_click = Text(id="button-click-message").properties().get("text")
    assert "Botão Secundário" in mensagem_depois_click

    Button(id="danger-btn", text="Botão Perigo").click()
    mensagem_depois_click = Text(id="button-click-message").properties().get("text")
    assert "Botão Perigo" in mensagem_depois_click

    disabled_btn = Button(id="disabled-btn")
    assert disabled_btn.properties().get("enabled") is False

    Button(text="Próximo").click()


def test_links():
    Textlink(id="simple-link").click()
    Browser.accept_alert()

    Textlink(id="new-tab-link", text="Link em Nova Aba").click()
    Browser.accept_alert()
    Browser.switch_to_new_tab()
    Browser.close_current_tab()

    Textlink(id="download-link", text="Link de Download").click()
    time.sleep(0.5)
    Button(text="Próximo").click()


def test_formularios():
    dummy_file_path = os.path.abspath(os.path.join(base_dir, "dummy_upload.txt"))
    with open(dummy_file_path, "w") as f:
        f.write("This is a dummy text file to test file upload.")

    try:
        InputField(id="text-input").enter_text("Texto de teste")
        InputField(id="email-input").enter_text("teste@exemplo.com")
        InputField(id="password-input").enter_text("senha123")
        InputField(id="number-input").enter_text(str(random.randint(1, 100)))
        InputField(id="date-input", name="date-input").enter_text("11121999")

        color_input = InputField(id="color-input")
        new_color = "#EEFF00"
        color_input.set_value(new_color)
        retrieved_color = color_input.get_attribute("value")
        assert retrieved_color.lower() == new_color.lower()

        file_input = FileManager(id="file-input")
        file_input.upload_file(dummy_file_path)

        range_input = InputField(id="range-input")
        new_range_value = str(random.randint(1, 100))
        range_input.set_value(new_range_value)
        assert range_input.get_attribute("value") == new_range_value

        InputField(id="textarea-input", name="textarea-input").enter_text(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eget nisi quam."
        )

        # Checkboxes e Radios podem usar o InputField já que são tags <input>
        InputField(type="checkbox", value="opcao2").click()
        InputField(type="checkbox", value="opcao1").click()
        InputField(type="radio", value="opcao2").click()

        single_dropdown = Dropdown(id="dropdown")
        single_dropdown.scroll_to()
        single_dropdown.select_by_text("Opção 2")
        assert single_dropdown.get_selected_texts() == ["Opção 2"]

        multi_dropdown = Dropdown(id="multi-dropdown")
        multi_dropdown.select_by_text("Opção 1")
        multi_dropdown.select_by_index(2)
        assert sorted(multi_dropdown.get_selected_texts()) == ["Opção 1", "Opção 3"]
        multi_dropdown.deselect_by_text("Opção 1")
        assert multi_dropdown.get_selected_texts() == ["Opção 3"]

        Button(type="submit", id="submit-btn").click()

        form_data = Text(id="form-data").properties().get("text")
        assert "dummy_upload.txt" in form_data

    finally:
        if os.path.exists(dummy_file_path):
            os.remove(dummy_file_path)
    Button(text="Próximo").click()


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

    Button(text="Próximo").click()


def test_tabs():
    tab1_content = Text(id="tab1")
    assert "primeira" in tab1_content.properties().get("text")

    UIElement(data_tab="tab2").click()
    tab2_content = Text(id="tab2")
    assert "segunda" in tab2_content.properties().get("text")

    UIElement(data_tab="tab3").click()
    tab3_content = Text(id="tab3")
    assert "terceira" in tab3_content.properties().get("text")

    Button(text="Próximo").click()


def test_modal():
    Button(id="open-modal-btn", text="Abrir Modal").click()
    modal = UIElement(class_="modal", id="test-modal")

    assert "modal simples que pode ser" in modal.properties().get("text")
    assert modal.properties().get("displayed")

    close_btn = Button(class_="close")
    assert close_btn.properties().get("displayed")
    close_btn.click()

    Button(text="Próximo").click()


def test_alertas():
    Button(id="success-alert-btn").click()
    alert_success = Text(class_="alert alert-success")
    assert "Sucesso!" in alert_success.properties().get("text")

    Button(id="warning-alert-btn").click()
    alert_warning = Text(class_="alert alert-warning")
    assert "Aviso!" in alert_warning.properties().get("text")

    Button(id="info-alert-btn").click()
    alert_info = Text(class_="alert alert-info")
    assert "Informação!" in alert_info.properties().get("text")

    Button(id="error-alert-btn").click()
    alert_error = Text(class_="alert alert-danger")
    assert "Erro!" in alert_error.properties().get("text")

    Button(id="toast-btn").click()
    toast_alert = Text(id="toast", class_="toast show-toast")
    assert "toast!" in toast_alert.properties().get("text")

    Button(text="Próximo").click()


def test_drag_and_drop():
    source_drag = UIElement(id="drag-source", draggable="true")
    target_drop = UIElement(id="drop-target")
    status = Text(id="dragdrop-status")

    assert "Nenhuma" in status.properties().get("text")
    source_drag.drag_to(target_drop)
    time.sleep(5)
    assert "solto" in status.properties().get("text")


@browser_session(MOCKUP_TEST_URL_FILE, browser_type="Firefox")
def full_execution():
    start()
    test_botoes()
    test_links()
    test_formularios()
    test_hover()
    test_tabs()
    test_modal()
    test_alertas()
    test_drag_and_drop()


if __name__ == "__main__":
    full_execution()
    print("Todos os testes do minima foram executados com sucesso!")
