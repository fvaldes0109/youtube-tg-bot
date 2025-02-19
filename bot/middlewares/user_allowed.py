import os
from functools import wraps

from telegram import Update

ALLOWED_USER_IDS = list(map(int, os.getenv("ALLOWED_USER_IDS", "").split(",")))

def user_allowed(func):
    """Middleware function to allow only users in the whitelist."""
    @wraps(func)
    async def wrapper(update: Update, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id in ALLOWED_USER_IDS:
            return await func(update, *args, **kwargs)
        else:
            await update.message.reply_text("🚫 Access denied. You are not authorized to use this bot.")
    return wrapper
