from pydantic import BaseModel,Field
from typing import Optional

class Movie(BaseModel):
    movie_id: Optional[int] = None
    title: str = Field(min_length=5, max_length=100)
    director: str = Field(min_length=5, max_length=50)
    year: int = Field(le=2023)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=15)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "my movie",
                    "director": "alguien la hizo",
                    "year": 2022,
                    "rating": 2.5,
                    "category": "animacion",
                }
            ]
        }
    }
