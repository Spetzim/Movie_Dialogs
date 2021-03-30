import sqlalchemy

from sql_data.Models.conversations import MovieLine, ConversationLine
from sql_data.Models.movies import Movie, Genre
from sql_data.db import session, engine


def store_movies(lines):
    for line in lines:
        # del line['genres']
        line['genres'] = [Genre(genre_name=genre) for genre in line['genres']]
        movie = Movie(**line)
        session.add(movie)
    session.commit()


def get_movie_by_id(id):
    return session.query(Movie).filter(Movie.movie_id == id).first()


def fix_genres():
    # Hämta alla movie_genres
    con = engine.connect()
    sql = "SELECT * FROM movies_genres"
    result = con.execute(sql)

    # Loopa igenom varje rad från movie_genres
    for row in result:
        #   plocka ut movie_id
        movie_id = row[0]
        #   plocka ut genre_id
        genre_id = row[1]

        #   Hämta genre från genres där genre_id = genre_id
        genre = session.query(Genre).filter(Genre.genre_id == genre_id).first()
        #   Hämta first_genre från genres som har genre.genre_name
        first_genre = session.query(Genre).filter(Genre.genre_name == genre.genre_name).first()
        #   om genre_id != first_genre.genre_id
        if genre_id != first_genre.genre_id:
            #       uppdatera movies_genres med first_genre.genre_id
            try:
                sql = f"UPDATE movies_genres SET genres_movie_id={first_genre.genre_id} WHERE movies_movie_id='{movie_id}' AND genres_movie_id={genre_id}"
                con.execute(sql)
            except sqlalchemy.exc.IntegrityError as e:
                sql = f"DELETE FROM movies_genres WHERE movies_movie_id='{movie_id}' AND genres_movie_id={genre_id}"
                con.execute(sql)
                print("Duplicate")


def delete_duplicate_genres():
    con = engine.connect()
    sql = "SELECT DISTINCT genres_movie_id FROM movies_genres"
    genre_ids = [value[0] for value in con.execute(sql)]
    for genre in session.query(Genre).all():
        if genre.genre_id not in genre_ids:
            sql = f"DELETE FROM genre WHERE genre_id={genre.genre_id}"

