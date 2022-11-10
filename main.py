#---------------------------------------------------------------------------



import telebot
import time
import random
import os
import numpy as np
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

        #Число пи
        elif message.text == 'pi' or message.text == 'Pi' or message.text == 'Пи' or message.text == 'пи' or message.text == 'Число пи' or message.text == 'Число pi' or message.text == 'π':
            bot.send_message(message.chat.id, "3.1415926535897932384626433832795028841971693993751058209749445923078164062862 089986280348253421170679821480865132823066470938446095505822317253594081284811 174502841027019385211055596446229489549303819644288109756659334461284756482337 867831652712019091456485669234603486104543266482133936072602491412737245870066 063155881748815209209628292540917153643678925903600113305305488204665213841469 519415116094330572703657595919530921861173819326117931051185480744623799627495 673518857527248912279381830119491298336733624406566430860213949463952247371907 021798609437027705392171762931767523846748184676694051320005681271452635608277 857713427577896091736371787214684409012249534301465495853710507922796892589235 420199561121290219608640344181598136297747713099605187072113499999983729780499 510597317328160963185950244594553469083026425223082533446850352619311881710100 031378387528865875332083814206171776691473035982534904287554687311595628638823 537875937519577818577805321712268066130019278766111959092164201989380952572010 654858632788659361533818279682303019520353018529689957736225994138912497217752 834791315155748572424541506959508295331168617278558890750983817546374649393192 550604009277016711390098488240128583616035637076601047101819429555961989467678 374494482553797747268471040475346462080466842590694912933136770289891521047521 620569660240580381501935112533824300355876402474964732639141992726042699227967")

        #Случайная статья
        elif message.text == "📗 Случайная статья":
            list_st = ["https://telegra.ph/CHast-1-Grafiki-funkcii-10-31","https://telegra.ph/Krivolinejnoe-dvizhenie-10-13","https://telegra.ph/Perevod-chisel-iz-desyatichnoj-sistemy-schisleniya-10-08", "https://telegra.ph/Sposob-nahodit-znacheniya-celyh-kubicheskih-kornej-v-ume-09-30", "https://telegra.ph/Kak-najti-kvadratnyj-koren-lyubogo-racionalnogo-chisla-na-bumage-09-28", "https://telegra.ph/Algebraicheskie-uravneniya-i-neravenstva-Lekciya-ZFTSH-MFTI-09-23", "https://telegra.ph/Kodirovanie-graficheskoj-informacii-09-21", "https://telegra.ph/Kompleksnye-chisla-09-18", "https://telegra.ph/Kinematika-Konspekt-2-09-18", "https://telegra.ph/Kodirovanie-tekstovoj-informacii-09-14", "https://telegra.ph/Osnovnye-opredeleniya-fiziki-Konspekt-09-06", "https://telegra.ph/Metod-matematicheskoj-indukcii-08-28"]
            random_index = random.randrange(len(list_st))
            list_stik = ["CAACAgIAAxkBAAEGUyljZsZpa4LRXxbSEKAVV7ApTRyqrAAC3MYBAAFji0YMsbUSFEouGv8rBA", "CAACAgIAAxkBAAEGUyxjZsZwcRZICAXFXyXZ6HlkGVIbmAAC3cYBAAFji0YM608pO-wjAlErBA", "CAACAgIAAxkBAAEGUy5jZsZxUAN7jhaQgypRx001c3CPGwAC3sYBAAFji0YMVHH9hav7ILkrBA", "CAACAgIAAxkBAAEGUzFjZsZ1Shg2QQzidBWLN_Wm_E4SVgAC38YBAAFji0YMHEUTINW7YxcrBA"]
            random_index1 = random.randrange(len(list_stik))
            bot.send_sticker(message.chat.id, list_stik[random_index1])
            bot.send_message(message.chat.id, list_st[random_index])

        #интегрирования
        elif "integral" in message.text:
            clear_func = message.text.replace("integral ", "")
            with open("int_get.txt", "w") as file:
                file.write(clear_func)
            os.system('python3 integral.py')

            time.sleep(2)
            with open("int_out.txt", "r") as file:
                for line in file:
                    text1 = str(line)
                bot.send_message(message.chat.id, text1)
        #популярная статья
        elif message.text == "📘 Популярное":
            bot.send_message(message.chat.id, 'Кажется это самая читаемая статья, возможно она вам покажется интересной \n\nhttps://telegra.ph/Sposob-nahodit-znacheniya-celyh-kubicheskih-kornej-v-ume-09-30', parse_mode='html')


        elif "tc" in message.text:
            a = message.text.lower()
            if "0 deg" in message.text and not "1" in a and not "2" in a and not "3" in a and not "6" in a and not "9" in a :
                bot.send_photo(message.chat.id, open('/home/innoky/Documents/hsbot/hsuniv/tgcircle/0.png', 'rb'));
                bot.send_message(message.chat.id, "Sin = 1\nCos = 0")
            elif "30 deg" in message.text:
                bot.send_photo(message.chat.id, open('/home/innoky/Documents/hsbot/hsuniv/tgcircle/30.png', 'rb'));
                bot.send_message(message.chat.id, "Sin = sqrt(3) / 2\nCos = 1 / 2")
            elif "45 deg" in message.text:
                bot.send_photo(message.chat.id, open('/home/innoky/Documents/hsbot/hsuniv/tgcircle/45.png', 'rb'));
            elif "60 deg" in message.text:
                bot.send_photo(message.chat.id, open('/home/innoky/Documents/hsbot/hsuniv/tgcircle/60.png', 'rb'));
            elif "90 deg" in message.text:
                bot.send_photo(message.chat.id, open('/home/innoky/Documents/hsbot/hsuniv/tgcircle/90.png', 'rb'));
            elif "120 deg" in message.text:
                bot.send_photo(message.chat.id, open('/home/innoky/Documents/hsbot/hsuniv/tgcircle/120.png', 'rb'));
            elif "135 deg" in message.text:
                bot.send_photo(message.chat.id, open('/home/innoky/Documents/hsbot/hsuniv/tgcircle/135.png', 'rb'));
            elif "150 deg" in message.text:
                bot.send_photo(message.chat.id, open('/home/innoky/Documents/hsbot/hsuniv/tgcircle/150.png', 'rb'));
            elif "180 deg" in message.text:
                bot.send_photo(message.chat.id, open('/home/innoky/Documents/hsbot/hsuniv/tgcircle/180.png', 'rb'));
            elif "210 deg" in message.text:
                bot.send_photo(message.chat.id, open('/home/innoky/Documents/hsbot/hsuniv/tgcircle/210.png', 'rb'));
            elif "225 deg" in message.text:
                bot.send_photo(message.chat.id, open('/home/innoky/Documents/hsbot/hsuniv/tgcircle/225.png', 'rb'));
            elif "240 deg" in message.text:
                bot.send_photo(message.chat.id, open('/home/innoky/Documents/hsbot/hsuniv/tgcircle/240.png', 'rb'));
            elif "270 deg" in message.text:
                bot.send_photo(message.chat.id, open('/home/innoky/Documents/hsbot/hsuniv/tgcircle/270.png', 'rb'));
            elif "300 deg" in message.text:
                bot.send_photo(message.chat.id, open('/home/innoky/Documents/hsbot/hsuniv/tgcircle/300.png', 'rb'));
            elif "315 deg" in message.text:
                bot.send_photo(message.chat.id, open('/home/innoky/Documents/hsbot/hsuniv/tgcircle/315.png', 'rb'));
            elif "330 deg" in message.text:
                bot.send_photo(message.chat.id, open('/home/innoky/Documents/hsbot/hsuniv/tgcircle/330.png', 'rb'));
        #простые числа
        elif "простое число" in message.text:
            a = message.text.lower()
            if "первое" in a:
                bot.send_message(message.chat.id,message.text + ": 2")
            elif "второе" in a:
                bot.send_message(message.chat.id,message.text + ": 3")
            elif "третье" in a:
                bot.send_message(message.chat.id,message.text + ": 5")
            elif "четвертое" in a:
                bot.send_message(message.chat.id,message.text + ": 7")
            elif "пятое" in a:
                bot.send_message(message.chat.id,message.text + ": 11")
            elif "шестое" in a:
                bot.send_message(message.chat.id,message.text + ": 13")
            elif "седьмое" in a:
                bot.send_message(message.chat.id,message.text + ": 17")
            elif "восьмое" in a:
                bot.send_message(message.chat.id,message.text + ": 19")
            elif "девятое" in a:
                bot.send_message(message.chat.id,message.text + ": 23")
            elif "десятое" in a:
                bot.send_message(message.chat.id,message.text + ": 27")



        #Неизвестная команда
        else:
            bot.send_message(message.chat.id, 'Пока что я не могу воспринимать свободный текст, так что посмотрите что есть в списке доступных команд)')



#---------------------------------------------------------------------------

#---------------------------------------------------------------------------


# Старт
bot.polling(none_stop=True)



#---------------------------------------------------------------------------
