from fastapi import FastAPI, HTTPException

app = FastAPI()

BOOK_DATABASE = [
    "Harry Potter and the Chamber of Secrets",
    "Lord of the Rings",
    "The da Vinci Code"
]


# /    -> Rota de boas vindas
@app.get("/")
async def home():
    return "Welcome to my bookstore"


# /list-books -> listar todos os livros
@app.get("/list-books")
async def list_books():
    return { "books": BOOK_DATABASE}


# /list_book_by_index/{index} -  listar 1 livro em especifico
@app.get("/list-book-by-index/{index}")
async def list_book_by_index(index: int):
    if index < 0 or index >= len(BOOK_DATABASE):
        #erro
        raise HTTPException(404, "Index out of range")
    else:
        return { "books": BOOK_DATABASE[index]}

# /get-random-book -> livro aleatório

# /add-book -> adicionar novo livro