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
    command("الاوامر")
)
async def هانتر_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/efa394c06f92186cd5277.jpg",
        caption=f"""**⩹━𓍹𓋹𓍻⊷━⌞𝑺𝑶𝑼𝑹𝑪𝑬 𝐘𝐒𝐎 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺ ⌝━⊶𓍹𓋹𓍻━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\nهذا قسم الاوامر الخاص بسورس هانتر \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**⩹━𓍹𓋹𓍻⊷━⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝐘𝐒𝐎 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺⌝━⊶𓍹𓋹𓍻━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر الجروبات", callback_data="gr"),
                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data="ch"),  
                 ],[
                    InlineKeyboardButton(
                        "اوامر الادمن", callback_data="adm"), 
                ],[
                
                    InlineKeyboardButton(
                        "𓍹𓋹𓍻⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝐘𝐒𝐎 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺ ⌝⚡", url=f"https://t.me/P_PP_Pi"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("gr"))
async def هانتر_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**⌯⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝐘𝐒𝐎 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺⌝⌯⊶𓍹𓋹𓍻━⩺**
𓍹𓋹𓍻¦ اهلا بك عزيزي في قسم اوامر التشغيل في الجروبات
𓍹𓋹𓍻¦ تشغيل + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ فديو + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ #فيديو + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ #فديو + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ {NAME_BOT} + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ /فيديو + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ /ق شغل + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ /تشغيل + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ cvplay + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ cplay + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ /vplay + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ /play + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ #تشغيل + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ فيديو + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ سورة + اسم السورة 
𓍹𓋹𓍻¦ cvplayforce + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ cplayforce + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ vplayforce + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ playforce + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ /cvplay + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ vplay + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ play + اسم الاغنيه/السوره

**⌯⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝐘𝐒𝐎 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺⌝⌯⊶𓍹𓋹𓍻━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="ch"), 
                    
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("ch"))
async def هانتر_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**⌯𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝐘𝐒𝐎 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺⌝⌯⊶𓍹𓋹𓍻━⩺**
𓍹𓋹𓍻¦ اهلا بك عزيزي في قسم اوامر التشغيل في القنوات
𓍹𓋹𓍻¦ شغل + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ قناه + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ مانو + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ ق + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ اغاني + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ . + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ / + اسم الاغنيه/السوره
**⩹⌯⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝐘𝐒𝐎 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺⌝⌯⊶𓍹𓋹𓍻━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="adm"), 
                    InlineKeyboardButton(
                        "العودة", callback_data="gr"), 
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("adm"))
async def هانتر_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝐘𝐒𝐎 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺⌝⌯⊶𓍹𓋹𓍻━⩺**
𓍹𓋹𓍻¦ اهلا بك عزيزي في قسم اوامر تشغيل الادمن
𓍹𓋹𓍻¦ رفع ثانوي
𓍹𓋹𓍻¦ تنزيل ثانوي
𓍹𓋹𓍻¦ قائمة الثانويين
𓍹𓋹𓍻¦ رفع ادمن
𓍹𓋹𓍻¦ تنزيل ادمن
𓍹𓋹𓍻¦ قائمة الادمن
𓍹𓋹𓍻¦ حظر
𓍹𓋹𓍻¦ الغاء الحظر
𓍹𓋹𓍻¦ المحظورين
𓍹𓋹𓍻¦ حظر عام
𓍹𓋹𓍻¦ الغاء الحظر العام
𓍹𓋹𓍻¦ المحظورين عام
𓍹𓋹𓍻¦ اونلاين
𓍹𓋹𓍻¦ اذاعه
𓍹𓋹𓍻¦ تحديث
𓍹𓋹𓍻¦ logger
𓍹𓋹𓍻¦ ريلود
𓍹𓋹𓍻¦ وقف
𓍹𓋹𓍻¦ كمل
𓍹𓋹𓍻¦ اسكت
𓍹𓋹𓍻¦ اتكلم
𓍹𓋹𓍻¦ ايقاف
𓍹𓋹𓍻¦ تخطي
𓍹𓋹𓍻¦ @all
𓍹𓋹𓍻¦ all stop
𓍹𓋹𓍻¦ يوتيوب / تنزيل
𓍹𓋹𓍻¦ playing
𓍹𓋹𓍻¦ القائمه
𓍹𓋹𓍻¦ حذف القائمه
𓍹𓋹𓍻¦ تحديث
𓍹𓋹𓍻¦ الاحصائيات
𓍹𓋹𓍻¦ لايف
𓍹𓋹𓍻¦ مساعده
𓍹𓋹𓍻¦ الاعدادت
𓍹𓋹𓍻¦ بينج

**⩹━𓍹𓋹𓍻⊷⌯⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝐘𝐒𝐎 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺ ⌝⌯⊶𓍹𓋹𓍻━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="gr"), 
                    InlineKeyboardButton(
                        "العودة", callback_data="ch"), 
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def هانتر_back(_, callback_query: CallbackQuery):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/efa394c06f92186cd5277.jpg",
        caption=f"""**⩹━𓍹𓋹𓍻⊷━⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝐘𝐒𝐎 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺ ⌝━⊶𓍹𓋹𓍻━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\nهذا قسم الاوامر الخاص بسورس هانتر \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**⩹━𓍹𓋹𓍻⊷━⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝐘𝐒𝐎 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺ ⌝━⊶𓍹𓋹𓍻━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر الجروبات", callback_data="gr"),
                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data="ch"),  
                 ],[
                    InlineKeyboardButton(
                        "اوامر الادمن", callback_data="adm"), 
                ],[
                
                    InlineKeyboardButton(
                        "𓍹𓋹𓍻⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝐘𝐒𝐎 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺⌝⚡", url=f"https://t.me/P_PP_Pi"),
                ],

            ]

        ),

    )

