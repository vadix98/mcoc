import telebot

token = "491823665:AAHyOrksjAMOcZqaqn6yyAXJDY1GG-l35Cs"
bot = telebot.TeleBot(token, threaded=False)

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
    user_markup.row('поделиться хорошей новостью!😊')
    user_markup.row('поделиться отрывком из Библии!👍🏻')
    user_markup.row('поделиться интересными мыслями!😋')
    user_markup.row('/start', '/stop')
    bot.send_message(message.from_user.id,'Привет, друг! \nУ тебя есть возможность поделиться хорошей новостью, интересными мыслями или отрывком из Библии, который тебя вдохновил!\n\nВыбирай пункт меню, затем пиши соответствующее сообщение!\n'
                                          'Если хочешь чтобы сообщение было не анонимно, подпиши свое имя после сообщения!\n\n'
                                          'Чтобы завершить работу с ботом нажми(или напиши) - /stop'
                                          '\n чтобы заново начать работу с ботом нажми(или напиши) - /start',reply_markup=user_markup)
#     bot.reply_to(message, """\
# Привет, друг!
# У тебя есть возможность поделиться хорошей новостью, интересными мыслями или отрывком из Библии, который тебя вдохновил!
# """)
@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id,'..',reply_markup=hide_markup)

@bot.message_handler(content_types=['text'])
def handle_start(message):
 if message.text == 'поделиться хорошей новостью!😊':
        bot.send_message(message.from_user.id, 'Расскажи свою хорошую новость!\n(Если хочешь чтобы сообщение было не анонимно, подпиши свое имя после сообщения!)')
 elif message.text == 'поделиться интересными мыслями!😋':
     bot.send_message(message.from_user.id, 'Поделись интересными мыслями!\n(Если хочешь чтобы сообщение было не анонимно, подпиши свое имя после сообщения!)')
 elif message.text == 'поделиться отрывком из Библии!👍🏻':
     bot.send_message(message.from_user.id, 'Поделись отрывком из Библии!\n(Если хочешь чтобы сообщение было не анонимно, подпиши свое имя после сообщения!)')
 else:
    bot.forward_message(-1001202457643,message.from_user.id,message.message_id)

# if messagefun == 2:
#  bot.send_message(-1001202457643, message.text+"/n ----------- /n новость")
 #  elif messagefun == 1:
   # bot.send_message(-1001202457643, message.text+"/n ----------- /n новость")


bot.polling(none_stop=True)
