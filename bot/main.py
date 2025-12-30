from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ChatMemberHandler,
    filters
)

from bot.handlers import welcome, chat
from bot.config import BOT_TOKEN


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("🔥 Kanglish Bot is LIVE...")
    app.run_polling()


if __name__ == "__main__":
    main()
