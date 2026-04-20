# Documentação Minima

Bem-vindo à documentação oficial do **Minima**!

O Minima é um framework de automação de UI altamente semântico e abstraído, construído sobre o Selenium. Ele foi projetado com a filosofia de que o código de automação deve ser intuitivo, profundamente legível e otimizado tanto para desenvolvedores humanos quanto para Grandes Modelos de Linguagem (LLMs).

## A Filosofia

Ao separar as entradas humanas (teclado e mouse) do motor principal do navegador, o Minima permite que os desenvolvedores criem scripts robustos que são fáceis de ler, manter e escalar. Além disso, o Minima reduz drasticamente o boilerplate estrutural típico dos scripts Selenium.

**"Leitura e escrita para Humanos e LLMs"**
Como o Minima utiliza uma sintaxe altamente semântica, ele requer até 40% menos tokens para expressar lógicas complexas em comparação com o Selenium puro. Isso resulta em uma geração de scripts por LLMs mais econômica, inferência de IA mais rápida e uma carga cognitiva drasticamente reduzida para mantenedores humanos.

## Estrutura da Documentação

```{toctree}
:maxdepth: 1
:hidden:

getting-started
api-reference
token-economics-hypothesis
```

- [**Primeiros Passos**](getting-started.md): Instalação, configuração e seu primeiro script Minima.
- [**Referência da API**](api-reference.md): Detalhamento dos elementos de UI, entradas e decoradores de sessão de navegador do Minima.
- [**Hipótese de Economia de Tokens**](token-economics-hypothesis.md): Leia a tese sobre como o Minima reduz o overhead de tokens de LLM e maximiza a legibilidade.

## Arquitetura do Projeto

O Minima é construído com uma separação rigorosa de preocupações:

```text
minima/
├── engine/             # Lógica Principal do Selenium e Gestão de Contexto
│   ├── context.py      # Gestão de sessão (@browser_session)
│   └── controller.py   # BrowserController
├── input/              # Simulação de Entrada
│   ├── keyboard.py     # Mapeamentos de teclado
│   └── mouse.py        # Ações de mouse
├── ui/                 # Camada de Widget de UI Semântica
│   ├── ui_element.py   # Interação base de elementos
│   ├── button.py       # Elementos de botão
│   ├── dropdown.py     # Elementos de seleção (select)
│   └── ...             # Inputs, Textos, Links, Imagens
├── settings/           # Configuração
└── logs/               # Rastreabilidade e Logs
```

Mergulhe no guia de [Primeiros Passos](getting-started.md) para começar a automatizar sem esforço!
