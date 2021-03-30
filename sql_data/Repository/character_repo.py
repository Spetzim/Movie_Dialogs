from sql_data.Models.characters import Character
from sql_data.db import session


def store_characters(lines):
    for line in lines:
        line['gender'] = line['gender'] if line['gender'] != '?' else None
        character = Character(**line)
        session.add(character)
    session.commit()
