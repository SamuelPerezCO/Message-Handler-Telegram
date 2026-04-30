from telegram import Update
from telegram.ext import ConversationHandler , CommandHandler , MessageHandler , ContextTypes , filters

"""Controlador con Conversation Handler"""


USERNAME , INFO , PHOTO = range(3)

class UserProfileController:

    @staticmethod
    async def starting_get_info (update:Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Profile Creation , Write your username: ")
        return USERNAME

    @staticmethod
    async def get_username (update:Update, context: ContextTypes.DEFAULT_TYPE):
        context.user_data["username"] = update.message.text
        await update.message.reply_text("Perfect, Write your info: ")
        return INFO

    @staticmethod
    async def get_info (update:Update, context: ContextTypes.DEFAULT_TYPE):
        context.user_data["userinfo"] = update.message.text
        await update.message.reply_text("Thank You , Can you send a profile photo?")
        return PHOTO
    
    @staticmethod
    async def get_photo (update:Update, context: ContextTypes.DEFAULT_TYPE):
        message = update.effective_message
        if message.photo: #Can be None
            context.user_data["user_photo"] = message.photo [-1].file_id
            await update.message.reply_photo(
                photo=context.user_data["user_photo"],
                caption = f"UserName : {context.user_data['username']} \n Info: {context.user_data["userinfo"]}"
            )
        else:
            await update.message.reply_text("No se proporciono una foto")
            await update.message.reply_text(
                caption = f"UserName : {context.user_data['username']} \n Info: {context.user_data["userinfo"]}"
            )
 
        return ConversationHandler.END
    
    @staticmethod
    async def cancel_operation (update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("The Operation was Cancel")
        return ConversationHandler.END
    
user_profile_controller_conversation_handler = ConversationHandler(
    entry_points=[CommandHandler("profile" , UserProfileController.starting_get_info)],
    states = {
        USERNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, UserProfileController.get_username)],
        INFO: [MessageHandler(filters.TEXT & ~filters.COMMAND, UserProfileController.get_info)],
        PHOTO : [MessageHandler(filters.ALL & ~filters.COMMAND, UserProfileController.get_photo)],
    },
    fallbacks=[MessageHandler(filters.COMMAND, UserProfileController.cancel_operation)]
)