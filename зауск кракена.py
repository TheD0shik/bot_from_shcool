import telebot
import time
import re
import config
import datetime
import gptt 
from gptt import gchat
from telebot import types
from telebot.types import InputFile
rass=[]
m="f" 
rere=-1
uses=0
ms=[]
mark = types.InlineKeyboardMarkup() 
g0=''
g1=''
g2=''
dz = ""
g3=''
day=''
b=['','','','','','','']
bot=telebot.TeleBot('7275570077:AAG-1zXrTJ_Lrt3GDmvpWlYdJwUU9L30fMQ')
pattern = r'(.*)-<"(.*?)">'
patternto = r'(\w+)\|(\w+)\|(\w+)_(\w+)'
print("запуск бота...")

for i, line in enumerate(config.dop):
    
    print(i)
    f = types.InlineKeyboardButton(text=line, callback_data=line)
    b[i] = f
    
    mark.add(b[i])
#match = re.search(r'(\w+)-<"(\w+)">', text)
#match.group(2)

ress = datetime.date.today()
too = ress + datetime.timedelta(days=1)
to=too.weekday()
res=ress.weekday()
def z(g):
    if(g==1):
        return config.Tuesday
    elif(g==2):
        return config.Wednesday
    elif(g==3):
        return config.Thursday
    elif(g==4):
        return config.Friday
    elif(g==5):
        return config.Saturday
    else:
        return config.Monday
def chek(chat,qwe):
    print(qwe)
    dz = ""
    with open("log.txt", "r+", encoding='utf-8') as log:
                lines = log.readlines() 
                for ele in qwe:
                    for i, line in enumerate(lines):
                    
                        matchh = re.search(pattern, line)
                        g2 = matchh.group(1)
                        g3 = matchh.group(2)
                        if ele == g2:
                            dz=dz+line+"\n"
    bot.send_message(chat,f'актуальное домашнее задание по расписанию на указаный день:\n{dz}')
                     

def unu(mes,mss,mm):
    global rere,ms
  
    ms=mss
   
    ii = ms[rere]

    bot.send_message(mes, ii) 
    with open("log.txt", "r+", encoding='utf-8') as log:
                lines = log.readlines() 
                log.seek(0)  
                for i, line in enumerate(lines):
                    matchh = re.search(pattern, line)
                    g2 = matchh.group(1)
                    g3 = matchh.group(2)
                    print(f'{ii}|{g2}')
                    if ii == g2:
                        m=f'{g2}-<"{mm}">'
                        lines[i] = m + "\n"

                        log.writelines(lines) 
                        break
    rere=rere+1
    if rere >= len(ms):
        bot.send_message(mes, 'усе') 
        rere=-1
    else:
        ii = ms[rere]
        bot.send_message(mes, ii)

    
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    rrr = rf'C:\Users\LEGION\Desktop\бот для шкилы\доп_материал\{callback.data}'
    print(rrr)
    message = bot.send_document(callback.message.chat.id, open(rrr, 'rb'))
    file_id = message.document.file_id
    file_info = bot.get_file(file_id)
    file_url = f'https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}'
    print(file_url)
    bot.send_document(callback.message.chat.id, file_url)


@bot.message_handler(commands=['start'])
def main(message):
    now = time.time()
    user_name = message.from_user.username
    user_id = message.from_user.id
    print(f'{time.ctime(now)}|{user_id}|{user_name}')
    bot.send_message(message.chat.id,'инструкция: \n(команды просто писать как обычное соо) \n"дз"-вывести все дз\n"дз на(день недели|завтра|сегодня)"- вывести актуальное дз только предметов на указаный день недели\n"доп материалы"-выводит дополнительные материалы')


@bot.message_handler(commands=['reg'])
def main(message):
    bot.send_message(message.chat.id,'для регистрации напишите "регистрация:" \nа затем напишите\nимя_фамилия\nпробелов после "регистрация:" нЭт')

@bot.message_handler(func=lambda message: True)
def handle(message):
    now = time.time()
    global mark,uses,rere
    user_name = message.from_user.username
    user_id = message.from_user.id
    m=message.text
    lg=f'{time.ctime(now)}|{user_id}|{user_name}|{m}'
    print(lg)
    with open("logs.txt", "a+",encoding='utf-8') as logs:
        logs.write(f"{str(lg)}\n")
        logs.close
    if 'чат гпт' in m.lower():
        m = m.replace('чат гпт', '', 1)
        
        bot.send_message(message.chat.id,gchat(m))
        
        
        
    elif 'дз' in m.lower():
        m = m.replace('дз', '', 1)
        if 'добавить' in m.lower():
            if 'с заменой на' in m.lower():
                m = m.replace('с заменой на', '', 1)
                if 'завтра' in m.lower():
                    m = m.replace('завтра', '', 1)
                    day = datetime.date.today().weekday()+1
                elif 'сегодня' in m.lower():
                    m = m.replace('сегодня', '', 1)
                    day = datetime.date.today().weekday()
                elif 'понедельник' in m.lower():
                    m = m.replace('понедельник', '', 1)
                    day = 0
                elif 'вторник' in m.lower():
                    m = m.replace('вторник', '', 1)
                    day = 1
                elif 'среду' in m.lower():
                    m = m.replace('среду', '', 1)
                    day = 2
                elif 'четверг' in m.lower():
                    m = m.replace('четверг', '', 1)
                    day = 3
                elif 'пятницу' in m.lower():
                    m = m.replace('пятницу', '', 1)
                    day = 4
                elif 'субботу' in m.lower():
                    m = m.replace('субботу', '', 1)
                    day = 5
                else:
                    bot.send_message(message.chat.id,f'неверный день недели')
                uses=user_id
                unu(message.chat.id,z(day),m)
            else:
                m = m.replace('добавить', '', 1)
                match = re.search(pattern, m)
                print(m)
                g0=match.group(1)
                g1=match.group(2)
                f=1
                n=0
            
                print('g')
                with open("log.txt", "r+", encoding='utf-8') as log:
                    lines = log.readlines() 
                    log.seek(0)  
                    for i, line in enumerate(lines):
                    
                        matchh = re.search(pattern, line)
                        g2 = matchh.group(1)
                        g3 = matchh.group(2)
                        print(f'{g0}|{g2}')
                        if g0 == g2:
                            print(0)
                            lines[i] = m + "\n" 
                            bot.send_message(message.chat.id, 'домашнее задание обновлено')
                            log.writelines(lines) 
                            break
        elif ' на ' in m.lower():
            m = m.replace('на', '', 1)
            if 'завтра' in m.lower():
                day = datetime.date.today().weekday()+1
            elif 'сегодня' in m.lower():
                day = datetime.date.today().weekday()
            elif 'понедельник' in m.lower():
                day = 0
            elif 'вторник' in m.lower():
                day = 1
            elif 'среду' in m.lower():
                day = 2
            elif 'четверг' in m.lower():
                day = 3
            elif 'пятницу' in m.lower():
                day = 4
            elif 'субботу' in m.lower():
                day = 5
            else:
                bot.send_message(message.chat.id,f'неверный день недели')
                
            print (day)
            
            rass=z(day)
            chek(message.chat.id,rass)
                
                
        else:
            with open("log.txt", "r",encoding='utf-8') as log:
                bot.send_message(message.chat.id,log.read())
                log.close
    elif 'регистрация:' in m.lower():
        m = m.replace('регистрация:', '', 1)
        if " " in m.lower():
            bot.send_message(message.chat.id,f'сказали же, пробела нЭт')
        else:
            if "_" in m.lower():
                if (m.lower()=="_" or m.lower()=="имя_фамилия"):
                    bot.send_message(message.chat.id,f'-_-')
                else:
                    
                    reg=f'{user_id}|{user_name}|{m}'
                    bot.send_message(message.chat.id,f'вы {reg}')
                    with open("ogyzki.txt", "r+", encoding='utf-8') as lg:
                        lg
                        d=False
                        for line in lg:
                            if reg in line:
                                d=True
                        if d:
                            bot.send_message(message.chat.id,f'вы уже смешарик')
                        else:
                            lg.write(reg + "\n")
                            bot.send_message(message.chat.id,f'{reg} добавлен в базу')
                
               
            else:
                bot.send_message(message.chat.id,f'сказали же ИМЯ_ФАМИЛИЯ, через "_" без пробелов')
    elif 'доп' in m.lower():
        bot.send_message(message.chat.id,'выбери доп материал',reply_markup = mark) 
    else:
        if (rere>=0):
            unu(message.chat.id,ms,m)
        else: 
            bot.send_message(message.chat.id,f'некоректный запрос.')
nnn=1
while nnn==1:
    try:
        bot.infinity_polling()
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(15)