from typing import List

from pydantic import BaseModel
import datetime


class Genre(BaseModel):
    name: str


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: datetime.date
    summary: str
    genres: List[Genre]
    pages: int
