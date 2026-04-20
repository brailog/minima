# Referência da API

O Minima fornece uma API rica e semântica para interagir com o navegador de forma perfeita.

## Motor Principal (Core Engine)

### `@browser_session`
Um decorador que automatiza a configuração, o contexto de execução e o encerramento de uma sessão de navegador.

```python
from minima.engine.context import browser_session

@browser_session(
    url="https://exemplo.com",
    browser_type="chrome", # 'chrome' ou 'firefox'
    maximize=True,
    headless=False,
    kill_browser=True
)
def meu_script():
    pass
```

### `Browser`
Uma interface de alto nível para ações no nível do navegador.
- `Browser.accept_alert(timeout=5)`
- `Browser.switch_to_new_tab()`
- `Browser.switch_to_original_tab()`
- `Browser.close_current_tab()`

---

## Elementos de UI

Todos os elementos de UI herdam da classe base `UIElement`. Os elementos são localizados usando argumentos de palavras-chave que correspondem aos atributos HTML (ex: `id="btn"`, `class_="primary"`, `text="Enviar"`).

### Ações Base (`UIElement`)
Disponíveis em todos os widgets derivados (Button, Dropdown, Text, etc.):
- `.click(timeout=10)`
- `.double_click(delay=0.1, timeout=10)`
- `.hover(timeout=10)`
- `.unhover(timeout=10)`
- `.scroll_to(timeout=10)`
- `.drag_to(target_widget, timeout=10)`
- `.properties(timeout=10)` -> `dict`
- `.get_attribute(attribute_name, timeout=10)` -> `str`

### `Button`
Representa botões clicáveis `<button>` ou `<input type="submit">`.
```python
Button(id="enviar-btn", text="Enviar").click()
```

### `InputField`
Representa campos de entrada de texto, áreas de texto (textareas) e seletores de intervalo (range sliders).
- `.enter_text(text: str)`: Foca com segurança, limpa e insere o texto.
- `.set_value(value: str)`: Define o valor do elemento diretamente via JavaScript (útil para campos ocultos ou sliders).
```python
InputField(id="usuario").enter_text("admin")
```

### `Dropdown`
Representa elementos `<select>`.
- `.select_by_text(text: str)`
- `.select_by_value(value: str)`
- `.select_by_index(index: int)`
- `.deselect_all()`
- `.deselect_by_text(text: str)`
- `.get_selected_texts()` -> `list[str]`
```python
Dropdown(id="selecao-pais").select_by_text("Brasil")
```

### `FileManager`
Representa `<input type="file">`.
- `.upload_file(file_path: str)`: Requer um caminho de arquivo absoluto.
```python
FileManager(id="upload").upload_file("/caminho/absoluto/para/arquivo.txt")
```

### `Text` e `Textlink`
Representa elementos de texto somente leitura (`<span>`, `<p>`, `<h1>`) e links (`<a>`).
```python
mensagem = Text(id="msg-status").properties().get("text")
Textlink(id="link-home").click()
```

### `Image`
Representa tags `<img>`. Use as ações base para interagir ou extrair o `src`.
```python
img_src = Image(id="logo").get_attribute("src")
```

---

## Entrada Avançada

Para interações complexas semelhantes às humanas, o Minima expõe controladores diretos.

### `KeyboardController`
Permite a emissão de teclas de baixo nível.
```python
from minima.engine.context import current_session
from minima.input.keyboard import KeyboardController

kb = KeyboardController(current_session.get().driver)
kb.press_enter()
kb.press_escape()
```

### `Mouse`
Controla interações de mouse de baixo nível usando ActionChains do Selenium.
```python
from minima.engine.context import current_session
from minima.input.mouse import Mouse

mouse = Mouse(current_session.get().driver)
# Mapeamento de ações avançadas do mouse.
```
