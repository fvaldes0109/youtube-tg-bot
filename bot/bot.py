import os

from telegram.ext import ApplicationBuilder

from routes.api import init_routes
import logging

if __name__ == '__main__':

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    
    init_routes(app)

    app.run_polling()
