# API Reference

Minima provides a rich, semantic API to interact with the browser seamlessly.

## Core Engine

### `@browser_session`
A decorator that automates the setup, execution context, and teardown of a browser session.

```python
from minima.engine.context import browser_session

@browser_session(
    url="https://example.com",
    browser_type="chrome", # 'chrome' or 'firefox'
    maximize=True,
    headless=False,
    kill_browser=True
)
def my_script():
    pass
```

### `Browser`
A high-level interface for browser-level actions.
- `Browser.accept_alert(timeout=5)`
- `Browser.switch_to_new_tab()`
- `Browser.switch_to_original_tab()`
- `Browser.close_current_tab()`

---

## UI Elements

All UI elements inherit from the base `UIElement` class. Elements are located using keyword arguments that correspond to HTML attributes (e.g., `id="btn"`, `class_="primary"`, `text="Submit"`).

### Base Actions (`UIElement`)
Available on all derived widgets (Button, Dropdown, Text, etc.):
- `.click(timeout=10)`
- `.double_click(delay=0.1, timeout=10)`
- `.hover(timeout=10)`
- `.unhover(timeout=10)`
- `.scroll_to(timeout=10)`
- `.drag_to(target_widget, timeout=10)`
- `.properties(timeout=10)` -> `dict`
- `.get_attribute(attribute_name, timeout=10)` -> `str`

### `Button`
Represents clickable buttons `<button>` or `<input type="submit">`.
```python
Button(id="submit-btn", text="Submit").click()
```

### `InputField`
Represents text inputs, textareas, and range sliders.
- `.enter_text(text: str)`: Safely focuses, clears, and inputs text.
- `.set_value(value: str)`: Sets the element value directly via JavaScript (useful for hidden inputs or sliders).
```python
InputField(id="username").enter_text("admin")
```

### `Dropdown`
Represents `<select>` elements.
- `.select_by_text(text: str)`
- `.select_by_value(value: str)`
- `.select_by_index(index: int)`
- `.deselect_all()`
- `.deselect_by_text(text: str)`
- `.get_selected_texts()` -> `list[str]`
```python
Dropdown(id="country-select").select_by_text("Brazil")
```

### `FileManager`
Represents `<input type="file">`.
- `.upload_file(file_path: str)`: Requires an absolute file path.
```python
FileManager(id="upload").upload_file("/absolute/path/to/file.txt")
```

### `Text` and `Textlink`
Represents read-only text elements (`<span>`, `<p>`, `<h1>`) and links (`<a>`).
```python
message = Text(id="status-msg").properties().get("text")
Textlink(id="home-link").click()
```

### `Image`
Represents `<img>` tags. Use base actions to interact or extract `src`.
```python
img_src = Image(id="logo").get_attribute("src")
```

---

## Advanced Input

For complex human-like interactions, Minima exposes direct controllers.

### `KeyboardController`
Allows for low-level keystroke emission.
```python
from minima.engine.context import current_session
from minima.input.keyboard import KeyboardController

kb = KeyboardController(current_session.get().driver)
kb.press_enter()
kb.press_escape()
```

### `Mouse`
Controls low-level mouse interactions using Selenium's ActionChains.
```python
from minima.engine.context import current_session
from minima.input.mouse import Mouse

mouse = Mouse(current_session.get().driver)
# Advanced mouse actions mapping.
```
