import telebot
bot = telebot.TeleBot('1727750386:AAFB57gczJbck5j7e8eC3Xw7zb21ZM7NYbo')
with open('words.txt', 'r') as file:
    words = file.readlines()
p = ['Привет','привет','/start']
d = ['Да','да','давай','Давай']
word = []
@bot.message_handler(content_types=['text'])



def get_text_messages(message):

        if message.text in p:
            bot.send_message(message.from_user.id, "Привет, сыграем в слова??")
        elif message.text in d:
            bot.send_message(message.from_user.id, "Ты начинаешь!")
        else:
            for w in list(words):
                if (message.text[-1] == w[0] and w not in word):
                    word.append(w)
                    bot.send_message(message.from_user.id, word[-1])
                    break
                    continue





bot.polling(none_stop=True)

