from mongo_data.Models.conversations import Conversation


def store_conversations(conversations, lines):
    for conv_no, conversation in enumerate(conversations):
        movie_id = conversation['movies_movie_id']
        conversation_lines = []
        for i, line_id in enumerate(conversation['line_list']):
            for line in lines:
                if line['line_id'] == line_id:
                    character_id = line['characters_character_id']
                    line_text = line['line_text']
                    break
            conversation_lines.append(
                {
                    'character_id': character_id,
                    'conversation_pos': i+1,
                    'line_text': line_text,
                }
            )
        conversation_obj = Conversation(movie_id=movie_id, conversation_lines=conversation_lines)
        conversation_obj.save()