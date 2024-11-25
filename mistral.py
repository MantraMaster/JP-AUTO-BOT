import os
from mistralai import Mistral

path_context = 'context.txt'
api_key = "xKNyPGWYa3Zjv2VmacEUkVKxBNbk0Qgv"
model = "mistral-large-latest"

with open(path_context, 'r', encoding='utf-8') as file:
    content_edu = file.read()

client = Mistral(api_key=api_key)
history = {}


def get_chat_response(id, question):
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
    return agent_message



