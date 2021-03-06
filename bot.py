# ยฉyoutubeslgeekshow me 

import os
import pyrogram
from pyrogram import Client, filters
from youtubesearchpython import VideosSearch
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
import YoutubeTags
from YoutubeTags import videotags

JOIN_ASAP = " **You cant use me untill subscribe our updates channel** โน๏ธ\n\n So Please join our updates channel by the following button and hit on the ` /start ` button again ๐"

FSUBB = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Join our update Channel ๐ฃ", url=f"https://t.me/sl_bot_zone") 
        ]]      
    )

SEARCH_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐บ๐ ๐ฉ๐๐ ๐๐๐๐ โ๏ธ", url=f"https://t.me/SL_bot_zone"),
                    InlineKeyboardButton("๐ข๐ ๐๐ธ๐ฝ ๐๐ฑ๐ช๐ฝ", url=f"https://t.me/slbotzone"),
                ],
                [
                    InlineKeyboardButton(text="Search Inline๐ ", switch_inline_query_current_chat="")],
            ]
        )

text = "๐ Hello There,\n\n **I'm Youtube Bot**.\n\n๐บFeatures\n๐Inline youtube search.\n๐Youtube Tag   Extractor.\n\nโจ Pแปwแบนrแบนษ ฦy : @SL_bot_zone\n\nโฎโโโโโโโโโโโโโโโโฎ\n\n๐ ๐ณ๐๐๐๐๐๐๐๐ : @supunmabot\n\nโฎโโโโโโโโโโโโโโโโฎ"

BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐บ๐ ๐ฉ๐๐ ๐๐๐๐ โ๏ธ", url=f"https://t.me/SL_bot_zone"),
                    InlineKeyboardButton("๐ข๐ ๐๐ธ๐ฝ ๐๐ฑ๐ช๐ฝ", url=f"https://t.me/slbotzone"),
                ],
                [
                    InlineKeyboardButton(text="๐ฆ Socure Code ๐ฆ", url=f"https://github.com/youtubeslgeekshow/Youtube-tag-bot")],
            ]
        )

slbotzone = Client(
    "@slbotzone", 
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]    
)
   
@slbotzone.on_message(filters.command(["start"]))
async def start(bot, message):
    try:
        await message._client.get_chat_member(int("-1001325914694"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
    )
        return       
    await message.reply_text(text=text,reply_markup=SEARCH_BUTTON)
   


@slbotzone.on_message(filters.regex("https://www.youtube.com") | filters.regex("http://www.youtube.com") | filters.regex("https://youtu.be/") | filters.regex("https://www.youtu.be/") | filters.regex("http://www.youtu.be/"))
async def tag(bot, message):
    link = str(message.text)
    tags = videotags(link) 
    if tags=="":
         await message.reply_text(" `๐๐จ ๐๐๐?๐ฌ ๐๐จ๐ฎ๐ง๐ ๐`")
    else:
         await message.reply_text(text=f"** ๐บ๐๐๐๐๐ ๐๐๐๐ ๐๐๐ ๐๐๐๐ ๐๐ ๐๐๐๐๐๐๐๐๐๐ ๐๐๐๐ ๐๐๐ ๐๐๐๐๐๐ ๐๐๐๐๐ **\n\n๐ฃ๐ฑ๐ฎ๐ผ๐ฎ ๐ช๐ป๐ฎ ๐ฝ๐ฑ๐ฎ ๐ฝ๐ช๐ฐ๐ผ ๐พ๐ผ๐ฎ๐ญ ๐ฏ๐ธ๐ป ๐ฝ๐ฑ๐ฎ ๐ฟ๐ฒ๐ญ๐ฎ๐ธ ๐๐ธ๐พ ๐ผ๐ฎ๐ท๐ฝ ๐ถ๐ฎ\n\n\n ` {tags} ` \n\n\n ๐ฅ Pแปwแบนrแบนษ ฦy : @SL_bot_zone\n\nโ๏ธ ๐ณ๐๐๐๐๐๐๐๐ : @supunmabot",reply_markup=BUTTON)
 

@slbotzone.on_inline_query()
async def search(client: Client, query: InlineQuery):
    answers = []
    search_query = query.query.lower().strip().rstrip()

    if search_query == "":
        await client.answer_inline_query(
            query.id,
            results=answers,
            switch_pm_text="Type video name here..",
            switch_pm_parameter="help",
            cache_time=0
        )
    else:
        videosSearch = VideosSearch(search_query, limit=50)

        for v in videosSearch.result()["result"]:
            answers.append(
                InlineQueryResultArticle(
                    title=v["title"],
                    description=" {} .".format(
                       v["viewCount"]["short"]
                    ),
                    input_message_content=InputTextMessageContent(
                        "https://www.youtube.com/watch?v={}".format(
                            v["id"]
                        )
                    ),
                    thumb_url=v["thumbnails"][0]["url"]
                )
            )

        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text="**Error: Search timed outโ**",
                switch_pm_parameter="",
            )

print(
    """
โโโณโโโโโโโโโโโโโโโโโโโ
โโโซโโณโโโโณโซโโณโโณโโโโโณโโซโโ
โฃโโโโซโโโซโโซโโซโปโซโโโโโโโโโซ
โโโปโโปโโโปโโโโปโโปโโโโโปโโปโโ
โโฎโฎโฎโฎ  I am supun  โฏโฏโฏโฏโ
โโฎโฎโฎโฎ  Join @sl_bot_zone โฏโฏโฏโฏโ
"""
)
slbotzone.run()

