import asyncio

import os
import time
import requests
from config import OWNER_ID, USER_OWNER
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين السورس","المطورين","مطورين","مطورين هانتر"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/efa394c06f92186cd5277.jpg",
        caption=f"""**⩹━𓍹𓋹𓍻⊷━⌞𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐 ⌝━⊶𓍹𓋹𓍻━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين هانتر ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━𓍹𓋹𓍻⊷━⌞𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐 ⌝━⊶𓍹𓋹𓍻━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓍹𓋹𓍻᚜⎖᳒𝑺𝑨𝑺𝑨 𖤐𓍹𓋹𓍻", url=f"https://t.me/U_7h1"), 
                 ],[
                    InlineKeyboardButton(
                        "𓍹𓋹𓍻᚜𝑴𝑨𝑵𝑫𝑶𝑶᚛𓍹𓋹𓍻", url=f"https://t.me/M_2A_E_S"),
                    InlineKeyboardButton(
                        "𓍹𓋹𓍻᚜™ ꪗꪮꪊડꫀꫀᠻ┋☬᚛𓍹𓋹𓍻", url=f"https://t.me/J3_oo"),
                ],[
                    InlineKeyboardButton(
                        "𓍹𓋹𓍻᚜𝒀𝑶𝑺𝑹᚛𓍹𓋹𓍻", url=f"https://t.me/Yosr3456"),
                ],[
                    InlineKeyboardButton(
                        "𓍹𓋹𓍻𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹  🦋", url=f"https://t.me/huntersource"),
                
        ],

            ]

        ),

    )








@app.on_message(
    command(["صاصا","مبرمج السورس","المبرمج","مبرمج"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("U_7h1")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━𓍹𓋹𓍻⊷━⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐 ⌝━⊶𓍹𓋹𓍻━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━𓍹𓋹𓍻⊷━⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐 ⌝━⊶𓍹𓋹𓍻━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["قناة السورس"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("huntersource")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━𓍹𓋹𓍻⊷━⌞ 𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐 ⌝━⊶𓍹𓋹𓍻━⩺\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━𓍹𓋹𓍻⊷━⌞ 𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐 ⌝━⊶𓍹𓋹𓍻━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["مطورك","ديشا","مطور السورس"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("U_7h1")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━𓍹𓋹𓍻⊷━⌞ 𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐 ⌝━⊶𓍹𓋹𓍻━⩺\n\n‍ ¦ᦔꫀꪜ :{name}مطوري\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━𓍹𓋹𓍻⊷━⌞ 𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐 ⌝━⊶𓍹𓋹𓍻━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    

@app.on_message(
    command(["المطور"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    
    usr = await client.get_chat(USER_OWNER)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**معلومات المطور الاساسي \n\n ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "مطور البوت", url=f"https://t.me/{usr.username}")
                ],   [
                    InlineKeyboardButton(
                        "قناة السورس", url=f"https://t.me/huntersource"),                        
                 ],
            ]
        ),
    )
    


@app.on_message(
    command(["ذكاء"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b2f471a99721d916ec8e9.jpg",
        caption=f"""**⩹⊷━⌞ 𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس هانتر\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞ 𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝑺𝑨𝑺Ả✎˹َّّ", url=f"https://t.me/U_7h1"), 
                 ],[
                
                    InlineKeyboardButton(
                        "𓍹𓋹𓍻⌞ 𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐 ⌝⚡", url=f"https://t.me/huntersource"),
                ],

            ]

        ),

    )



@app.on_message(
    command(["قرأن"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/2577f47589c4b4c63e4a6.jpg",
        caption=f"""**⩹⊷━⌞ 𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس هانتر\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**⩹━━⌞ 𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝑺𝑨𝑺Ả✎˹َّّ", url=f"https://t.me/U_7h1"), 
                 ],[
                
                    InlineKeyboardButton(
                        "𓍹𓋹𓍻⌞ 𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐 ⌝⚡", url=f"https://t.me/huntersource"),
                ],

            ]

        ),

    )



@app.on_message(
    command(["ماندو","بتاع الرمزيات","المطور ماندوا","مطور ماندو"])
    & filters.group
  
)
async def yas(client, message):
    usr = await client.get_chat("M_2A_E_S")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━𓍹𓋹𓍻⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹 🦋⌯⊶𓍹𓋹𓍻━⩺\n\n🧞‍♂️ ¦𝙺𝙸𝙽𝙶 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━𓍹𓋹𓍻⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹 🦋⌯⊶𓍹𓋹𓍻━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )

