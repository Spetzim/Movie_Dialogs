from sql_data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


movies_genres = sa.Table('movies_genres', Base.metadata,
                        sa.Column('movies_movie_id', sa.String(5), sa.ForeignKey('movies.movie_id'), primary_key=True),
                        sa.Column('genres_movie_id', sa.Integer, sa.ForeignKey('genres.genre_id'), primary_key=True),
                        )


# class MovieGenre(Base):
#     __tablename__ = 'movie_genres'
#
#     movies_movie_id = sa.Column(sa.String(5), sa.ForeignKey('movies.movie_id'), primary_key=True)
#     genres_movie_id = sa.Column(sa.Integer, sa.ForeignKey('genres.genre_id'), primary_key=True)
#
#     genre = relationship('Genre', back_populates='movies')
#     movie = relationship('Movie', back_populates='genres')



class Movie(Base):
    __tablename__ = 'movies'

    movie_id = sa.Column(sa.String(5), primary_key=True)
    movie_title = sa.Column(sa.String(150), nullable=False)
    movie_year = sa.Column(sa.Integer, nullable=False)
    imdb_rating = sa.Column(sa.Float, nullable=False)
    imdb_votes = sa.Column(sa.Integer, nullable=False)

    genres = relationship('Genre', secondary=movies_genres)

    characters = relationship('Character')

    #conversations = relationship('Conversation')
    #movie_lines = relationship('Movie_line')

    def __repr__(self):
        return f'{self.movie_title} - {self.movie_year}'


class Genre(Base):
    __tablename__ = 'genres'

    genre_id = sa.Column(sa.Integer, primary_key=True)
    genre_name = sa.Column(sa.String(150), nullable=False)

    #movies = relationship('MovieGenre', back_populates='genre')

    def __repr__(self):
        return self.genre_name

