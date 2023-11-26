from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers.movie import movie_router
from routers.user import user_router


from middlewares.error_handler import ErrorHandler


app = FastAPI()
app.title = "CRUD movies"
app.description = "this is a app about movies"
app.version = "0.0.1"
app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)


movies = [
    {
        "id": 1,
        "title": "The Godfather",
        "director": "Francis Ford Coppola",
        "year": 1972,
        "rating": 9.2,
        "category": "terror",
    },
    {
        "id": 2,
        "title": "The Godfather: Part II",
        "director": "Francis Ford Coppola",
        "year": 1974,
        "rating": 9.0,
        "category": "terror",
    },
    {
        "id": 3,
        "title": "The Dark Knight",
        "director": "Christopher Nolan",
        "year": 2008,
        "rating": 9.0,
        "category": "comedia",
    },
]


@app.get("/", tags=["home"])
def home():
    return HTMLResponse("<h1> esta es la muestra de una respuesta html </h1>")
