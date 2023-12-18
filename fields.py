from langchain.chat_models.gigachat import GigaChat
from utils import prompt_user, extract_information

def fill_fields(fields: list, chat: GigaChat) -> dict:
    dialogue_context = {}
    for i, field in enumerate(fields):
        user_input = prompt_user(field)
        extracted_info = extract_information(field, user_input, fields, chat)
        dialogue_context[field] = extracted_info
    return dialogue_context