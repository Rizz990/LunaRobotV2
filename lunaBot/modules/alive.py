import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from lunaBot.events import register as MEMEK
from lunaBot import telethn as tbot

PHOTO = "https://telegra.ph/file/31bc57899d12435e668c4.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  LUNA = "**Holla I'm Zenkou Akaishi!** \n\n"
  LUNA += "🔴 **I'm Working Properly** \n\n"
  LUNA += "🔴 **My Master : [Rizzu](https://t.me/xflyrzu)** \n\n"
  LUNA += f"🔴 **Telethon Version : {tlhver}** \n\n"
  LUNA += f"🔴 **Pyrogram Version : {pyrover}** \n\n"
  LUNA += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/zenkourobot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/aboutrizzu")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=ZENKOU,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  ZENKOU AKAISHI = "✅ **bot restarted successfully**\n\n• Admin list has been **updated**"
  BUTTON = [[Button.url("📡 ᴜᴘᴅᴀᴛᴇs", "https://t.me/aboutrizzu")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)
