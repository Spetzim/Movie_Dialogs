from data.Models.movies import Movie
from data.db import session


def store_movies(lines):
    for line in lines:
        del line['genres']
        movie = Movie(**line)
        session.add(movie)
    session.commit()