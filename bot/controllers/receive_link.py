from pytubefix import YouTube
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

from helpers import is_youtube_link

async def receive_link(update: Update, message_text: str) -> None:
    
    if not is_youtube_link(message_text):
        await update.message.reply_text("Please send a valid YouTube link")
        return
    
    yt = YouTube(message_text, 'WEB')
    title, thumbnail = yt.title, yt.thumbnail_url
    streams = yt.streams.filter(file_extension="mp4").order_by("resolution").desc()
    qualities = [f"{stream.resolution}" for stream in streams]
    sizes = [f"{stream.filesize / 1024 / 1024:.2f} MB" for stream in streams]
    
    qualities_sizes = list(zip(qualities, sizes))

    # Creating buttons with two elements per row
    buttons = []
    for i in range(0, len(qualities_sizes), 2):
        row = [
            InlineKeyboardButton(f"{qualities_sizes[i][0]} / {qualities_sizes[i][1]}", callback_data=f"{message_text} {qualities_sizes[i][0]}")
        ]
        if i + 1 < len(qualities_sizes):  # Add second button if it exists
            row.append(
                InlineKeyboardButton(f"{qualities_sizes[i+1][0]} / {qualities_sizes[i+1][1]}", callback_data=f"{message_text} {qualities_sizes[i+1][0]}")
            )
        buttons.append(row)
    
    keyboard = InlineKeyboardMarkup(buttons)
    
    await update.message.reply_photo(thumbnail, title, reply_markup=keyboard)
    
    