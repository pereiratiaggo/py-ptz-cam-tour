# py-ptz-cam-tour

Este projeto é um controlador de câmera PTZ (Pan-Tilt-Zoom) escrito em Python. Ele permite automatizar movimentos de câmeras PTZ, facilitando a criação de tours automáticos, monitoramento e integração com outros sistemas.

## Funcionalidades
- Controle de movimentos Pan, Tilt e Zoom
- Automação de sequências de movimentos (tour)
- Interface simples via script Python
- Fácil integração e customização

## Estrutura do Projeto
- `Camera.py`: Classe principal para controle da câmera PTZ
- `main.py`: Script de exemplo para execução de um tour automatizado
- `requirements.txt`: Dependências do projeto

## Instalação
1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/py-ptz-cam-tour.git
   cd py-ptz-cam-tour
   ```
2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Uso
Copie o arquivo `.env.example` para `.env` e edite com as configurações necessárias da sua câmera PTZ:
```sh
cp .env.example .env
# Edite o arquivo .env conforme necessário
```
Depois, execute o projeto:
```sh
python main.py
```

## Requisitos
- Python 3.12+
- Dependências listadas em `requirements.txt`
