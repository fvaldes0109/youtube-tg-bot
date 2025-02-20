import os
import uuid
from pytubefix import YouTube
from telegram import Update

from helpers import is_youtube_link

async def download_video(update: Update, input_data: str) -> None:
    
    url, quality = input_data.split(' ')

    if not is_youtube_link(url):
        await update.callback_query.message.reply_text('Invalid youtube link')
        return
    
    try:
        
        await update.callback_query.message.reply_text('Downloading video...')
        yt = YouTube(url)
        stream = yt.streams.filter(file_extension='mp4', res=quality).first()
        filename = uuid.uuid4().hex + '.mp4'
        stream.download(output_path='/tmp', filename=filename)
        
        await update.callback_query.message.reply_text('Downloaded. Sending video...')
        
        file = open(f"/tmp/{filename}", 'rb')
        await update.callback_query.message.reply_video(video=file)
        # Delete video
        file.close()
        os.remove(f"/tmp/{filename}")
    except Exception as e:
        print(e)
        await update.callback_query.message.reply_text('Something went wrong')