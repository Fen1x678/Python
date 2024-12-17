from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Определение состояний конечного автомата
START, STATE_1, STATE_2 = range(3)

def start(update: Update, context: CallbackContext) -> int:
    user = update.effective_user
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=f"Привет, {user.first_name}! Я - бот с конечным автоматом. Как я могу помочь?",
        reply_markup=main_menu()
    )
    return START

def main_menu():
    keyboard = [
        [InlineKeyboardButton("Перейти в состояние 1", callback_data='state1')],
        [InlineKeyboardButton("Перейти в состояние 2", callback_data='state2')],
    ]
    return InlineKeyboardMarkup(keyboard)

def button_click(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    if query.data == 'state1':
        context.bot.send_message(chat_id=query.message.chat_id, text="Вы перешли в состояние 1!", reply_markup=main_menu())
        return STATE_1
    elif query.data == 'state2':
        context.bot.send_message(chat_id=query.message.chat_id, text="Вы перешли в состояние 2!", reply_markup=main_menu())
        return STATE_2

def end(update: Update, context: CallbackContext) -> int:
    context.bot.send_message(chat_id=update.message.chat_id, text="Вы завершили взаимодействие с ботом. До свидания!")
    return ConversationHandler.END

def main() -> None:
    updater = Updater("YOUR_BOT_TOKEN")
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            START: [CallbackQueryHandler(button_click)],
            STATE_1: [CallbackQueryHandler(button_click)],
            STATE_2: [CallbackQueryHandler(button_click)],
        },
        fallbacks=[CommandHandler('end', end)]
    )

    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
