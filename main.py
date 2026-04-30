from telegram import Update
from telegram.ext import ContextTypes , CommandHandler , ApplicationBuilder , MessageHandler , ConversationHandler , filters

from Controllers.UserProfileController import user_profile_controller_conversation_handler

import sys
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

GET_NAME , GET_LAST_NAME = range(2)


application = ApplicationBuilder().token(TOKEN).build()
application.add_handler( user_profile_controller_conversation_handler )

application.run_polling(allowed_updates=Update.ALL_TYPES)