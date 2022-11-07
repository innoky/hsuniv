#---------------------------------------------------------------------------



import telebot
import random
from telebot import types



#---------------------------------------------------------------------------



bot = telebot.TeleBot('5654797665:AAFWZlDHscyks90H_8lP0sD_g2LOOupw7cY')
 
@bot.message_handler(commands=['start'])



#---------------------------------------------------------------------------



def welcome(message):

 
    # keyboard (Создание кнопок и приветствие)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("📙 Персонализировать материал")
    item2 = types.KeyboardButton("📘 Популярное")
    item3 = types.KeyboardButton("📗 Случайная статья")
 
    markup.add(item1, item2, item3)
 
    bot.send_message(message.chat.id, "Здравствуй, {0.first_name}!\nЯ - HS Intelligence. Пока что многие мои функции в разработке, но скоро я смогу подобрать интересный для тебя учебный материал и много чего другого! Желаю успехов) ".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])



#---------------------------------------------------------------------------



def lalala(message):
    if message.chat.type == 'private':
        if message.text == '📙 Персонализировать материал':
            bot.send_message(message.chat.id, 'Пока что эта функция в разработке, но скоро она станет доступна!')

        # elif message.text == ' '
        elif message.text == "📗 Случайная статья":
            list_st = ["https://telegra.ph/CHast-1-Grafiki-funkcii-10-31","https://telegra.ph/Krivolinejnoe-dvizhenie-10-13","https://telegra.ph/Perevod-chisel-iz-desyatichnoj-sistemy-schisleniya-10-08", "https://telegra.ph/Sposob-nahodit-znacheniya-celyh-kubicheskih-kornej-v-ume-09-30", "https://telegra.ph/Kak-najti-kvadratnyj-koren-lyubogo-racionalnogo-chisla-na-bumage-09-28", "https://telegra.ph/Algebraicheskie-uravneniya-i-neravenstva-Lekciya-ZFTSH-MFTI-09-23", "https://telegra.ph/Kodirovanie-graficheskoj-informacii-09-21", "https://telegra.ph/Kompleksnye-chisla-09-18", "https://telegra.ph/Kinematika-Konspekt-2-09-18", "https://telegra.ph/Kodirovanie-tekstovoj-informacii-09-14", "https://telegra.ph/Osnovnye-opredeleniya-fiziki-Konspekt-09-06", "https://telegra.ph/Metod-matematicheskoj-indukcii-08-28"]
            random_index = random.randrange(len(list_st))
            list_stik = ["CAACAgIAAxkBAAEGUyljZsZpa4LRXxbSEKAVV7ApTRyqrAAC3MYBAAFji0YMsbUSFEouGv8rBA", "CAACAgIAAxkBAAEGUyxjZsZwcRZICAXFXyXZ6HlkGVIbmAAC3cYBAAFji0YM608pO-wjAlErBA", "CAACAgIAAxkBAAEGUy5jZsZxUAN7jhaQgypRx001c3CPGwAC3sYBAAFji0YMVHH9hav7ILkrBA", "CAACAgIAAxkBAAEGUzFjZsZ1Shg2QQzidBWLN_Wm_E4SVgAC38YBAAFji0YMHEUTINW7YxcrBA"]
            random_index1 = random.randrange(len(list_stik))
            bot.send_sticker(message.chat.id, list_stik[random_index1])
            bot.send_message(message.chat.id, list_st[random_index])

        elif message.text == "📘 Популярное":
            bot.send_message(message.chat.id, 'Кажется это самая читаемая статья, возможно она вам покажется интересной \n\nhttps://telegra.ph/Sposob-nahodit-znacheniya-celyh-kubicheskih-kornej-v-ume-09-30', parse_mode='html')


        else:
            bot.send_message(message.chat.id, 'Пока что я не могу воспринимать свободный текст, так что посмотрите что есть в списке доступных команд)')



#---------------------------------------------------------------------------

#---------------------------------------------------------------------------


# Старт
bot.polling(none_stop=True)



#---------------------------------------------------------------------------