import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint
@app.on_message(
    command(["صورص","سورس","السورس","سورس ميكو", "ميكو"])
)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/0b6b1d4a1695489a543df.jpg",
        caption=f"""
  - 𓏺[𝑺𝑶𝑼𝑹𝑪𝑬 𝐘𝐒𝐎 𖤐](https://t.me/P_PP_Pi) 
—————————————
-   [𝙗𝙤𝙩 𝙘𝙝𝙖𝙩 ❤️](https://t.me/P_PP_Pich) 

-  [𝙨𝙤𝙪𝙧𝙘𝙚 𝙙𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧](https://t.me/I_RA6) 
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐘𝐒𝐎✎ ˹ ♡", url=f"https://t.me/I_RA6"), 
                ],[
                    InlineKeyboardButton(
                        "⩹━⊷⌯𝑺𝑶𝑼𝑹𝑪𝑬 𝐘𝐒𝐎 𖤐♡", url=f"t.me/P_PP_Pi"),
                ],

            ]

        ),

    )



@app.on_message(command(["غنيلي", "غني", "غ", "ميكو غنيلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(command(["صورة","صور"]))
async def ihd(client: Client, message: Message):
    rs = random.randint(39,148)
    url = f"https://t.me/GTTUTY/{rs}"
    await client.send_photo(message.chat.id,url,caption="💕 ¦ تـم اختيـار الصوره لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
