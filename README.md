<h1 align="center">RECICLA AÍ BACKEND</h1>
Repositório do backend do projeto Recicla Aí, uma plataforma dedicada a promover a reciclagem e a sustentabilidade ambiental.

# Preparando a Virtual Environment
Para garantir que todas as dependências do projeto sejam gerenciadas corretamente, é recomendado o uso de uma virtual environment. Siga os passos abaixo para configurar a sua:
1. **Criar a Virtual Environment**:
   ```bash
   python -m venv venv
   ```
   - Em algumas versões do linux é necessário atualizar a versão do venv, como no caso do python 3.12 no ubuntu 24.04:
   ```bash
   sudo apt install python3.12-venv -y
   ```
2. **Ativar a Virtual Environment**:
    - No Windows:
        ```bash
        venv\Scripts\activate
        ```
    - No macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
3. **Instalar as Dependências**:
    ```bash
    pip install -r requirements.txt
    ```
# Executando o Projeto
Para iniciar o servidor backend, execute o seguinte comando com a virtual environment ativada:
```bash
python main.py
```

# Requirements
As dependências do projeto estão listadas no arquivo `requirements.txt`. Certifique-se de instalar todas as dependências usando o comando mencionado acima.

## Como construir o arquivo requirements.txt
Para gerar o arquivo `requirements.txt` com as dependências atuais do seu ambiente virtual, utilize o seguinte comando:
```bash
pip freeze > requirements.txt
```

## Como instalar as dependências do requirements.txt
Para instalar todas as dependências listadas no arquivo `requirements.txt`, utilize o comando:
```bash
pip install -r requirements.txt
```