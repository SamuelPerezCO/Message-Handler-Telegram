from telegram import Update
from telegram.ext import ContextTypes , CommandHandler , ApplicationBuilder , MessageHandler , ConversationHandler , filters

import sys
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

GET_NAME , GET_LAST_NAME = range(2)


async def ask_for_name (update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("What's your name")
    return GET_NAME


async def get_name (update:Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["name"] = update.message.text
    await update.message.reply_text("What's your last name")
    return GET_LAST_NAME


async def get_last_name (update:Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["last_name"] = update.message.text
    await update.message.reply_text(
        f"""Thank You , The data is Name : {context.user_data['name']} , last name: {context.user_data['last_name']}""")
    return ConversationHandler.END

async def cancel_conversation (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Cancel Conversation")


info_conversation_handler = ConversationHandler(
    entry_points=[ CommandHandler("data" , ask_for_name)],
    states={
        GET_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
        GET_LAST_NAME:[MessageHandler(filters.TEXT & ~filters.COMMAND, get_last_name)],
    },
    fallbacks=[MessageHandler(filters.COMMAND , cancel_conversation)]
)

application = ApplicationBuilder().token(TOKEN).build()
application.add_handler( info_conversation_handler)

application.run_polling(allowed_updates=Update.ALL_TYPES)