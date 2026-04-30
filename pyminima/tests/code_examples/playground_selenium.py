import os
import random
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

base_dir = os.path.dirname(os.path.abspath(__file__))
MOCKUP_TEST_URL_FILE = "http://localhost:5173/playground"


# ── NAVIGATION ──
def select_full_mode(driver):
    xpath = "//*[contains(text(), 'Jornada Completa')]"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    ).click()


def skip_intro(driver):
    xpath = "//*[contains(text(), 'Começar')]"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    ).click()


def navigate_next(driver):
    xpath = "//*[contains(text(), 'Próximo')]"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    ).click()


# ── BUTTONS SECTION ──
def test_botoes(driver):
    xpath_primary = "//*[@id='primary-btn' and contains(text(), 'Botão Primário')]"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_primary))
    ).click()
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "button-click-message"))
    )
    assert "Primário" in message_element.text

    xpath_secondary = "//*[@id='secondary-btn' and contains(text(), 'Botão Secundário')]"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_secondary))
    ).click()
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "button-click-message"))
    )
    assert "Secundário" in message_element.text

    xpath_danger = "//*[@id='danger-btn' and contains(text(), 'Botão Perigo')]"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_danger))
    ).click()
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "button-click-message"))
    )
    assert "Perigo" in message_element.text

    disabled_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "disabled-btn"))
    )
    assert not disabled_btn.is_enabled()

    navigate_next(driver)


# ── LINKS SECTION ──
def test_links(driver):
    original_window = driver.current_window_handle

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "simple-link"))
    ).click()
    WebDriverWait(driver, 5).until(EC.alert_is_present()).accept()

    xpath_new_tab = "//*[@id='new-tab-link' and contains(text(), 'Nova Aba')]"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_new_tab))
    ).click()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    new_tab_handle = [
        handle for handle in driver.window_handles if handle != original_window
    ][0]
    driver.switch_to.window(new_tab_handle)
    driver.close()
    driver.switch_to.window(original_window)

    xpath_download = "//*[@id='download-link' and contains(text(), 'Download')]"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_download))
    ).click()
    time.sleep(0.5)

    navigate_next(driver)


# ── HOVER SECTION ──
def test_hover(driver):
    hover_div = driver.find_element(By.ID, "hover-div")
    hover_status = driver.find_element(By.ID, "hover-status")
    body = driver.find_element(By.TAG_NAME, "body")

    assert "não está" in hover_status.text
    for _ in range(3):
        ActionChains(driver).move_to_element(hover_div).perform()
        assert "está sobre" in hover_status.text
        time.sleep(0.5)

        ActionChains(driver).move_to_element(body).perform()
        assert "não está" in hover_status.text

    navigate_next(driver)


# ── TABS SECTION ──
def test_tabs(driver):
    tab1_content = driver.find_element(By.ID, "tab1")
    assert "primeira" in tab1_content.text

    driver.find_element(By.XPATH, "//*[@data-tab='tab2']").click()
    tab2_content = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "tab2"))
    )
    assert "segunda" in tab2_content.text

    driver.find_element(By.XPATH, "//*[@data-tab='tab3']").click()
    tab3_content = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "tab3"))
    )
    assert "terceira" in tab3_content.text

    navigate_next(driver)


# ── MODAL SECTION ──
def test_modal(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "open-modal-btn"))
    ).click()

    modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "test-modal"))
    )

    assert "modal simples" in modal.text
    assert modal.is_displayed()

    close_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "modal-close-btn"))
    )
    assert close_btn.is_displayed()
    close_btn.click()

    navigate_next(driver)


# ── ALERTS SECTION ──
def test_alertas(driver):
    driver.find_element(By.ID, "success-alert-btn").click()
    alert_success = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".pg-alert.pg-alert--success")
        )
    )
    assert "Sucesso" in alert_success.text

    driver.find_element(By.ID, "info-alert-btn").click()
    alert_info = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".pg-alert.pg-alert--info")
        )
    )
    assert "Info" in alert_info.text

    driver.find_element(By.ID, "error-alert-btn").click()
    alert_error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".pg-alert.pg-alert--danger")
        )
    )
    assert "Erro" in alert_error.text

    driver.find_element(By.ID, "toast-btn").click()
    toast = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".pg-toast.show")
        )
    )
    assert "Toast" in toast.text

    navigate_next(driver)


# ── DRAG AND DROP SECTION ──
def test_drag_and_drop(driver):
    source_drag = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "drag-source"))
    )
    target_drop = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "drop-target"))
    )
    status = driver.find_element(By.ID, "dragdrop-status")

    assert "Nenhuma" in status.text
    ActionChains(driver).drag_and_drop(source_drag, target_drop).perform()
    time.sleep(5)
    assert "Solto" in status.text

    navigate_next(driver)


# ── FORMS SECTION ──
def test_formularios(driver):
    dummy_file_path = os.path.abspath(os.path.join(base_dir, "dummy_upload.txt"))
    with open(dummy_file_path, "w") as f:
        f.write("This is a dummy text file to test file upload.")

    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "text-input"))
        ).send_keys("Texto de teste")

        driver.find_element(By.NAME, "email-input").send_keys("teste@exemplo.com")
        driver.find_element(By.NAME, "password-input").send_keys("senha123")

        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "file-input"))
        )
        file_input.send_keys(dummy_file_path)

        range_input = driver.find_element(By.NAME, "range-input")
        new_range_value = str(random.randint(1, 100))
        driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));",
            range_input,
            new_range_value,
        )
        assert range_input.get_attribute("value") == new_range_value

        driver.find_element(By.XPATH, "//*[@type='checkbox' and @name='c1']").click()

        dropdown_el = driver.find_element(By.NAME, "dropdown")
        ActionChains(driver).scroll_to_element(dropdown_el).perform()
        single_select = Select(dropdown_el)
        single_select.select_by_visible_text("Opção 2")
        assert [opt.text for opt in single_select.all_selected_options] == ["Opção 2"]

        driver.find_element(
            By.XPATH, "//*[@type='submit' and contains(text(), 'Enviar')]"
        ).click()

    finally:
        if os.path.exists(dummy_file_path):
            os.remove(dummy_file_path)

    navigate_next(driver)


def full_execution():
    driver = webdriver.Chrome()
    try:
        driver.maximize_window()
        driver.get(MOCKUP_TEST_URL_FILE)

        select_full_mode(driver)
        skip_intro(driver)

        # Game section: skip
        navigate_next(driver)

        # Card sections in order
        test_botoes(driver)
        test_links(driver)
        test_hover(driver)
        test_tabs(driver)
        test_modal(driver)
        test_alertas(driver)
        test_drag_and_drop(driver)

        # Forms
        test_formularios(driver)

    finally:
        driver.quit()


if __name__ == "__main__":
    full_execution()
    print("Todos os testes do Selenium foram executados com sucesso!")
