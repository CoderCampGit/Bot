import telebot
from config import *
import random

bot = telebot.TeleBot(token) # Bot init

@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Я работаю!')

@bot.message_handler(commands=['ban'])
def ban(message):
    chat_id = message.chat.id
    user = message.from_user.id
    if user in admins:
        if message.reply_to_message:

            from_user = message.reply_to_message.from_user.id
            #bot.send_message(chat_id, from_user)
            try:
                bot.kick_chat_member(id, from_user)
                bot.send_message(chat_id, 'Правосудие свершилось!\nПользователь заблокирован!')
            except Exception as e:
                bot.send_message(chat_id, 'Произошла ошибка! Возможно пользователь являеться администратором!')
                bot.send_message(chat_id, e)
        else:
            bot.send_message(chat_id, 'Эта команда должна быть ответом на сообщение!')
    else:
        bot.send_message(chat_id, 'Вы не являетесь администратором!')

@bot.message_handler(commands=['unban'])
def unban(message):
    chat_id = message.chat.id
    user = mesage.from_user.id
    if user in admins:
        if message.reply_to_message:

            from_user = message.reply_to_message.from_user.id
            #bot.send_message(chat_id, from_user)
            try:
                bot.unban_chat_member(id, from_user)
                bot.send_message(chat_id, 'Кто то ошибся!\nПользователь разблокирован!')
            except Exception as e:
                bot.send_message(chat_id, 'Произошла ошибка!    ')
                bot.send_message(chat_id, e)
        else:
            bot.send_message(chat_id, 'Эта команда должна быть ответом на сообщение!')
    else:
        bot.send_message(chat_id, 'Вы не являетесь администратором!')
@bot.message_handler(commands=['mute'])
def unmute(message):
    chat_id = message.chat.id
    user = message.from_user.id
    if user in admins:
        if message.reply_to_message:

            from_user = message.reply_to_message.from_user.id
            #bot.send_message(chat_id, from_user)
            try:
                bot.restrict_chat_member(id, from_user, can_send_messages=False)
                bot.send_message(chat_id, 'Свершилось правосудие!\nПользователю заблокирована возможность писать сообщения')
            except Exception as e:
                bot.send_message(chat_id, 'Произошла ошибка!   ')
                bot.send_message(chat_id, e)
        else:
            bot.send_message(chat_id, 'Эта команда должна быть ответом на сообщение!')
    else:
        bot.send_message(chat_id, 'Вы не являетесь администратором!')

@bot.message_handler(commands=['rules'])
def rules(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, rules_banner )

@bot.message_handler(commands=['unmute'])
def mute(message):
    chat_id = message.chat.id
    user = message.from_user.id
    if user in admins:
        if message.reply_to_message:

            from_user = message.reply_to_message.from_user.id
            #bot.send_message(chat_id, from_user)
            try:
                bot.restrict_chat_member(id, from_user, can_send_messages=True)
                bot.send_message(chat_id, 'Пользователю возвращена способность писать сообщения')
            except Exception as e:
                bot.send_message(chat_id, 'Произошла ошибка! ')
                bot.send_message(chat_id, e)
        else:
            bot.send_message(chat_id, 'Эта команда должна быть ответом на сообщение!')
    else:
        bot.send_message(chat_id, 'Вы не являетесь администратором!')



@bot.message_handler(content_types=['text'])
def send_text(message):
    from_user = message.from_user.id
    chat_id = message.chat.id

    for i in range(0, len(other_lang)):
        if other_lang[i] in message.text.lower():
            bot.send_message(chat_id, 'Изыди')
    for i in range(0, len(top_lang)):
        if top_lang[i] in message.text.lower():
            bot.send_message(chat_id, 'Ай какой молодец!')

    for i in range(0, len(bad_words)):
        if bad_words[i] in message.text.lower():
            answer = random.randint(1,4)
            if answer == 1:
                bot.send_message(chat_id,'А ты шалун')
            elif answer == 2:
                bot.send_message(chat_id,'Кто как обзывается, тот так и называется!')
            elif answer == 3:
                bot.send_message(chat_id, 'Шя как достану ствол правосудия')
            elif answer == 4:
                bot.send_message(chat_id, 'Осуждаю!')
    if 'пасть порву' in message.text.lower():
        bot.send_message(chat_id, 'Пасть свою себе порви')



bot.polling()
