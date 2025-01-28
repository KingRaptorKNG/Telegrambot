import telebot
import random
from telebot.types import Message
from config import TOKEN

class Plane:
    def __init__(self, name:str, max_count:int, plane_type:str, count=0):
        self.name = name
        self.max_count = max_count
        self.plane_type = plane_type
        self.count = count
    
    def info(self, msg):
        bot.send_message(msg.chat.id, f'Самолёт {self.name} с {self.count} пассажирами, тип самолёта: {self.plane_type}. ')

Jokes = ['Скажите, пожалуйста, сколько будет дважды два? Четыре, - отвечает оператор. Ой, как здорово! А я все время думала, что пять!',
'А почему у зайца длинные уши? Чтобы лучше слышать, - отвечает учитель. А почему у тебя такие большие уши? Чтобы лучше слушать такие глупые вопросы!',
'Доктор, у меня двойное зрение! Ну, так закройте один глаз. А если я закрою оба? Тогда вы вообще ничего не увидите!',
'Идет слон по джунглям, видит — обезьяна висит на лиане. Слон и говорит: Эй, обезьяна, слезь, я тебя съем! Обезьяна ему в ответ: Да ты что, слон, я с дерева спрыгну, ты меня все равно не догонишь! Слон подумал и говорит: Ну, ладно, не буду тебя есть, просто обидно будет, если ты упадешь и разобьешься.',
'Сидят два крокодила на болоте... Один другому говорит: Слушай, а ты когда-нибудь пробовал ананас? Нет, а что такое ананас? Ну, это такой фрукт, жёлтый, круглый... Ага, понял, как арбуз, только зелёный!',
'Приходит мужик к врачу и жалуется: Доктор, у меня бессонница. Лечусь уже неделю, а заснуть не могу. Врач: Ну, давайте попробуем так: ляжете в кровать, закроете глаза и будете считать овец. Через неделю мужик приходит весь измученный: Доктор, я посчитал всех овец в мире, всех коз, свиней... И все равно не могу заснуть! Врач: Ну, тогда попробуйте посчитать бухгалтеров. Мужик: Доктор, вы гений! Я заснул уже на втором!',
'Муж приходит домой и спрашивает жену: Дорогая, ты меня любишь? Жена откладывает книгу и с улыбкой отвечает: Конечно, любимый! Как же я могу тебя не любить? Муж: А почему тогда ты вчера в анкете написала, что замужем за миллионером?']

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def startcommand(msg: Message):
    bot.reply_to(msg, 'Привет')
    bot.send_message(msg.chat.id, 'Как дела?')


@bot.message_handler(content_types=['photo'])
def photocommand(msg: Message):
    bot.send_message(msg.chat.id, 'Классное фото!!')


@bot.message_handler(commands=['joke'])
def echo_message(msg: Message):
    bot.reply_to(msg, random.choice(Jokes))


@bot.message_handler(commands=['plane'])
def echo_message(msg: Message):
    args = telebot.util.extract_arguments(msg.text).split()
    if len(args) >= 3 or len(args) <= 4:
            try:
                name = str(args[0])
                max_count = int(args[1])
                plane_type = str(args[2])
                try:
                    count = int(args[3])
                except IndexError:
                    count = 0
                if max_count <= count:
                    bot.send_message(msg.chat.id, f'Максимальное число пассажиров не может быть меньше общего числа пассажиров!')
                else: 
                    plane = Plane(name, max_count, plane_type, count)
                    #bot.send_message(msg.chat.id, f'Самолёт {plane.name} с {plane.count} пассажирами, тип самолёта: {plane_type}, число пассажиров {plane.count} ')
                    plane.info(msg)
            except ValueError:
                bot.send_message(msg.chat.id, f'Введите данные корректно! Название, Максимальное число пассажиров, Тип самолёта, Число пассажиров')
    else:
        bot.send_message(msg.chat.id, 'Название, Максимальное число пассажиров, Тип самолёта, Число пассажиров')
            


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text) 


@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'Добро пожаловать новый пользователь!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)














bot.infinity_polling()