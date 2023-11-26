from fastapi import APIRouter, status, Depends, Query, Body, Path
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List, Annotated
from schemas.movie_schemas import Movie
from middlewares.jwt_bearer import JWTBearer
from models.movie import Movie as MovieModel
from services.movie import MovieService


movie_router = APIRouter()


@movie_router.get(
    "/movies",
    tags=["movies"],
    response_model=List[Movie],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
)
def get_movies() -> List[Movie]:
    res = MovieService().get_movies(MovieModel)
    return JSONResponse(content=jsonable_encoder(res))


@movie_router.get(
    "/movies/{movie_id}",
    tags=["movies"],
    response_model=Movie,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
)
def get_movie(
    movie_id: Annotated[int, Path(title="pelicula buscada", ge=1, le=2000)]
) -> Movie:
    res = MovieService().get_movie(movie_id, MovieModel)
    if not res:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Pelicula no encontrada"},
        )
    return JSONResponse(content=jsonable_encoder(res))


@movie_router.get(
    "/movies/",
    tags=["movies"],
    response_model=List[Movie],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
)
def filter_category(
    category: Annotated[str, Query(min_length=5, max_length=15)]
) -> List[Movie]:
    res = MovieService().get_category(category, MovieModel)
    return JSONResponse(content=jsonable_encoder(res))


@movie_router.post(
    "/movie/",
    tags=["movies"],
    response_model=dict,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(JWTBearer())],
)
def create_movie(movie: Annotated[Movie, Body()]) -> dict:
    try:
        MovieService().create_movie(movie.dict(), MovieModel)
        return JSONResponse(content={"message": "la pelicula fue agregada"})
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": f"pelicula no creada, error: {str(e)}"},
        )


@movie_router.put(
    "/movies/{movie_id}",
    tags=["movies"],
    response_model=dict,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(JWTBearer())],
)
def update_movie(
    movie_id: int,
    movie: Annotated[Movie, Body()],
) -> dict:
    res = MovieService().update_movie(movie_id, MovieModel, movie)
    if res:
        return JSONResponse(content={"message": "la pelicula fue editada"})
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Pelicula no encontrada"},
        )


@movie_router.delete(
    "/movies/{movie_id",
    tags=["movies"],
    status_code=status.HTTP_200_OK,
    response_model=dict,
    dependencies=[Depends(JWTBearer())],
)
def delete_movie(movie_id: int) -> dict:
    res = MovieService().delete_movie(movie_id, MovieModel)
    if res:
        return JSONResponse(content={"message": " la pelicula fue eliminada"})
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Pelicula no encontrada"},
        )
