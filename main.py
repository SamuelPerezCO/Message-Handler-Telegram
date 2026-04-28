from telegram import Update
from telegram.ext import ContextTypes , CommandHandler , ApplicationBuilder , MessageHandler , ConversationHandler , filters

import sys
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


async def say_hello (update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Conversacion Iniciada")


async def send_message (update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Has escrito un mensaje")

application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(CommandHandler("start", say_hello) )
application.add_handler( MessageHandler(filters.TEXT & ~filters.AUDIO , send_message ))

application.run_polling(allowed_updates=Update.ALL_TYPES)