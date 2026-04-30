# Getting Started with Minima

This guide will help you install Minima and write your first cost-effective, highly-readable UI automation script.

## Prerequisites

- **Python 3.10+**
- Recommended: A virtual environment tool (like `venv` or `poetry`)
- Installed browsers (Chrome or Firefox)

## Installation

Minima can be installed and set up locally in your project.

```bash
git clone https://github.com/your-username/minima.git
cd minima
pip install -r requirements.txt
# or via poetry if configured
```

## Your First Minima Script

Writing a Minima script is designed to feel like reading plain instructions. Instead of managing WebDrivers, explicit waits, and complex XPaths, you simply import the elements you need and interact with them.

### Example: A Simple Form Submission

Create a file named `hello_minima.py`:

```python
from minima.engine.context import browser_session
from minima.ui.input_field import InputField
from minima.ui.button import Button
from minima.ui.text import Text

# The @browser_session decorator automatically handles browser setup,
# navigation, and teardown. No boilerplate required!
@browser_session(url="https://minima-ui.com/playground/", browser_type="chrome")
def run_test():
    # 1. Enter text into input fields
    InputField(id="email-input").enter_text("hello@minima.dev")
    InputField(id="password-input").enter_text("supersecret")
    
    # 2. Click a button
    Button(id="submit-btn", text="Login").click()
    
    # 3. Verify text appears
    success_message = Text(class_="alert alert-success").properties().get("text")
    assert "Success" in success_message
    
    print("Test completed successfully!")

if __name__ == "__main__":
    run_test()
```

### Running the Script

Simply run your python file:

```bash
python hello_minima.py
```

Minima will automatically launch the browser, perform the interactions smoothly with built-in dynamic waits, and close the session.

## Next Steps

Now that you've written your first script, check out the [API Reference](api-reference.md) to explore the full suite of UI elements (Dropdowns, FileManagers, Alerts) and advanced actions (Drag & Drop, Hover) available in Minima.
