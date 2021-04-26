import telebot
import config

from utils import card_correct
from utils import generate_dice
import time

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

# todo для конкретного юзера конкртеные ластмес и гаме
last_message = ""
game = ""
bal = 0
bj_kostyl = 0


@bot.message_handler(commands=['start'])
def welcome(message):
    item1 = types.KeyboardButton("Игры")
    item2 = types.KeyboardButton("Пополнить балланс")
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True)
    markup.add(item1, item2)

    bot.send_message(chat_id=message.chat.id,
                     text="Добро пожаловать, {0.first_name}!\n"
                          "Я - <b>{1.first_name}</b>.".
                     format(message.from_user, bot.get_me()),
                     parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(commands=['bj'])
def dice_m(message):
    global last_message
    global game
    last_message = ""
    item1 = types.KeyboardButton("ИГРАТЬ")
    item2 = types.KeyboardButton("ЗАВЕРШИТЬ ИГРУ")
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=False)
    markup.add(item1, item2)

    bot.send_message(chat_id=message.chat.id,
                     text="{0.first_name}, добро пожаловать в игру 'Блэкджэк на минималках'\n"
                          "Здесь ты можешь выиграть, если наберешь 21 очко.\n"
                          "Чтобы начать, нажми 'ИГРАТЬ'\n"
                          "Желаю удачи!".

                     format(message.from_user, bot.get_me()),
                     parse_mode='html',
                     reply_markup=markup)

    bot.send_message(chat_id=message.chat.id,
                     text="Правила:\n"
                          "Карты от 2 до 10 стоят столько, сколько на них написано\n"
                          "J, Q, K - стоят 10 очков\n"
                          "A может стоить либо 1, либо 11\n"
                          "В блэкджэке платят 3:2")
    bot.send_message(chat_id=message.chat.id,
                     text="Правила:\n"
                          "1) Сделайте ставку (10, 50, 100 рублей)\n"
                          "2) Раздача карт: диллер и игрок получают по 2 карты"
                          "3) на каждом ходу вы можете:\n"
                          "\tHIT - взять еще одну карту\n"
                          "\tSTAND - больше не брать\n"
                          "\tSURRENDER - откат: диллер забирает половину вашей ставки и раздача заканчивается")
    game = "BJ"


@bot.message_handler(commands=['diceE'])
def dice_e(message):
    global last_message
    global game
    last_message = ""
    item1 = types.KeyboardButton("ИГРАТЬ")
    item2 = types.KeyboardButton("ЗАВЕРШИТЬ ИГРУ")
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=False)
    markup.add(item1, item2)

    bot.send_message(chat_id=message.chat.id,
                     text="{0.first_name}, добро пожаловать в игру 'Кости. Простой уровень'\n"
                          "Здесь ты можешь выиграть, оба выпавших числа больше 3.\n"
                          "Цена игры - 10 рублей\n"
                          "Ты можешь выиграть - 15 рублей\n"
                          "Чтобы начать, нажми 'ИГРАТЬ'\n"
                          "Желаю удачи!".

                     format(message.from_user, bot.get_me()),
                     parse_mode='html',
                     reply_markup=markup)
    game = "KE"


@bot.message_handler(commands=['diceM'])
def dice_m(message):
    global last_message
    global game
    last_message = ""
    item1 = types.KeyboardButton("ИГРАТЬ")
    item2 = types.KeyboardButton("ЗАВЕРШИТЬ ИГРУ")
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=False)
    markup.add(item1, item2)

    bot.send_message(chat_id=message.chat.id,
                     text="{0.first_name}, добро пожаловать в игру 'Кости. Средний уровень'\n"
                          "Здесь ты можешь выиграть, если выпадет дубль.\n"
                          "Цена игры - 10 рублей\n"
                          "Ты можешь выиграть - 20 рублей\n"
                          "Чтобы начать, нажми 'ИГРАТЬ'\n"
                          "Желаю удачи!".

                     format(message.from_user, bot.get_me()),
                     parse_mode='html',
                     reply_markup=markup)
    game = "KM"


@bot.message_handler(commands=['diceH'])
def dice_h(message):
    global last_message
    global game
    last_message = ""
    item1 = types.KeyboardButton("ИГРАТЬ")
    item2 = types.KeyboardButton("ЗАВЕРШИТЬ ИГРУ")
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=False)
    markup.add(item1, item2)

    bot.send_message(chat_id=message.chat.id,
                     text="{0.first_name}, добро пожаловать в игру 'Кости. Сложный уровень'\n"
                          "Здесь ты можешь выиграть, если тебе выпадет дубль чётных чиел.\n"
                          "Цена игры - 10 рублей\n"
                          "Ты можешь выиграть - 500 рублей\n"
                          "Чтобы начать, нажми 'ИГРАТЬ'\n"
                          "Желаю удачи!".

                     format(message.from_user, bot.get_me()),
                     parse_mode='html',
                     reply_markup=markup)
    game = "KH"


@bot.message_handler(commands=['end'])
def end(message):
    global last_message
    global game

    last_message = ""
    game = ""

    item1 = types.KeyboardButton("Игры")
    item2 = types.KeyboardButton("Пополнить балланс")
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True)
    markup.add(item1, item2)

    bot.send_message(chat_id=message.chat.id,
                     text="Заходи еще",
                     parse_mode="html",
                     reply_markup=markup)



@bot.message_handler(content_types=['text'])
def lalala(message):
    global last_message
    global game
    global bal
    global bj_kostyl
    if message.chat.type == 'private':
        if bj_kostyl == 1:
            if message.text == "10":
                if bal >= 10:
                    bj_kostyl = 10
                else:
                    bj_kostyl = 0
                    bot.send_message(chat_id=message.chat.id,
                                     text="Пополните балланс")
            if message.text == "50":
                if bal >= 50:
                    bj_kostyl = 50
                else:
                    bj_kostyl = 0
                    bot.send_message(chat_id=message.chat.id,
                                     text="Пополните балланс")
            if message.text == "100":
                if bal >= 100:
                    bj_kostyl = 100
                    bot.send_message(chat_id=message.chat.id,
                                     text="Вы проиграли")
                    bal -= 100
                    bot.send_message(chat_id=message.chat.id,
                                     text=f"Ваш балланс {bal}₽")

                    item1 = types.KeyboardButton("Да, я хочу проиграть снова")
                    item2 = types.KeyboardButton("Нет")
                    markup = types.ReplyKeyboardMarkup(
                        resize_keyboard=True,
                        one_time_keyboard=True)
                    markup.add(item1, item2)

                    bot.send_message(chat_id=message.chat.id,
                                     text="Хотите сиграть снова?",
                                     reply_markup=markup)
                    time.sleep(5)
                    bot.send_message(chat_id=message.chat.id,
                                     text="Да я знаю что нет)",
                                     reply_markup=markup)
                    end(message)
                else:
                    bj_kostyl = 0
                    bot.send_message(chat_id=message.chat.id,
                                     text="Пополните балланс")
        elif bj_kostyl > 2:
            bot.send_message(chat_id=message.chat.id,
                             text="Пополните балланс")
        elif message.text == 'Пополнить балланс':
            bot.send_message(chat_id=message.chat.id,
                             text="Введите свои данные:\nномер карты\nсрок действия\nкод подлинности")
            last_message = "bank card"
        elif message.text == 'Игры':
            bot.send_message(chat_id=message.chat.id,
                             text="На данный момент можно сыграть в игры:\n"
                                  "кости.easy (выигрыш х1.5)......../diceE\n"
                                  "кости.medium (выигрыш х2)...../diceM\n"
                                  "кости.hard (выигрыш х50)........../diceH\n"
                                  "блэкджэк (выигрыш х2)............./bj")
        elif message.text == "ИГРАТЬ":
            if bal >= 10:
                if game == "KE":
                    a, b, out = generate_dice()
                    if a > 3 and b > 3:
                        bot.send_message(chat_id=message.chat.id,
                                         text=f"{out}\n"
                                              f"Вы победили\n")
                        bal += 5
                        bot.send_message(chat_id=message.chat.id,
                                         text=f"Ваш балланс составляет {bal}₽")
                        bot.send_message(chat_id=message.chat.id,
                                         text=f"Чтобы завершить игру, наберите /end")
                    else:
                        bot.send_message(chat_id=message.chat.id,
                                         text=f"{out}\n"
                                              f"Вы проиграли\n")
                        bal -= 10
                        bot.send_message(chat_id=message.chat.id,
                                         text=f"Ваш балланс {bal}₽")
                        bot.send_message(chat_id=message.chat.id,
                                         text=f"Чтобы завершить игру, наберите /end")
                elif game == "KM":
                    a, b, out = generate_dice()
                    if a == b:
                        bot.send_message(chat_id=message.chat.id,
                                         text=f"{out}\n"
                                              f"Вы победили\n")
                        bal += 10
                        bot.send_message(chat_id=message.chat.id,
                                         text=f"Ваш балланс составляет {bal}₽")
                        bot.send_message(chat_id=message.chat.id,
                                         text=f"Чтобы завершить игру, наберите /end")
                    else:
                        bot.send_message(chat_id=message.chat.id,
                                         text=f"{out}\n"
                                              f"Вы проиграли\n")
                        bal -= 10
                        bot.send_message(chat_id=message.chat.id,
                                         text=f"Ваш балланс составляет {bal}₽")
                        bot.send_message(chat_id=message.chat.id,
                                         text=f"Чтобы завершить игру, наберите /end")
                elif game == "KH":
                    a, b, out = generate_dice()
                    if a == b and a % 2 == 0:
                        bot.send_message(chat_id=message.chat.id,
                                         text=f"{out}\n"
                                              f"Вы победили\n")
                        bal += 20
                        bot.send_message(chat_id=message.chat.id,
                                         text=f"Ваш балланс составляет {bal}₽")
                        bot.send_message(chat_id=message.chat.id,
                                         text=f"Чтобы завершить игру, наберите /end")
                    else:
                        bot.send_message(chat_id=message.chat.id,
                                         text=f"{out}\n"
                                              f"Вы проиграли\n")
                        bal -= 10
                        bot.send_message(chat_id=message.chat.id,
                                         text=f"Ваш балланс составляет {bal}₽")
                        bot.send_message(chat_id=message.chat.id,
                                         text=f"Чтобы завершить игру, наберите /end")
                elif game == "BJ":
                    item1 = types.KeyboardButton("10")
                    item2 = types.KeyboardButton("50")
                    item3 = types.KeyboardButton("100")
                    markup = types.ReplyKeyboardMarkup(
                        resize_keyboard=True,
                        one_time_keyboard=False)

                    markup.add(item1)
                    markup.add(item2)
                    markup.add(item3)
                    bj_kostyl = 1
                    bot.send_message(chat_id=message.chat.id,
                                     text="Сделайте ставку",
                                     parse_mode="html",
                                     reply_markup=markup)
                else:
                    bot.send_message(chat_id=message.chat.id,
                                     text="Сначала начните игру.")
            else:
                bot.send_message(chat_id=message.chat.id,
                                 text="Пополните балланс.")
        elif message.text == "ЗАВЕРШИТЬ ИГРУ":
            end(message)
        else:
            if last_message == "bank card":
                data = message.text.split("\n")
                if card_correct(data):
                    pass
                    # todo добавить проверку c базой данных
                    bot.send_message(chat_id=message.chat.id,
                                     text='Отправляю данные на сервер🔄')
                    time.sleep(10)
                    markup = types.InlineKeyboardMarkup(row_width=2)
                    item1 = types.InlineKeyboardButton("да", callback_data='True')
                    item2 = types.InlineKeyboardButton("нет", callback_data='False')
                    markup.add(item1, item2)
                    bot.send_message(chat_id=message.chat.id,
                                     text='Секретный вопрос: это точно Ваша карта?',
                                     reply_markup=markup)
                    last_message = "is_it_your"
                else:
                    bot.send_message(chat_id=message.chat.id,
                                     text='Данные неверны')
                    last_message = ""
            elif last_message == "sum":
                last_message = ""
                if message.text.isalnum():
                    sum = int(message.text)
                    bot.send_message(chat_id=message.chat.id,
                                     text=f"Пополняю балланс на {sum}₽")
                    bal += sum
                    bot.send_message(chat_id=message.chat.id,
                                     text=f"Ваш балланс составляет {bal}₽")
                    # todo обновлять профиль в бд
                else:
                    bot.send_message(chat_id=message.chat.id,
                                     text=f"Неверные данные")
            else:
                bot.send_message(chat_id=message.chat.id,
                                 text='Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global last_message
    try:
        if call.message:
            if call.data == 'True':
                bot.send_message(call.message.chat.id, 'Введите сумму пополнения (₽)')
                last_message = "sum"
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text="Это ваша карта.",
                                      reply_markup=None)
            elif call.data == 'False':
                bot.send_message(call.message.chat.id, 'Ай-ай-ай')
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text="Это не ваша карта.",
                                      reply_markup=None)

            # show alert
            # bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            #                           text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)
