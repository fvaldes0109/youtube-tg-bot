import os

from telegram.ext import ApplicationBuilder

from routes.api import init_routes
    
if __name__ == '__main__':
    
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    
    init_routes(app)

    app.run_polling()
