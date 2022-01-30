import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgQAAxkBAAEDsTZh4xBVu96tWo0G0CIbn_meSGs6LwACWxcAAqbxcR4yeTJRtPe4UCME")
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fc5af1769743caa2bd6f1.png",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━
🖤 ʜᴇʏ, ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs...
ᴀʟʟ ᴏꜰ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴏʀ : [ᔕåßᔕäᒪ](t.me/StopFollowMe)
┗━━━━━━━━━━━━━━━━━┛

💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](t.me/StopFollowMe) ʙᴀʙʏ...
━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😫ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ​😫", url="https://telegram.me/share/url?url=https://t.me/HaPpInEsS4Ev6")
                  ],[
                    InlineKeyboardButton(
                        "😘ᴄʀᴇᴀᴛᴏʀ✨", url="https://t.me/StopFollowMe"
                    ),
                    InlineKeyboardButton(
                        "✨sᴜᴘᴘᴏʀᴛ💫", url="https://t.me/HaPpInEsS4Ev6"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🤔sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ​🤔", url="https://t.me/HaPpInEsS4Ev6"
                    )]
            ]
       ),
    )

@Client.on_message(command(["ping"]) & filters.group & ~filters.edited & ~filters.private)

async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fc5af1769743caa2bd6f1.png",
        caption=f"""ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ !🖤""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💕sᴜᴘᴘᴏʀᴛ💕", url=f"https://t.me/HaPpInEsS4Ev6")
                ]
            ]
        ),
    )
