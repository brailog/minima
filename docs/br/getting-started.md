# Primeiros Passos com o Minima

Este guia ajudará você a instalar o Minima e a escrever seu primeiro script de automação de UI econômico e altamente legível.

## Pré-requisitos

- **Python 3.10+**
- Recomendado: Uma ferramenta de ambiente virtual (como `venv` ou `poetry`)
- Navegadores instalados (Chrome ou Firefox)

## Instalação

O Minima pode ser instalado e configurado localmente no seu projeto.

```bash
git clone https://github.com/seu-usuario/minima.git
cd minima
pip install -r requirements.txt
# ou via poetry, se configurado
```

## Seu Primeiro Script Minima

Escrever um script Minima foi projetado para parecer com a leitura de instruções simples. Em vez de gerenciar WebDrivers, esperas explícitas e XPaths complexos, você simplesmente importa os elementos que precisa e interage com eles.

### Exemplo: Uma Submissão de Formulário Simples

Crie um arquivo chamado `ola_minima.py`:

```python
from minima.engine.context import browser_session
from minima.ui.input_field import InputField
from minima.ui.button import Button
from minima.ui.text import Text

# O decorador @browser_session lida automaticamente com a configuração do navegador,
# navegação e encerramento. Nenhum boilerplate necessário!
@browser_session(url="https://minima-ui.com/playground/", browser_type="chrome")
def executar_teste():
    # 1. Insira texto nos campos de entrada
    InputField(id="email-input").enter_text("ola@minima.dev")
    InputField(id="password-input").enter_text("supersecreto")
    
    # 2. Clique em um botão
    Button(id="submit-btn", text="Login").click()
    
    # 3. Verifique se o texto aparece
    mensagem_sucesso = Text(class_="alert alert-success").properties().get("text")
    assert "Success" in mensagem_sucesso
    
    print("Teste concluído com sucesso!")

if __name__ == "__main__":
    executar_teste()
```

### Executando o Script

Basta executar o seu arquivo python:

```bash
python ola_minima.py
```

O Minima lançará automaticamente o navegador, realizará as interações suavemente com esperas dinâmicas integradas e fechará a sessão.

## Próximos Passos

Agora que você escreveu seu primeiro script, confira a [Referência da API](api-reference.md) para explorar o conjunto completo de elementos de UI (Dropdowns, FileManagers, Alertas) e ações avançadas (Drag & Drop, Hover) disponíveis no Minima.
