#Code by xIRANx and CoderCamp community
import telebot
from config import *
import random
import keyboard as kb
#Технические списки

#---------------------
bot = telebot.TeleBot(token) # Bot init

@bot.message_handler(content_types=['new_chat_members'])
def handler_new_member(message):
    try:
        user_name = message.from_user.first_name
        bot.send_message(message.chat.id, 'Добро пожаловать, {0}!'.format(user_name) + '\nРасскажи о себе немного, какие языки программироания знаешь?')
    except:
        print('Error')

@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Привет!')

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
                bot.send_message(chat_id, 'Правосудие свершилось!\nПользователь заблокирован!', reply_markup=kb.unban)
            except Exception as e:
                bot.send_message(chat_id, 'Произошла ошибка! Возможно пользователь являеться администратором!')
        else:
            bot.send_message(chat_id, 'Эта команда должна быть ответом на сообщение!')
    else:
        bot.send_message(chat_id, 'Вы не являетесь администратором!')

@bot.message_handler(commands=['unban'])
def unban(message):
    chat_id = message.chat.id
    user = message.from_user.id
    if user in admins:
        try:
            text = message.text
            arg = text.split(' ')
            bot.send_message(chat_id, 'ID:' + arg[1])
            bot.unban_chat_member(chat_id, arg)
            bot.send_message('Оно свершилось! Пользователь разблокирован')
        except Exception as e:
            bot.send_message(chat_id,'Что то пошло не так!')
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
    msg = message.text.lower()
    msg_id = message.message_id
    for lang in top_lang:
        if lang in msg:
            bot.reply_to(message, 'Одобряю')
            break
    for lang in other_lang:
        if lang in msg:
            bot.reply_to(message, 'Осуждаю')
            break
    for word in bad_words:
        if word in msg:
            bot.reply_to(message, 'Веди себя культурнее!')
            break
    else:
        pass

bot.polling()
