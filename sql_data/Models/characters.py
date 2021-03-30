
from sql_data.db import Base
import sqlalchemy as sa
from .movies import Movie

class Character(Base):
    __tablename__ = 'characters'

    character_id = sa.Column(sa.String(6), primary_key=True)
    character_name = sa.Column(sa.String(150), nullable=False)
    gender = sa.Column(sa.String(5))
    movies_movie_id = sa.Column(sa.String(5), sa.ForeignKey('movies.movie_id'), nullable=False)

    #conversations = relationship('Conversation')
    #movie_lines = relationship('Movie_line')

    def __repr__(self):
        return self.character_name
