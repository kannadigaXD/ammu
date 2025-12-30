from telegram import Update
from telegram.ext import ContextTypes
from .responses import get_reply


async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_member.new_chat_member.user
    name = user.first_name

    await context.bot.send_message(
        chat_id=update.chat_member.chat.id,
        text=f"👋 Hey {name} 😄\nGroup-ge swagatha guru 🔥"
    )


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.from_user.first_name
    text = update.message.text

    reply = get_reply(text, name)
    await update.message.reply_text(reply)
