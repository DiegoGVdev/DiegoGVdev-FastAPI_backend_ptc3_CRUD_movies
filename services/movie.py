from config.database import Base, Session, engine
Base.metadata.create_all(bind=engine)


class MovieService:

    __db = Session()

    # def __init__(self, ) -> None:
        

    def get_movies(self, model):
        res = MovieService.__db.query(model).all()
        return res

    def get_movie(self, id, model):
        res = MovieService.__db.query(model).filter(model.movie_id == id).first()
        return res

    def get_category(self, category, model):
        res = MovieService.__db.query(model).filter(model.category == category).all()
        return res

    def create_movie(self, dict: dict, model):
        res = model(**dict)
        MovieService.__db.add(res)
        MovieService.__db.commit()
        return

    def update_movie(self, id, model, movie):
        res = MovieService.__db.query(model).filter(model.movie_id == id).first()
        if res:
            res.title = movie.title
            res.director = movie.director
            res.year = movie.year
            res.rating = movie.rating
            res.category = movie.category
            MovieService.__db.commit()
            return True

        else:
            return False

    def delete_movie(self, id, model):
        res = self.db.query(model).filter(model.movie_id == id).first()
        if res:
            MovieService.__db.delete(res)
            MovieService.__db.commit()
            return True
        else:
            return False