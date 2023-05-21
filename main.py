import openai
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


openai.api_key = "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"
telegram_api = "5849440191:AAHnZyoiY2HW8-3Fju6ygjrU-JBbO2Yis44"


if __name__ == '__main__':
    bot = Bot(token=telegram_api)
    dispatcher = Dispatcher(bot)

    @dispatcher.message_handler(commands=['start', 'help'])
    async def welcome(message: types.message):
        await message.reply("Hello! Im Test Resolv Bot", reply_markup=keyboard)


    @dispatcher.message_handler()
    async def echo(message: types.message):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message.text,
            temperature=0.9,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=["!Stop!"]
        )
        await message.answer(response['choices'][0]['text'])


    button_chat_bot = KeyboardButton("/lets_go")
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button_chat_bot)

    executor.start_polling(dispatcher)
