from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, InlineKeyboardButton, InlineKeyboardMarkup

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=f"Привет, {user.first_name}! Я - простой бот. Как я могу помочь?",
        reply_markup=main_menu()
    )

def main_menu():
    keyboard = [
        [InlineKeyboardButton("Нажми меня", callback_data='button1')],
        [InlineKeyboardButton("Еще кнопка", callback_data='button2')],
    ]
    return InlineKeyboardMarkup(keyboard)

def button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    if query.data == 'button1':
        context.bot.send_message(chat_id=query.message.chat_id, text="Вы нажали на кнопку 1!")
    elif query.data == 'button2':
        context.bot.send_message(chat_id=query.message.chat_id, text="Вы нажали на кнопку 2!")

def main() -> None:
    updater = Updater("YOUR_BOT_TOKEN")
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, start))
    dp.add_handler(CallbackQueryHandler(button_click))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
