import os, time
from telebot import TeleBot, types

token = '1945603676:AAFMynOpoE4_SDz1dvXfIRcqg-5Bxfcl1Ag'
bot = TeleBot(token)
counter = 0

facts = 'cool beautiful awesome perfect lovely breathtaking gorgeous hot'
tripod_options = ['Tripod fact of the day', 'Tripod picture of the day',
				  'Tripod poem of the day', 'I don\'t like tripods']

poems = ["Roses are red\nViolets are blue\nTripods are my life\nMy love for them is true",
		 "A tripod a day\nKeeps the doctor away",
		 "Twinkle, twinkle, little star\nI will figure what you are\nWith a tripod that's so high\nIt will reach you in the sky",
		 "Yesterday\nAll my tripods seemed so far away\nNow I have them all with me to stay\nBecause I got a tripod case"]


@bot.message_handler(commands=['start'])
def send_welcome(message):
	cid = message.chat.id
	markup = types.ReplyKeyboardMarkup(row_width=2)
	btns = map(types.KeyboardButton, tripod_options)
	markup.add(*btns)

	bot.send_message(cid, "What tripod related information may I provide?", reply_markup=markup)


@bot.message_handler(func=lambda x: True)
def reply(message):
	cid = message.chat.id
	cycle = globals()['counter']
	if message.text == 'Tripod fact of the day':
		bot.send_message(cid, f'Tripods are {facts.split()[cycle % 8]}!')
	elif message.text == 'Tripod picture of the day':
		photo = open(os.path.join('pics', f'{cycle}.jpg', ), 'rb')
		bot.send_photo(cid, photo)
	elif message.text == 'Tripod poem of the day':
		bot.send_message(cid, poems[cycle % 5])
	elif message.text == 'I don\'t like tripods':
		bot.send_message(cid, "Screw you! Tripods are my friends and they are better than you!")
	else:
		bot.send_message(cid, "There are no tripods for this option 🙁")
	globals()['counter'] = (cycle + 1) % 10
	print(cycle)

while True:
	try:
		bot.polling(none_stop=True)
	except:
		time.sleep(5)
