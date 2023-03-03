from .chatgpt import chatgpt
from .userconf import chat

from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler


chatgpt_command, chatgpt_apikey = range(2)


async def chatgpt_satrt(update: Update, context: CallbackContext.DEFAULT_TYPE) -> int:
    await update.message.reply_text("输入OpenAI API token以继续, 使用 /cancel 取消")
    return chatgpt_apikey


async def get_apikey(update: Update, context: CallbackContext.DEFAULT_TYPE) -> int:
    user = update.effective_user.id
    message = update.message.text
    chat.openai_key[user] = message
    await update.message.reply_text("已保存，使用 /cancel 终止聊天\n使用 /renew 重置聊天记录")
    return chatgpt_command


async def chatgpt_continue(update: Update, context: CallbackContext.DEFAULT_TYPE) -> int:
    user = update.effective_chat.id
    message = update.message.text
    chat.save_user_chat(user, message)
    text = chatgpt(user, chat.chat_history[user])
    await context.bot.send_message(update.effective_chat.id, text=f"{text}")
    return chatgpt_command


async def cancel(update: Update, context: CallbackContext.DEFAULT_TYPE) -> int:
    await update.message.reply_text("已终止聊天")
    return ConversationHandler.END


async def renew(update: Update, context: CallbackContext.DEFAULT_TYPE) -> int:
    user = update.effective_user.id
    chat.chat_history[user] = []
    await update.message.reply_text("已重置聊天记录")
    return chatgpt_command
