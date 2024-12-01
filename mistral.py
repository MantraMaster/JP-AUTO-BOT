from mistralai import Mistral
api_keys = ["xKNyPGWYa3Zjv2VmacEUkVKxBNbk0Qgv", "GfGaeHdkG7WsjTDWT9EQ2mbPdsvWSipN", "C7K6c3vXWijzJs3Qh3SpSwdGUnexnoKs", "jsqDjnIBRpEn9rXjqIGA9jaQtavQzKcw"]
path_context = 'context.txt'
index = 0


model = "mistral-large-latest"

with open(path_context, 'r', encoding='utf-8') as file:
    content_edu = file.read()


history = {}


def get_chat_response(id, user_name, question):
    api_key = api_keys[index]
    client = Mistral(api_key=api_key)
    # Добавляем вопрос пользователя в историю
    history[id].append({"role": "user", "content": question})
    # Формируем список сообщений для отправки в модель
    messages = history[id]
    # Отправляем запрос к модели
    response = client.chat.complete(
        model=model,
        messages=messages
    )
    agent_message = response.choices[0].message.content
    history[id].append({"role": "assistant", "content": agent_message})
    print(f"Кому - {user_name} |", agent_message)
    return agent_message


