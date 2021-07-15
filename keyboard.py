import telebot
from telebot import types

#Создание клавиатур
def make_inline(items):
    #Создаем markup
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    #Помещаем каждый элемент из списка в markup
    for i in items:
        markup.add(types.InlineKeyboardButton(i, callback_data=i))

    #Тут без комментариев
    return markup

def make(items):
    #Создаем markup
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.row_width = 3
    #Помещаем каждый элемент из списка в markup
    for i in items:
        markup.add(types.InlineKeyboardButton(i))
    #Тут без комментариев
    return markup
