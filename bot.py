from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, WebAppData
from aiogram.filters import CommandStart
import asyncio
from server import Data


bot = Bot(token='7388243533:AAEMH7wpms_kGeESPP217LWqE3txFu1qfQQ')
dp = Dispatcher()
data = Data()


@dp.message()
async def address_check(message: Message):
    
    refer = message.text[7:] # refer
    if refer != '' and refer != None and refer != False and refer != message.from_user.id:
        data.reg(message.from_user.id, refer)
        await bot.send_message(refer, 'You have new referal! ⭐️\n\nYou will get 10% of his income!')
    else:
        data.reg(message.from_user.id, 0)

    referServer = data.return_refer(message.from_user.id)
    
    personal_url = f'https://tonleague.ru/{message.from_user.id}_{referServer}'
    print(personal_url)
    markup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Play Now 💸', web_app=WebAppInfo(url=personal_url))],
    [InlineKeyboardButton(text='Join community', url='https://t.me/thetonleague')]
])

    await message.answer('Welcome to the TON League!\n\nStart to earn TON now!', reply_markup=markup)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())