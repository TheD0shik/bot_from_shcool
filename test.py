import telebot
import time

print("бот запущен")
bot=telebot.TeleBot('7275570077:AAG-1zXrTJ_Lrt3GDmvpWlYdJwUU9L30fMQ') 
@bot.message_handler(commands=['start'])
def main(message):
    now = time.time()
    user_name = message.from_user.username
    user_id = message.from_user.id
    print(f'{time.ctime(now)}|{user_id}|{user_name}')
    bot.send_message(message.chat.id,'бот на техобслуживании до 14.10')

@bot.message_handler(func=lambda message: True)
def handle(message):
    now = time.time()
    user_name = message.from_user.username
    user_id = message.from_user.id
    m=message.text
    bot.send_message(message.chat.id,'бот на техобслуживании до 14.10')
    print(f'{time.ctime(now)}|{user_id}|{user_name}|{m}')
    
nnn=1
while nnn==1:
    try:
        bot.infinity_polling()
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(15)