import telebot
import requests
import json

bot = telebot.TeleBot('6770420064:AAHrpItQGicrYuVAqAvLKgnrWnTfeCWtdXw')
API = '1bc9818d4d78ee8300248f8fdceb004a'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привіт, радий тебе вітати! Напиши назву міста погода якого тобі цікава.')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot.reply_to(message, f'Зараз погода {data["main"]["temp"]} градусів цельсія')

    else:
        bot.reply_to(message, 'Неправильно вказане місто')


bot.polling(none_stop=True)