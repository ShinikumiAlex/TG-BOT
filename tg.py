import telebot;
bot = telebot.TeleBot('7301991701:AAHbHgUtBQHW8z4dkLL_2A8T1IEwgmyfhtE')
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

#расписания
SCHEDULE = {
    "Понедельник": ["Химия 10:00", "Английский 14:00"],
    "Вторник": ["Биология 11:00", "Информатика 15:00"],
    "Среда": ["Физкультура 12:00", "Литература 16:00"],
    "Четверг": ["История 10:00", "Русский Язвк 14:00"],
    "Пятница": ["Математика 11:00", "Молдавский 15:00"],
}

#начальноее соо
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("📅 Увидеть расписание", callback_data="view_schedule")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Привет! Я бот твоей онлайн-школы. Нажми на кнопку ниже, чтобы увидеть расписание уроков.", 
        reply_markup=reply_markup
    )

#Кнопочки
def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "view_schedule":
        schedule_text = "\n\n".join([f"*{day}*\n" + "\n".join(lessons) for day, lessons in SCHEDULE.items()])
        query.edit_message_text(
            text=f"📚 Расписание на неделю:\n\n{schedule_text}",
            parse_mode="Markdown"
        )

#Основа
def main():
    updater = Updater("7301991701:AAHbHgUtBQHW8z4dkLL_2A8T1IEwgmyfhtE")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button_handler))

    # Запуск\
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
