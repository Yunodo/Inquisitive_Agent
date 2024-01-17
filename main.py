import logging
from utils import confirm_information
from dialogue import edit_information
from fields import fill_fields
from langchain.chat_models.gigachat import GigaChat
import os
from dotenv import load_dotenv

def main():
    logging.basicConfig(level=logging.INFO)

    # Set the fields to be filled
    fields = ["Имя", "Фамилия", "Гражданство"]
    fields = {field.lower() for field in fields}

    load_dotenv(".env")
    GIGACHAT_CREDENTIALS = os.environ.get("GIGACHAT_CREDENTIALS")

    chat = GigaChat(credentials=GIGACHAT_CREDENTIALS, verify_ssl_certs=False)

    # Fill the fields
    dialogue_context = fill_fields(fields, chat)


    # Confirm the filled information
    if not confirm_information(dialogue_context):
        # Get the fields to be edited
        edit_fields = list(map(str.strip, input("Укажите поле или поля для редактирования через запятую:").lower().split(",")))

        # Edit the filled information
        dialogue_context = edit_information(dialogue_context, edit_fields, chat, fields)

    print(f"Заполненная информация: {dialogue_context}")
    logging.info("Conversation finished.")


if __name__ == "__main__":
    main()