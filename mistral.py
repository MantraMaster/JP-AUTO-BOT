import os
from mistralai import Mistral

api_key = "xKNyPGWYa3Zjv2VmacEUkVKxBNbk0Qgv"
model = "mistral-large-latest"

client = Mistral(api_key=api_key)
content_edu = "Ты элитный менеджер по подбору/продажам автомобилей, веди себя как человек и распологай собеседника, используй тригерные вопросы для выявления потребностей, а после 3 вопросов попроси оставить контактный номер телефона, для уточнения деталей, но обязательно уточни в какое время удобно было бы связаться, используй деловой стиль в общении.  Наша компания занимается доставкой автомобилей преимущественно из Японии, но при желании мы можем пригнать любой автомобиль из других стран таких как Южная Корея или Китай. Они все высокого качества и дешевле в 2 раза, чем рыночная стоимость в России. Отвечай кратко, но будь любезен чтобы у вас завязался Диалог, не пиши больше 300 символов в одном предложении, и разговаривай всегда на Вы с большой буквы. "

history = {}

def get_chat_response(id, question):
    # Добавляем вопрос пользователя в историю
    if id not in history:
        history[id] = {"role": "user", "content": content_edu + " " + question}
    else:
        history[id]["content"] += question

    # Формируем список сообщений для отправки в модель
    print(history[id])
    #messages = [{"role": "user", "content": question}]

    # Отправляем запрос к модели
    response = client.chat.complete(
        model=model,
        messages=messages
    )

    agent_message = response.choices[0].message.content
    return agent_message


#response = get_chat_response(question)
#print(question)

