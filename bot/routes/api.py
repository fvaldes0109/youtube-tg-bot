from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, MessageHandler, filters, CallbackQueryHandler

from middlewares import user_allowed
from controllers import receive_link, download_video

@user_allowed
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

@user_allowed
async def process_link(update: Update, context: CallbackContext) -> None:

    message_text = update.message.text
    await receive_link(update, message_text)
    
@user_allowed
async def download_video_with_quality(update: Update, context: CallbackContext) -> None:
    
    query = update.callback_query
    
    await query.answer()
    await download_video(update, query.data)
    
def init_routes(app: ApplicationBuilder):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, process_link))
    app.add_handler(CallbackQueryHandler(download_video_with_quality))
    