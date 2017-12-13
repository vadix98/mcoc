import telebot
from time import sleep
token = "491823665:AAHyOrksjAMOcZqaqn6yyAXJDY1GG-l35Cs"
import datetime
bot = telebot.TeleBot(token, threaded=False)

fileName = 'otrivki.txt'

f = open(fileName)
line = f.readlines()
i=0
line[-1] = "#БиблияНаКаждыйдень @mcocyouth_bot"
while i<139:
    bot.send_message(-1001202457643,line[i]+line[i+1]+"\n"+line[-1])
    i=i+3
    sleep(86400)
















#if now.hour == 23 and now.minute == 35:
 #   bot.send_message(-1001202457643, now)
#bot.get_updates(offset=None,limit=None)


# while True:
#     try:
#         bot.polling(none_stop=True)
#
#     except Exception as e:
#         print(e)
#         if now.hour == 21 and now.minute == 5:
#             bot.send_message(-1001202457643, now)
#         # или import traceback; traceback.print_exc() для печати полной инфы
#         time.sleep(15)






#last_upd = upd[-1]
#messege_from_user = last_upd.messege
#print(last_upd.message)


# def log(message,answer):
#     print("\n-------------")
#     from datetime import datetime
#     print(datetime.now())
#     print("Сообщение от (0) (1). (id=(2)) \n Текст - (3)".format(message.from_user.first_name,
#                                                                  message.from_user.last_name,
#                                                                  str(message.from_user.id),
#                                                                  message.text
#                                                                  ))
#
#     print(answer)
#

# @bot.message_handler(content_types=['text'])
# def handle_text(message):
#     answer = "Ты не умеешь играть в эту игру"
#     if message.text == "а":
#         answer = "б"
#         log(message,answer)
#         bot.send_message(message.chat.id,"б")
#     elif message.text == "в":
#             answer = "г"
#             log(message, answer)
#             bot.send_message(message.chat.id, "г")
#     elif message.text == "д":
#                 answer = "е"
#                 log(message, answer)
#                 bot.send_message(message.chat.id, "е")
#     else:
#                 bot.send_message(message.chat.id, answer)
#                 log(message, answer)
#
#
#
#
#


