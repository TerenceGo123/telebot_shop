
from telebot import *
import sqlite3
from dotenv import dotenv_values

config = dotenv_values('.env')
bot = telebot.TeleBot(config.get('TOKEN'))


@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("К покупкам!", callback_data='shop')
    markup.add(button1)
    bot.send_message(message.chat.id, f"Добрый день, {name}! Приступайте к покупкам!)", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:call.data=='shop')
def callback_menu(call):
  if call.data == 'shop':
    markup = types.InlineKeyboardMarkup()
    button2 = types.InlineKeyboardButton("Меню", callback_data='menu')
    button3 = types.InlineKeyboardButton("Корзина", callback_data='drink')
    button4 = types.InlineKeyboardButton("Отзывы", url='https://google.com')
    button5 = types.InlineKeyboardButton("sqlite", callback_data='sqlite')
    markup.add(button2, button3, button4, button5)
    bot.send_photo(call.message.chat.id, 'https://i.postimg.cc/jC00fyct/image.png', caption="ВЫБЕРИТЕ", reply_markup=markup)

# BACK MENU
@bot.callback_query_handler(func=lambda call:call.data=='back1')
def callback_menu(call):
  if call.data == 'back1':
    markup = types.InlineKeyboardMarkup()
    button2 = types.InlineKeyboardButton("Меню", callback_data='menu')
    button3 = types.InlineKeyboardButton("Корзина", callback_data='drink')
    button4 = types.InlineKeyboardButton("Отзывы", url='https://google.com')
    button5 = types.InlineKeyboardButton("sqlite", callback_data='sqlite')
    markup.add(button2, button3, button4, button5)
    bot.send_photo(call.message.chat.id, 'https://i.postimg.cc/jC00fyct/image.png', caption="ВЫБЕРИТЕ", reply_markup=markup)

# @bot.callback_query_handler()
# def answer(call):
#     if call.data == 'shop':
#         bot.send_message(call.chat.id, 'Hello')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
  if call.data == "sqlite":
    id = call.from_user.id
    name = call.from_user.first_name
    print(f'{id}: {name} запросил меню')
    connection = sqlite3.connect(config.get('DB'))
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM items''')
    tovar = cursor.fetchall()
    connection.close()
#     msg = ''
#     for i in tovar: 
#         msg += str(i) + '\n'
#     bot.send_message(call.from_user.id, msg)

@bot.callback_query_handler(func=lambda call:call.data=='menu')
def callback_menu(call):
  if call.data == 'menu':
    markup = types.InlineKeyboardMarkup()
    button2 = types.InlineKeyboardButton("Горячее", callback_data='hot')
    button3 = types.InlineKeyboardButton("Напитки", callback_data='drink')
    button4 = types.InlineKeyboardButton("Закуски", callback_data='snacks')
    button1 = types.InlineKeyboardButton("Назад", callback_data='back1')
    markup.add(button2, button3, button4, button1)
    bot.send_photo(call.message.chat.id, 'https://i.postimg.cc/zDW87M17/image.png', caption="ВОТ НАШЕ МЕНЮ", reply_markup=markup)

# BACK MENU
@bot.callback_query_handler(func=lambda call:call.data=='back4')
def callback_menu(call):
  if call.data == 'back4':
    markup = types.InlineKeyboardMarkup()
    button2 = types.InlineKeyboardButton("Горячее", callback_data='hot')
    button3 = types.InlineKeyboardButton("Напитки", callback_data='drink')
    button4 = types.InlineKeyboardButton("Закуски", callback_data='snacks')
    button1 = types.InlineKeyboardButton("Назад", callback_data='back1')
    markup.add(button2, button3, button4, button1)
    bot.send_photo(call.message.chat.id, 'https://i.postimg.cc/zDW87M17/image.png', caption="ВОТ НАШЕ МЕНЮ", reply_markup=markup)

# CHIIIPS
@bot.callback_query_handler(func=lambda call:call.data=='snacks')
def callback_categoty(call):
  if call.data == 'snacks':
    name = call.from_user.first_name
    msg = 'ВОТ ЧТО ЕСТЬ ИЗ ЗАКУСОК:'
    markup = types.InlineKeyboardMarkup()
    button2 = types.InlineKeyboardButton("Пивная тарелка", callback_data='bear+')
    button3 = types.InlineKeyboardButton("Вяленная говядина", callback_data='meat+')
    button4 = types.InlineKeyboardButton("Чипсы", callback_data='chips')
    button5 = types.InlineKeyboardButton("Назад", callback_data='back4')
    markup.add(button2, button3, button4, button5)
    bot.send_message(call.message.chat.id, f"{name}, {msg}", reply_markup=markup)


# BACK CHIPS
@bot.callback_query_handler(func=lambda call:call.data=='back2')
def callback_categoty(call):
  if call.data == 'back2':
    name = call.from_user.first_name
    msg = 'ВОТ ЧТО ЕСТЬ ИЗ ЗАКУСОК:'
    markup = types.InlineKeyboardMarkup()
    button2 = types.InlineKeyboardButton("Пивная тарелка", callback_data='bear+')
    button3 = types.InlineKeyboardButton("Вяленная говядина", callback_data='meat+')
    button4 = types.InlineKeyboardButton("Чипсы", callback_data='chips')
    button5 = types.InlineKeyboardButton("Назад", callback_data='back4')
    markup.add(button2, button3, button4, button5)
    bot.send_message(call.message.chat.id, f"{name}, {msg}", reply_markup=markup)


@bot.callback_query_handler(func=lambda call:call.data=='bear+')
def callback_categoty(call):
  if call.data == 'bear+':
    markup = types.InlineKeyboardMarkup()
    button3 = types.InlineKeyboardButton("Купить за 150р", callback_data='soup')
    button1 = types.InlineKeyboardButton("Назад", callback_data='back2')
    markup.add(button3, button1)
    bot.send_photo(call.message.chat.id, 'https://baltrest.ru/upload/iblock/5b3/MG_3163-_2_.jpg', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:call.data=='meat+')
def callback_categoty(call):
  if call.data == 'meat+':
    markup = types.InlineKeyboardMarkup()
    button3 = types.InlineKeyboardButton("Купить за 250р", callback_data='soup')
    button1 = types.InlineKeyboardButton("Назад", callback_data='back2')
    markup.add(button3, button1)
    bot.send_photo(call.message.chat.id, 'https://discount-h.ru/upload/iblock/stati/Dieta-Anityi-TSoy-84.jpg', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:call.data=='chips')
def callback_categoty(call):
  if call.data == 'chips':
    markup = types.InlineKeyboardMarkup()
    button3 = types.InlineKeyboardButton("Купить за 100р", callback_data='soup')
    button1 = types.InlineKeyboardButton("Назад", callback_data='back2')
    markup.add(button3, button1)
    bot.send_photo(call.message.chat.id, 'https://masterpiecer-images.s3.yandex.net/e6c81fd96f1411eeaab02aacdc0146ad:upscaled', reply_markup=markup)

# DRIIIIIIINK
@bot.callback_query_handler(func=lambda call:call.data=='drink')
def callback_categoty(call):
  if call.data == 'drink':
    name = call.from_user.first_name
    msg = 'ВОТ ЧТО ЕСТЬ ИЗ НАПИТКОВ:'
    markup = types.InlineKeyboardMarkup()
    button2 = types.InlineKeyboardButton("Пиво", callback_data='bear')
    button3 = types.InlineKeyboardButton("Чай/Кофе", callback_data='tea/coffe')
    button4 = types.InlineKeyboardButton("Крепкий алкоголь", callback_data='alcogol')
    button1 = types.InlineKeyboardButton("Назад", callback_data='back2')
    markup.add(button2, button3, button4)
    bot.send_message(call.message.chat.id, f"{name}, {msg}", reply_markup=markup)

# BACK DRINK
@bot.callback_query_handler(func=lambda call:call.data=='back5')
def callback_categoty(call):
  if call.data == 'back5':
    name = call.from_user.first_name
    msg = 'ВОТ ЧТО ЕСТЬ ИЗ НАПИТКОВ:'
    markup = types.InlineKeyboardMarkup()
    button2 = types.InlineKeyboardButton("Пиво", callback_data='bear')
    button3 = types.InlineKeyboardButton("Чай/Кофе", callback_data='tea/coffe')
    button4 = types.InlineKeyboardButton("Крепкий алкоголь", callback_data='alcogol')
    button1 = types.InlineKeyboardButton("Назад", callback_data='back2')
    markup.add(button2, button3, button4, button1)
    bot.send_message(call.message.chat.id, f"{name}, {msg}", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:call.data=='bear')
def callback_categoty(call):
  if call.data == 'bear':
    markup = types.InlineKeyboardMarkup()
    button3 = types.InlineKeyboardButton("Купить за 100р", callback_data='soup')
    button1 = types.InlineKeyboardButton("Назад", callback_data='back5')
    markup.add(button3, button1)
    bot.send_photo(call.message.chat.id, 'https://img.freepik.com/premium-photo/beer-pouring-into-glass-bottle-on-the-table-in-pub-or-bar-beautiful-bokeh-lights_860978-540.jpg', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:call.data=='tea/coffe')
def callback_categoty(call):
  if call.data == 'tea/coffe':
    markup = types.InlineKeyboardMarkup()
    button3 = types.InlineKeyboardButton("Купить за 70р", callback_data='soup')
    button1 = types.InlineKeyboardButton("Назад", callback_data='back5')
    markup.add(button3, button1)
    bot.send_photo(call.message.chat.id, 'https://devgreen.lenta.com/upload/iblock/251/hvtp60r1ed4hxk2nsrs7boqx511udn2a.jpg', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:call.data=='alcogol')
def callback_categoty(call):
  if call.data == 'alcogol':
    markup = types.InlineKeyboardMarkup()
    button3 = types.InlineKeyboardButton("Купить за 1000р", callback_data='soup')
    button1 = types.InlineKeyboardButton("Назад", callback_data='back5')
    markup.add(button3, button1)
    bot.send_photo(call.message.chat.id, 'https://vikupvin.ru/wp-content/uploads/2020/06/vikupvin_ru-26-06-2020-011.jpg', reply_markup=markup)



# HOOOOOOOT
@bot.callback_query_handler(func=lambda call:call.data=='hot')
def callback_categoty(call):
  if call.data == 'hot':
    name = call.from_user.first_name
    msg = 'ВОТ ЧТО ЕСТЬ ГОРЯЧЕЕ:'
    markup = types.InlineKeyboardMarkup()
    button2 = types.InlineKeyboardButton("Суп", callback_data='soup')
    button3 = types.InlineKeyboardButton("Стрейк", callback_data='steak')
    button4 = types.InlineKeyboardButton("Рыба", callback_data='fish')
    button1 = types.InlineKeyboardButton("Назад", callback_data='back2')
    markup.add(button2, button3, button4, button1)
    bot.send_message(call.message.chat.id, f"{name}, {msg}", reply_markup=markup)


# HOT BACK
@bot.callback_query_handler(func=lambda call:call.data=='hot_back')
def callback_categoty(call):
  if call.data == 'hot_back':
    name = call.from_user.first_name
    msg = 'ВОТ ЧТО ЕСТЬ ГОРЯЧЕЕ:'
    markup = types.InlineKeyboardMarkup()
    button2 = types.InlineKeyboardButton("Суп", callback_data='soup')
    button3 = types.InlineKeyboardButton("Стрейк", callback_data='steak')
    button4 = types.InlineKeyboardButton("Рыба", callback_data='fish')
    button1 = types.InlineKeyboardButton("Назад", callback_data='back2')
    markup.add(button2, button3, button4, button1)
    bot.send_message(call.message.chat.id, f"{name}, {msg}", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:call.data=='soup')
def callback_categoty(call):
  if call.data == 'soup':
    markup = types.InlineKeyboardMarkup()
    button3 = types.InlineKeyboardButton("Купить за 300р", callback_data='soup')
    button_back = types.InlineKeyboardButton("Назад", callback_data='hot_back')
    markup.add(button3, button_back)
    bot.send_photo(call.message.chat.id, 'https://n1s1.hsmedia.ru/4b/d5/7d/4bd57defc7847a00268ecd5425ffc28b/1000x745_0xac120003_11690543061562649847.jpg', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:call.data=='steak')
def callback_categoty(call):
  if call.data == 'steak':
    markup = types.InlineKeyboardMarkup()
    button3 = types.InlineKeyboardButton("Купить за 700р", callback_data='soup')
    button_back = types.InlineKeyboardButton("Назад", callback_data='hot_back')
    markup.add(button3, button_back)
    bot.send_photo(call.message.chat.id, 'https://img.freepik.com/premium-photo/the-best-looking-steak-in-the-entire-world-it-is-perfectly-seasoned-and-had-a-delicious-looking-sauce-on-it_812426-5422.jpg', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:call.data=='fish')
def callback_categoty(call):
  if call.data == 'fish':
    markup = types.InlineKeyboardMarkup()
    button3 = types.InlineKeyboardButton("Купить за 500р", callback_data='soup')
    button_back = types.InlineKeyboardButton("Назад", callback_data='hot_back')
    markup.add(button3, button_back)
    bot.send_photo(call.message.chat.id, 'https://food.pibig.info/uploads/posts/2023-03/1679665417_food-pibig-info-p-goryachie-ribnie-blyuda-oboi-1.jpg', reply_markup=markup)

bot.polling(none_stop=True, interval=0)

























