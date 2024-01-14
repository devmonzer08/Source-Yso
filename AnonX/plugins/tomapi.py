import asyncio
import os
from pyrogram.types import CallbackQuery
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    filters.command("help")
    
)
async def cr_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5f52312e9021cd9268077.jpg",
        caption=f"""**⩹━𓍹𓋹𓍻⊷━• ⌞ ⩹━⊷⌯ 𓏺𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐 •**\nمرحبا بك عزيزي {message.from_user.mention}\nانا بوت الذكاء الاصطناعي الخاص بسورس هانتر \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**⩹━𓍹𓋹𓍻⊷━⌞• ⌞ ⩹━⊷⌯ 𓏺𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐 •**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "طريقة الإستخدام", callback_data="usage"), 
                 ],[
                    InlineKeyboardButton(
                        "𓆩˹ 𝑺𝑨𝑺Ả✎", url=f"https://t.me/U_7h1"),
                   
                ],[
                
                    InlineKeyboardButton(
                        "𓍹𓋹𓍻• ⌞ ⩹━⊷⌯ 𓏺𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐 •⚡", url=f"https://t.me/huntersource"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("usage"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**⩹━𓍹𓋹𓍻⊷⌯⌞ 𓏺𝓼𝓸𝓾𝓻𝓬𝓮 𝓱𝓾𝓷𝓽𝓮𝓻⌝⌯⊶𓍹𓋹𓍻━⩺**
𓍹𓋹𓍻¦ اهلا بك عزيزي في قسم الأوامر
𓍹𓋹𓍻¦ لتتمكن من تشغيل الذكاء الاصطناعي الخاص بالوسكي فقط اكتب
𓍹𓋹𓍻¦ /gpt - لـلـسـؤال آي سـؤال بالـذكـاء الاسـطـناعي

**⩹━𓍹𓋹𓍻⊷⌯⌞ 𓏺᥉𝓸𝓾𝓻𝓬𝓮 𝓱𝓾𝓷𝓽𝓮𝓮𝓻⌝⌯⊶𓍹𓋹𓍻━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العودة", callback_data="back"), 
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def cr_back(_, callback_query: CallbackQuery):
    message = callback_query.message
  
    await message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("طريقة الإستخدام", callback_data="دليل")],
            [InlineKeyboardButton("𓆩˹𝑺𝑨𝑺Ả✎", url=f"https://t.me/U_7h1")],
            [InlineKeyboardButton("𓍹𓋹𓍻• ⌞ ⩹━⊷⌯ 𓏺𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐 •⚡", url=f"https://t.me/huntersource")],
        ]
    ))

