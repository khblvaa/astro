import random
import telebot
import webbrowser
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import date

bot = telebot.TeleBot('7396494559:AAHLPkmvDSyll8NXD5UW9dfifKUmYe1fRBo')
h = False
user_state = {}
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Меню 🌠", callback_data="pressed")
    markup.add(button)
    first_name = message.from_user.first_name or ''
    last_name = message.from_user.last_name or ''
    bot.send_message(message.chat.id, f'Привет, <em>{first_name} {last_name}</em> ! \nХочешь узнать твой гороскоп на сегодня? 🔮 \nИли хочешь чтобы я, основываясь на знаки свыше, выбрал бы для тебя идеального героя, позицию или сразу предсказал бы тебе всю команду? \nЕсли да, жди кнопку Меню, чтобы узнать про все возможности бота!\n\n(Пока что бот разговаривает только на русском) \n\nДоступные команды: \n/start - Жми, если хочешь перезапустить бота \n/dox - Жми, если хочешь докс\n/website - Жми, если плохо получается играть в доту и твои тимейты тебя ненавидят', parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "pressed")
def handle_button(call):
    bot.answer_callback_query(call.id)
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("Гороскоп на сегодня", callback_data="horoscope")
    btn2 = InlineKeyboardButton("Кого мне пикнуть", callback_data="hero")
    btn3=InlineKeyboardButton("Оценю твою фоточку от 1 до 10", callback_data="foto")
    btn4=InlineKeyboardButton("<UNK> <UNK> <UNK>", callback_data="back2")
    markup.row(btn3)
    markup.row(btn1, btn1)
    bot.send_message(call.message.chat.id, "Что ты хочешь узнать от бота сегодня?🎉", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "horoscope")
def handle_horoscope(call):
    user_state[call.from_user.id] = 'waiting_for_sign'
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Напиши свой знак зодиака:")

@bot.message_handler(commands=['dox'])
def dox(message):
    bot.send_message(message.chat.id, f'Жди докс: \n {message.from_user}! ')

@bot.message_handler(commands=['website'])
def website(message):
    bot.send_message(message.chat.id, 'https://www.leagueoflegends.com/ru-ru/download/')

@bot.message_handler()
def znak(message):
    user_id = message.from_user.id
    if user_state.get(user_id) != 'waiting_for_sign':
        return
    text = message.text.lower()
    horo = {'овен': "♈ <b>Овен</b>\n\nСегодня ты — как Сларк с Shadow Blade: хочешь прыгнуть, но не уверен, выживешь ли. Думай, прежде чем прыгать. Даже в драку.\n\n<b>Совет:</b> Не агри Рошана в соло — сначала проверь, есть ли команда.",

        'телец': "♉ <b>Телец</b>\n\nТы как Акслотл с Vanguard — стоишь, танкуешь, молчишь. Но не забывай: даже самым стойким нужен хил. Не тащи всё в одиночку.\n\n<b>Совет:</b> Не иди в файт без саппорта — и в жизни тоже.",

        'близнецы': "♊ <b>Близнецы</b>\n\nСегодня ты как Meepo: везде и сразу. Только бы не рассыпаться. Концентрируйся хотя бы на одной задаче — и шанс на победу вырастет.\n\n<b>Совет:</b> Не бери больше, чем можешь вытянуть.",

        'рак': "♋ <b>Рак</b>\n\nТы как Tidehunter без ульта — все ждут твоего момента, а ты не готов. Не бойся надавить Ravage в нужный момент — время пришло.\n\n<b>Совет:</b> Иногда надо врываться первым, не дожидаясь пинга.",

        'лев': "♌ <b>Лев</b>\n\nТы как Лион с Aghanim — много шума, много пальцев, и все боятся. Главное — не прожигай ману на ерунду. И не пытайся быть мидером в каждой катке жизни.\n\n<b>Совет:</b> Меньше болтай, больше дизейбль.",

        'дева': "♍ <b>Дева</b>\n\nТы как Котл в душе — хочешь помогать, но все называют 'крысой'. Не обращай внимания, твой свет освещает путь даже через тьму флейма.\n\n<b>Совет:</b> Не забывай заряжать чакру доброты.",

        'весы': "♎ <b>Весы</b>\n\nСегодня ты — как Рубик: хочешь украсть чужие идеи и сделать лучше. У тебя даже получается! Только не забудь — своя игра важнее.\n\n<b>Совет:</b> Используй украденное с умом, а не ради фана.",

        'скорпион': "♏ <b>Скорпион</b>\n\nТы как Никс: всех бесишь, но эффективно. Главное — не переборщи со стелсом, а то забудут, что ты вообще в команде.\n\n<b>Совет:</b> Иногда выйти из инвиза — тоже победа.",

        'стрелец': "♐ <b>Стрелец</b>\n\nСегодня ты как Windranger: либо попадёшь, либо все мимо. Не надейся только на удачу — возьми в руки мышку и начни целиться серьёзно.\n\n<b>Совет:</b> Даже если 3 стрелы подряд не попали — четвёртая может быть критом.",

        'козерог': "♑ <b>Козерог</b>\n\nТы — как Underlord: хочешь всё контролировать, но команда не слушает. Не злись, просто старайся не открывать портал в тильт.\n\n<b>Совет:</b> Иногда полезно не тянуть всех за собой, а дать им самим нажать ТП.",

        'водолей': "♒ <b>Водолей</b>\n\nСегодня ты — как Пудж без хука: вроде и на месте, но чего-то не хватает. Не врывайся в тильт — собери терпение и аркан бутсы.\n\n<b>Совет:</b> Не пикай в шутку — жизнь тоже ранжовая.",

        'рыбы': "♓ <b>Рыбы</b>\n\nТы как Naga Siren: умеешь усыпить всех, кроме себя. Хочешь помочь — и правда можешь, но не забудь про себя в этой суете.\n\n<b>Совет:</b> Пой песню своей души — даже если тебя мьютят в чате."}
    for key in horo:
        if text == key:
            bot.reply_to(message, "Прогноз на " + date.day() +"\n\n" +horo[key], parse_mode='html')
            user_state[user_id] = None
            return
    bot.send_message(message.chat.id, "Я не совсем понял, напиши пожалуйста свой знак зодиака", parse_mode='html')
bot.infinity_polling()
