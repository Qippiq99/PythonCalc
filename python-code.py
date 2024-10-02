from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Введите цену, и я помогу вам её разделить на 10.")

def divide_price(update: Update, context: CallbackContext) -> None:
    try:
        price = float(update.message.text)
        first_division = price / 10
        second_division = first_division / 10
        
        response = (
            f"Первая сумма (цена / 10): {first_division}\n"
            f"Вторая сумма (первая сумма / 10): {second_division}\n"
            "Введите новую цену для продолжения."
        )
        update.message.reply_text(response)
    except ValueError:
        update.message.reply_text("Пожалуйста, введите корректное число.")

def main() -> None:
    # Замените токен на ваш собственный
    updater = Updater("7202062305:AAEFixDdqL9y62cesEEH567I2iAt-nVLpZA")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, divide_price))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()