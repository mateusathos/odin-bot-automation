# CampaignBot

Automação desktop em Python com reconhecimento de imagens para fluxo repetitivo de interface (estudo de automação GUI, controle de janela e threading).
Vídeo demonstração: https://youtu.be/Q4aWFIms01Y

## Stack

- Python 3.10+
- PyAutoGUI
- PyDirectInput
- Tkinter
- psutil
- pywin32
- requests
- keyboard

## Estrutura deste repositório

- `main.py`: único arquivo Python versionado no GitHub (script principal da automação)
- `images/`: referências visuais usadas no reconhecimento de tela
- `requirements.txt`: dependências do projeto

## Como rodar

1. Crie e ative um ambiente virtual:
   - PowerShell:
     - `python -m venv .venv`
     - `.venv\Scripts\Activate.ps1`
2. Instale as dependências:
   - `pip install -r requirements.txt`
3. Execute:
   - `python main.py`

## Observações

- Projeto voltado para ambiente Windows.
- A automação depende de resolução/posição de janela e imagens de referência.
- Este repositório foi enxugado para portfólio e mantém apenas o `main.py` como código-fonte Python versionado.
- Não versione chaves, executáveis e artefatos de build (já cobertos no `.gitignore`).

## Portfólio

Este repositório demonstra:

- automação de interface com visão por template matching;
- integração com API para controle de acesso;
- manipulação de processo/janela no Windows;
- interface de controle em Tkinter com execução em thread.

