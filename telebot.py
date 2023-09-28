import telebot

from classes import APIException, CurrencyConverter

from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_help(message):
    instructions = "Привет! Я бот для получения цены на валюту.\n" \
                   "Для получения цены нужно написать сообщение в формате:\n" \
                   "<имя валюты, цену которой вы хотите узнать> <имя валюты, в которой надо узнать цену первой>" \
                   "<количество первой валюты>\n" \
                   "Например: USD RUB 10\n" \
                   "Для получения списка доступных валют используй команду /values"
    bot.reply_to(message, instructions)


@bot.message_handler(commands=['values'])
def send_values(message):
    values = "Доступные валюты:\n" \
             "Евро - EUR\n" \
             "Доллар - USD\n" \
             "Рубль - RUB"
    bot.reply_to(message, values)


@bot.message_handler(func=lambda message: True)
def send_price(message):
    try:
        text = message.text.upper().split()
        if len(text) != 3:
            raise Exception("Invalid input format. Please enter: <base currency> <quote currency> <amount>")

        base, quote, amount = text
        amount = float(amount)
        result = CurrencyConverter.get_price(base, quote, amount)
        response = f"Цена {amount} {base} в {quote}: {result}"
        bot.reply_to(message, response)
    except Exception as e:
        bot.reply_to(message, f"Error occurred: {type(e).__name__}")


bot.polling()