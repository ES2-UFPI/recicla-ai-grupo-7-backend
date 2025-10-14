FROM python:3.12-slim

# working directory
WORKDIR /app

# Instala wget e sqlc
RUN apt-get update && apt-get install -y wget \
    && wget https://downloads.sqlc.dev/sqlc_1.26.0_linux_amd64.tar.gz \
    && tar -xzf sqlc_1.26.0_linux_amd64.tar.gz \
    && mv sqlc /usr/local/bin/ \
    && rm sqlc_1.26.0_linux_amd64.tar.gz \
    && chmod +x /usr/local/bin/sqlc \
    && rm -rf /var/lib/apt/lists/*

# instala as dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

# copia para o container
COPY . .

# Gera os arquivos sqlc
RUN sqlc generate

# port
EXPOSE 5000

# comando para rodar flask
CMD ["python", "main.py"]