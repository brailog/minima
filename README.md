# pyMinima

Minima focuses on the Readability and Token Economics Hypothesis.
Optimized interfaces for humans and LLMs, reducing automation costs and errors.

**Author:** Gabriel Ramos | Federal University of Pernambuco - CIn

## Research & Paper
This project is the practical implementation of the research paper:  
**"PyAutoTk: Bridging Usability and Flexibility in Web Automation Frameworks"**  
[Access at UFPE Repository](https://repositorio.ufpe.br/handle/123456789/66425)

### Abstract Summary
The research addresses the high entry barrier in web automation by proposing a framework that bridges the gap between usability and technical flexibility. Key findings include:
- **High-Level Abstractions:** Implementation of "Widgets" and "Session Decorators" to minimize boilerplate.
- **Semantic Density:** Reducing the cognitive load required to write and maintain automation scripts.
- **Educational Foundation:** Designed to help users focus on automation logic rather than driver intricacies.
- **Empirical Validation:** Demonstrating significant reductions in code complexity and token usage compared to raw Selenium.

---

## Installation

```bash
pip install pyminima
```
**PyPI:** [https://pypi.org/project/pyminima/](https://pypi.org/project/pyminima/)
**Docs:** [https://minima-br.readthedocs.io/pt-br/latest/](https://minima-br.readthedocs.io/pt-br/latest/)

---

## Why Minima?

Writing a Minima script is designed to feel like reading simple instructions. Instead of managing WebDrivers, explicit waits, and complex XPaths, you simply import the elements you need and interact with them.

### Token Economics and Readability Hypothesis: Minima vs. Selenium

Minima was intentionally designed as a “Human Read and Write” interface and eventually thought to also adapt to language models (LLMs). By abstracting verbose and structural code from raw browser automation (like Selenium). In the modern era of AI-assisted coding and autonomous agents, this translates directly into token generation savings: fewer tokens needed to represent logic lead to lower API costs, faster LLM generation times, reduced context window exhaustion, and higher human readability.

## Empirical Comparison

To test this hypothesis, we compared identical test suites executing the same business logic against raw Selenium WebDriver.


### Metrics

| Metric | Selenium Implementation | Minima Implementation | Savings / Reduction |
|--------|-------------------------|-----------------------|---------------------|
| Lines of Code (LOC) | 326 | 209 | **~36% reduction** |
| File Size (Bytes) | 11,591 bytes | 7,024 bytes | **~39% reduction** |
| Estimated LLM Tokens | ~2,900 tokens | ~1,750 tokens | **~39% reduction** |

Code example for table metrics: [Interactive Playground](https://minima-ui.com/playground?mode=cards&section=intro-section)

*Note: 1 token is roughly equivalent to 4 characters in standard English text and code.*

## Qualitative Analysis and Cost Implications

### 1. Semantic Density and Generation Cost
Compare the token requirements to click a button:

**Selenium WebDriver:**
```python
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='primary-btn' and contains(text(), 'Botão Primário')]"))
).click()
```

**Minima Framework:**
```python
Button(id="primary-btn", text="Botão Primário").click()
```
Minima's syntax focuses exclusively on intention and target, maximizing semantic density. For an LLM generating code, it skips predicting `WebDriverWait`, `expected_conditions`, `By.XPATH`, and complex string interpolations.

### 2. Context Window Efficiency
LLMs are constrained by their context windows. A roughly 40% reduction in code size means you can fit more test cases, application context, or prompt instructions in the same context window. For RAG (Retrieval-Augmented Generation) applications that feed code to LLMs, minima ensures the context is filled with meaningful business logic rather than automation boilerplate.

### 3. Lower Error Rate (Hallucination Mitigation)
Code designed to avoid LLM hallucination (e.g., forgetting parentheses, importing the wrong `By` or `EC` module, or messing up XPath syntax). Minima provides a strongly-typed, object-oriented API that restricts the LLM to simple, predictable patterns: `[Element]([Locators]).[Action]()`.

### 4. Human Readability and Maintenance
Code is read much more often than it is written. While LLMs are cheap to generate code, human developer time is expensive. The declarative nature of minima scripts reads almost like plain English. A QA engineer or Product Manager can easily audit a minima script to verify business rules, whereas reviewing raw Selenium scripts often requires deep technical context to separate signal from noise.

---

*Clean, semantic, and resilient UI automation. Built for the LLM era.*

### 5. License
Distributed under the [Apache 2.0](https://github.com/brailog/minima?tab=Apache-2.0-1-ov-file). See LICENSE for more information.