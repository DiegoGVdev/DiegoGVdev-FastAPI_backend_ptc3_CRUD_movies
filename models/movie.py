from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Movie(Base):

    __tablename__= 'movies'

    movie_id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    year= Column(Integer)
    rating= Column(Float)
    category= Column(String)

    