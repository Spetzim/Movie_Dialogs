#from sql_data.Repository.character_repo import store_characters
#from sql_data.Repository.conversation_repo import store_conversations
#from sql_data.Repository.movie_repo import store_movies

from mongo_data.Repo.character_repo import store_characters
from mongo_data.Repo.conversation_repo import store_conversations
from mongo_data.Repo.movie_repo import store_movies



def extract_data_from_movie():
    with open('./raw_data/movie_titles_metadata.txt') as movie_data:
        lines = []
        for line in movie_data:
            line = line.strip()
            line_data = line.split(' +++$+++ ')
            line_dict = {
                'movie_id': line_data[0],
                'movie_title': line_data[1].title(),
                'movie_year': int(line_data[2]),
                'imdb_rating': float(line_data[3]),
                'imdb_votes': int(line_data[4]),
                'genres': line_data[5][1:-2].replace("'", "").split(', ')
            }

            lines.append(line_dict)

    store_movies(lines)

def extract_data_from_characters():
    with open('./raw_data/movie_characters_metadata.txt') as movie_data:
        lines = []
        for line in movie_data:
            line = line.strip()
            line_data = line.split(' +++$+++ ')
            line_dict = {
                'character_id': line_data[0],
                'character_name': line_data[1].title(),
                'gender': line_data[4],
                'movies_movie_id': line_data[2],
            }

            lines.append(line_dict)

    store_characters(lines)



def extract_data_from_conversations():
    with open('./raw_data/movie_conversations.txt', encoding='Latin-1') as conversation_file:
        conversation = []
        for conversation_line in conversation_file:
            conversation_line = conversation_line.strip()
            conversation_data = conversation_line.split(' +++$+++ ')
            conversation_dict = {
                'characters_character1_id': conversation_data[0],
                'characters_character2_id': conversation_data[1],
                'movies_movie_id': conversation_data[2],
                'line_list': conversation_data[3][1:-2].replace("'", "").split(', '),
            }
            conversation.append(conversation_dict)
    with open('./raw_data/movie_lines.txt', encoding='Latin-1') as lines_file:
        lines = []
        for line in lines_file:
            line = line.strip()
            line_data = line.split(' +++$+++ ')

            if len(line_data) == 5:
                line_text = line_data[4]
            else:
                line_text = "!"

            line_dict = {
                'line_id': line_data[0],
                'characters_character_id': line_data[1],
                'movies_movie_id': line_data[2],
                'line_text': line_text,
            }
            lines.append(line_dict)
    store_conversations(conversation, lines)



def main():
    extract_data_from_conversations()

if __name__ == '__main__':
    main()