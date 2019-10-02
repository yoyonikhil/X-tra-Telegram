from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.utils import load_module
from userbot import LOAD_PLUG, BOTLOG_CHATID, LOGS
from pathlib import Path
import asyncio

async def add_bot(bot_token):
    await bot.start(bot_token)

try:
    bot.start()
except PhoneNumberInvalidError:
    print("Phone Number you added was incorrect. Make sure to use your country code with your code")
    exit(1)

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
    bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))

async def botlog():
    if not BOTLOG_CHATID:
        LOGS.info(
        "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, "
        "many critical features depend on it. KTHXBye.")

    if BOTLOG_CHATID is not None:
        entity = await bot.get_entity(BOTLOG_CHATID)
        if entity.default_banned_rights.send_messages:
            LOGS.info(
                "Your account doesn't have rights to send messages to BOTLOG_CHATID "
                "group. Check if you typed the Chat ID correctly.")
            quit(1)

with bot:
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except:
        LOGS.info(
            "BOTLOG_CHATID environment variable isn't a "
            "valid entity. Check your environment variables/config.env file.")

import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))
        print("Successfully (re)imported {}".format(f.name.replace("userbot/plugins/", "")))

import userbot._core

os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)

print("Yay your userbot is officially working.")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()


