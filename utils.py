from langchain.schema import SystemMessage, HumanMessage
from langchain.chat_models.gigachat import GigaChat

def prompt_user(field: str) -> str:
    """Prompt the user for the given field."""
    print(f"Не могли бы вы предоставить свой {field}?")
    return input()

def extract_information(field: str, user_input: str, fields: list, chat : GigaChat) -> str:
    """Extract the relevant information from GigaChat response."""
    field_instruction = HumanMessage(
        content=f"Извлеки следующую информацию: {field} из данного предложения: '{user_input}. Верни только данную информацию и никакого лишнего текста. НЕ ВОЗВРАЩАЙ НАЗВАНИЕ ПОЛЯ {field}'"
    )
    system_message = SystemMessage(
        content=f"Ты ИИ ассистент. Твоя задача в диалоговом формате заполнить информацию из следующих полей: {', '.join(fields)}. Ты будешь задавать уточняющие вопросы у юзера, спрашивая у него данную информацию."
    )
    messages = [system_message, field_instruction]
    gigachat_response = chat(messages)
    return gigachat_response.content

def confirm_information(dialogue_context: dict) -> bool:
    """Confirm the filled information with the user."""
    confirmation_text = ", ".join(
        f"{field}: '{dialogue_context[field]}'" for field in dialogue_context
    )
    print(f"Подтвердим информацию. Это верно? {confirmation_text}")
    print("Если все верно, напишите «Да».")
    print("Чтобы изменить информацию, введите «Нет»")

    while True:
        user_input = input().lower()
        if user_input == "да":
            return True
        elif user_input == "нет":
            return False
        else:
            print("Пожалуйста, введите либо «Да», либо «Нет».")