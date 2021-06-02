import telebot
from config import *


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
    chat_id = message.chat.id
    if message.text in languages:
        bot.send_message(chat_id, 'Изыди')
    else:
        pass

bot.polling()
