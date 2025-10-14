FROM python:3.12-slim

# working directory
WORKDIR /src

# instala as dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

# copia para o container
COPY . .

# port
EXPOSE 5000

# comando para rodar flask
CMD ["python", "main.py"]