import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app

import re
import sys
from os import getenv

from dotenv import load_dotenv



@app.on_message(
    command(["اصدار"])
  
)
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b325cc3e9ed4d1ffcc279.mp4",
        caption=f"""**⩹━𓍹𓋹𓍻⊷⌯⌞ 𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\n
𓍹𓋹𓍻᚜ اسم سورس:-هانتر
𓍹𓋹𓍻᚜ نوعه:-ميوزك
𓍹𓋹𓍻᚜ للغه برمجه:- بايثون
𓍹𓋹𓍻᚜ اللغه:-اللغه العربيه ويدعم الانجليزيه 
𓍹𓋹𓍻᚜ مجال تشغيل :- تشغيل بوتات الميوزك
𓍹𓋹𓍻᚜ نظام تشغيل:-cr بوت ميوزك
𓍹𓋹𓍻᚜ الاصدار 4.0.1 pyrogram 
𓍹𓋹𓍻᚜ تاريخ تاسيس:-21-3-2023
𓍹𓋹𓍻᚜ مأسس هانتر:- [𓆩˹ 【𝑺𝑨𝑺Ả✎】•༄►](https://t.me/U_7h1)

**⩹━𓍹𓋹𓍻⊷⌯𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺ ⌯⊶𓍹𓋹𓍻━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺ ⌝", url=f"https://t.me/huntersource"), 
                 ],[
                 InlineKeyboardButton(
                        "◁", callback_data="hpdtsnju"),
               ],
          ]
        ),
    )


