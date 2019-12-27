""".admin Plugin for @XtraTgBot"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @XtraTgBot"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**` Jis #Race se mujhe nikalne ki koshish kar rahe hai yeh bewakoof woh yeh nahi jaante ki is #Race ka Sikandar main hu ! Chalo bahut ho gaya khelna khilana ab dekho ψ(｀∇´)ψ`**\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\special Thanks - @miya_bhi\n`Crew Challenge: #4 Rank holder \n\nAlways with you, my master!\n`"
                     f"`My peru owner`: {DEFAULTUSER}\n"
                     "[Deploy this userbot Now](https://github.com/Dark-Princ3/X-tra-Telegram)")
