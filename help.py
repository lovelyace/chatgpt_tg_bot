from telegram import Update
from telegram.ext import CallbackContext


async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await update.message.reply_text("使用 /chatgpt 与ChatGpt聊天")
