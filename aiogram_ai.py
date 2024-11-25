import asyncio
from aiogram import Bot, Dispatcher, types
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
    await message.answer('Как к Вам обращаться?')

@dp.message()
async def question(message: types.Message):
    if message.from_user.id not in mistral.history:
        id_user = message.from_user.id
        mistral.history[id_user] = [{"role": "system", "content": mistral.content_edu}]
        print(mistral.history)
    print(message.from_user.username,"|", message.text)
    id_user = message.from_user.id
    mistral.question = message.text
    response = mistral.get_chat_response(id_user, message.from_user.username, message.text)
    await message.answer(response)

async def main() -> None:
    await dp.start_polling(bot)

asyncio.run(main())

