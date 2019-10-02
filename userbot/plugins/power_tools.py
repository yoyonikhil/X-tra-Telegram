import asyncio
import os
import sys


@command(pattern="^.restart", outgoing=True)
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Restarting. `.ping` me or `.helpme` in a few minutes to check if I am online")
    await bot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)


@command(pattern="^.shutdown", outgoing=True)
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Turning off ...Manually turn me on later")
    await bot.disconnect()
