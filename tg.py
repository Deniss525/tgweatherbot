import pyowm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

import telebot
bot = telebot.TeleBot("5217616495:AAFyxxsBGOWA-15UaqUPDQ-0ycTCHXmb4lc")

owm = OWM('ca8eaf9567ef0fc4d68d253abd1da6aa')
mgr = owm.weather_manager()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Ohayo, onii-chan! Your city/country is: ")

@bot.message_handler(content_types=['text'])
def send_weather(message):
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	temp = w.temperature('celsius')['temp']
	feel = w.detailed_status
	wind = w.wind()['speed']

	answer = 'In '+ message.text +' now is ' + str(temp) + ' degrees.' + '\n'
	answer += 'It feels like ' + str(feel) + ' today.' + '\n'
	answer += 'Wind speed is around ' + str(wind) + ' m/s.' + '\n\n'

	if temp < 1:
		answer += 'Today is cold, pls dress warmly <3 '
	elif temp < 10:
		answer += 'Today is quite cold, u need to dress warmly UwU'
	elif temp < 20:
		answer += 'Today is not so cold, perfect weather :3'
	else:
		answer += 'Yeeah now is really warm outside!'

	bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)