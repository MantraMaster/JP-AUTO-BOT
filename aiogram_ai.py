import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.client import telegram
from aiogram.filters import CommandStart
import mistral

bot = Bot(token="8062628342:AAFd3CfTq8jORec1GFQM8hRcdXuXG2tI_oY")
dp = Dispatcher()



@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    if message.from_user.id not in mistral.history:
        id_user = message.from_user.id
        mistral.history[id_user] = [{"role": "system", "content": mistral.content_edu}]
        print(mistral.history)
    else:
        print("Уже существует", {message.from_user.id})
    await message.answer('Как к вам обращаться?')


@dp.message()
async def question(message: types.Message):
    # Проверка, является ли чат групповым
    if message.chat.type != "private":
        return  # Игнорировать сообщения в групповых чатах

    if message.from_user.id not in mistral.history:
        id_user = message.from_user.id
        mistral.history[id_user] = [{"role": "system", "content": mistral.content_edu}]
        print(mistral.history)
    print(message.from_user.username, "|", message.text)
    id_user = message.from_user.id
    try:
        print("Готовим ответ")
        response = mistral.get_chat_response(id_user, message.from_user.username, message.text)
        await bot.send_chat_action(chat_id=id_user, action="typing")
        await asyncio.sleep(2)
        await message.answer(response)

    except Exception as e:
        if mistral.index == len(mistral.api_keys):
            mistral.index == 0
        else:
            mistral.index += 1
            response = mistral.get_chat_response(id_user, message.from_user.username, message.text)
            await bot.send_chat_action(chat_id=id_user, action="typing")
            await asyncio.sleep(2)
            await message.answer(response)

    await bot.send_message(chat_id=-1002303909150,
                            text=f"<b>💬 Сообщение от пользователя {message.from_user.id, message.from_user.username}</b>"
                                 f": \n{message.text}", parse_mode="HTML")


async def main() -> None:
    await dp.start_polling(bot)

asyncio.run(main())

