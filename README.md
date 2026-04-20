## Overview

Minima is built on the philosophy that automation should be as intuitive as manual interaction. By separating human inputs (keyboard and mouse) from the core browser engine, Minima allows developers to build robust scripts that are easy to read, maintain, and scale.

## 📚 Documentation

For complete usage instructions and API references, check out our newly added docs:
- [Introduction & Philosophy](docs/index.md)
- [Getting Started](docs/getting-started.md)
- [API Reference](docs/api-reference.md)
- [Token Economics & Readability Hypothesis](docs/token-economics-hypothesis.md)

## Project Structure

The repository is organized to ensure a strict separation of concerns and responsibility based on the follow diagram:


```text
.
├── engine/             # Selenium Dependencia & Core Logic
│   ├── context.py      # BrowserSession & Decorators
│   └── controller.py   # BrowserController (URL Nav, Element Search)
├── input/              # Input Controller (Human Actions)
│   ├── keyboard.py     # Keyboard Mapping (Shortcuts, Enter, Fn keys)
│   └── mouse.py        # Mouse Actions (Click, Hover, Drag n Drop)
├── ui/                 # Widget Layer
│   └── base.py         # Base Widget & WidgetDecompose classes
├── settings/           # Configuration & Resources
│   ├── settings.py     # Binary PATHs & OS Configs
│   └── exceptions.py   # Custom Minima Exceptions
├── logs/               # Traceability
│   └── logger_utils.py # Logging utilities
└── tests/              # Validation
    ├── code-examples/  # Playground scripts
    └── unit_tests.py   # System verification

```

## 🛠️ Getting Started

### Prerequisites

* **Python 3.10+**

### Installation

Minima uses Poetry to ensure environment stability. To get started, clone the repository and install the dependencies:

```bash
git clone https://github.com/your-username/minima.git
cd minima

```

## ⚖️ License

Distributed under the **MIT License**. See `LICENSE` for more information.
