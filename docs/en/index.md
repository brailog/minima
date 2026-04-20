# Minima Documentation

Welcome to the official documentation for **Minima**!

Minima is a highly semantic, abstracted UI automation framework built on top of Selenium. It is designed around the philosophy that automation code should be intuitive, deeply readable, and optimized for both human developers and Large Language Models (LLMs).

## The Philosophy

By separating human inputs (keyboard and mouse) from the core browser engine, Minima allows developers to build robust scripts that are easy to read, maintain, and scale. Furthermore, Minima drastically cuts down on the structural boilerplate typical of Selenium scripts.

**"Human and LLM read and write"**
Because Minima uses a highly semantic syntax, it requires up to 40% fewer tokens to express complex logic compared to raw Selenium. This leads to cost-effective LLM script generation, faster AI inference, and drastically reduced cognitive load for human maintainers.

## Documentation Structure

```{toctree}
:maxdepth: 1
:hidden:

getting-started
api-reference
token-economics-hypothesis
```

- [**Getting Started**](getting-started.md): Installation, setup, and your first Minima script.
- [**API Reference**](api-reference.md): Detailed breakdowns of Minima's UI elements, inputs, and browser session decorators.
- [**Token Economics Hypothesis**](token-economics-hypothesis.md): Read the thesis on how Minima reduces LLM token overhead and maximizes readability.

## Project Architecture

Minima is built with a strict separation of concerns:

```text
minima/
├── engine/             # Selenium Core Logic & Context Management
│   ├── context.py      # Session management (@browser_session)
│   └── controller.py   # BrowserController
├── input/              # Input Simulation
│   ├── keyboard.py     # Keyboard mappings
│   └── mouse.py        # Mouse actions
├── ui/                 # Semantic UI Widget Layer
│   ├── ui_element.py   # Base element interaction
│   ├── button.py       # Button elements
│   ├── dropdown.py     # Select elements
│   └── ...             # Inputs, Texts, Links, Images
├── settings/           # Configuration
└── logs/               # Traceability and Logging
```

Dive into the [Getting Started](getting-started.md) guide to begin automating effortlessly!
