# Imagem base com Python 3.11
FROM python:3.11

# Copia o arquivo requirements.txt para a imagem
COPY requirements.txt /

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r /requirements.txt

# Cria um diretório para o projeto e define-o como diretório de trabalho
WORKDIR /app

# Copia o código do projeto para o diretório /app
COPY . /app

# Expõe a porta 80, que é a porta padrão para o FastAPI
EXPOSE 80

# Inicia o servidor com o comando uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

# Cria um arquivo requirements.txt
# pip freeze > requirements.txt

# Builda a imagem
# docker build -t sorte-io .

# Roda o container
# docker run -p 80:80 sorte-io