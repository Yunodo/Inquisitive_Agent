from utils import extract_information
from langchain.chat_models.gigachat import GigaChat

def edit_information(dialogue_context: dict, edit_fields: set, chat: GigaChat, fields : set) -> dict:
    """Edit the filled information by prompting the user for each field."""
    for field in edit_fields:
        field = field.lower()
        if field not in fields:
            print(f"Ошибка: поле '{field}' не является допустимым.")
            # Offer another chance and re-prompt for field name
            while field not in fields:
                print("Пожалуйста, укажите верное имя поля:")
                field = input().lower()
        print(f"Пожалуйста, предоставьте новое значение для {field}:")
        user_input = input()
        extracted_info = extract_information(field, user_input, dialogue_context.get(field, ""), chat)
        dialogue_context[field] = extracted_info
    return dialogue_context