# API Simples de Livraria com FastAPI

Este projeto implementa uma API RESTful básica para gerenciar um catálogo de livros, utilizando o framework web FastAPI em Python. O objetivo é demonstrar operações fundamentais de leitura (GET) e criação (POST) de dados, servindo como um ponto de partida para o desenvolvimento de APIs mais complexas.

Duas versões da API são fornecidas:
1.  **`main.py`**: Utiliza um modelo de dados `Pydantic` (`Book` class) para definir a estrutura dos livros, garantindo validação de dados, tipagem forte e serialização/deserialização automática.
2.  **`main-sem-classe.py`**: Uma versão mais simplificada que trata os livros como strings, ideal para entender os conceitos básicos do FastAPI sem a complexidade adicional de modelos de dados customizados.

Ambas as versões persistem os dados em um arquivo `books.json` simples.

## Funcionalidades da API

A API oferece as seguintes rotas:

* **`GET /`**: Retorna uma mensagem de boas-vindas.
* **`GET /list-books`**: Lista todos os livros disponíveis no catálogo.
* **`GET /list-book-by-index/{index}`**: Retorna um livro específico pelo seu índice na lista. Retorna erro 404 se o índice estiver fora do intervalo.
* **`GET /get-random-book`**: Retorna um livro aleatório do catálogo.
* **`POST /add-book`**: Adiciona um novo livro ao catálogo.

## Estrutura do Projeto

* `main.py`: Implementação da API utilizando `Pydantic` para modelos de dados.
* `main-sem-classe.py`: Implementação da API com tratamento de dados simplificado (livros como strings).
* `books.json`: Arquivo JSON para persistência dos dados dos livros.

## Tecnologias Utilizadas

* **Python 3**
* **FastAPI**: Framework web de alta performance para construir APIs.
* **Pydantic**: (Apenas em `main.py`) Para validação de dados e modelagem.
* **`uvicorn`**: Servidor ASGI para executar as aplicações FastAPI.


## Persistência de Dados

Ambas as versões da API salvam e carregam o catálogo de livros de um arquivo `books.json`. Isso significa que os livros adicionados persistem entre as reinicializações do servidor.
