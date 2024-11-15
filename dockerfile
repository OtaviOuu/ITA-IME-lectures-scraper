# Use a imagem oficial do Python a partir do Docker Hub
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo requirements.txt para dentro do container
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o resto do código da aplicação para dentro do container
COPY . .

# Definir o comando para rodar a aplicação
CMD ["python", "app.py"]
