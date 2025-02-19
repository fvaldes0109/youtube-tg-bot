from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, MessageHandler, filters

from middlewares import user_allowed
from controllers import receive_link

@user_allowed
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

@user_allowed
async def echo(update: Update, context: CallbackContext) -> None:
    
    message_text = update.message.text
    await receive_link(update, message_text)
    
def init_routes(app: ApplicationBuilder):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, echo))