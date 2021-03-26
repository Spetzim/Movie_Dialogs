from data.Models.movies import Movie, Genre
from data.db import session


def store_movies(lines):
    for line in lines:
        #del line['genres']
        line['genres'] = [Genre(genre_name=genre) for genre in line['genres']]
        movie = Movie(**line)
        session.add(movie)
    session.commit()


def get_movie_by_id(id):
    return  session.query(Movie).filter(Movie.movie_id==id).first()