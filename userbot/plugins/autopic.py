import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
import asyncio

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

@command(pattern="^.autopic", outgoing=True)
async def autopic(event):
    downloaded_file_name = "userbot/original_pic.png"
    downloader = SmartDL(Var.DOWNLOAD_PFP_URL_CLOCK, downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    while not downloader.isFinished():
        place_holder = None
    im = Image.open(downloaded_file_name)
    photo = "userbot/photo_pfp.png"
    file_test = im.rotate(-1, expand=True).save(photo, "PNG")
    while True:
        current_time = datetime.now().strftime("⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ \n ⚡USERBOT TIMEZONE⚡ \n  Time: %H:%M:%S \n  Date: %d.%m.%y \n⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡")
        drawn_text = ImageDraw.Draw(photo)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((10, 10), current_time, font=fnt, fill=(255, 255, 255)).save("userbot/photo_complete.png", "PNG")
        file = await bot.upload_file("userbot/photo_complete.png")  # pylint:disable=E0602
        try:
            await bot(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove("userbot/photo_complete.png")
            await asyncio.sleep(60)
        except:
            return
