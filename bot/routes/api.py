from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, MessageHandler, filters

from middlewares import user_allowed

@user_allowed
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

@user_allowed
async def echo(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(update.message.text)
    
def init_routes(app: ApplicationBuilder):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, echo))