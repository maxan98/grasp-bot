import vkapi
import os
import importlib
from command_system import command_list
from litedb import *

def load_modules():
   # путь от рабочей директории, ее можно изменить в настройках приложения
   files = os.listdir("commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       importlib.import_module("commands." + m[0:-3])

def get_answer(data):
    # Сообщение по умолчанию если распознать не удастся
    message = "Прости, не понимаю тебя. Напиши 'помощь', чтобы узнать мои команды"
    attachment = ''
    pending = ''
    body = data['body'].lower()
    for c in command_list:
        if body in c.keys:
            message, attachment, pending = c.process()
    if '/группа' in body or '/Группа' in body:
        gr = body[8:]
        db = Database()
        db.execwrite("UPDATE users SET gr = '%s' WHERE vkid = %s"%(data['user_id'],data['user_id']))
        db.close()
        message = 'Супер, теперь я буду знать что ты учишься в группе # '+gr
    return message, attachment, pending

def create_answer(data, token):
   load_modules()
   user_id = data['user_id']
   message, attachment, pending = get_answer(data)
   vkapi.send_message(user_id, token, message, attachment)
   db = Database()
   answer = db.execread("SELECT vkid FROM users WHERE vkid = %s"%user_id)
   
   print(answer[0])
   if user_id in answer[0]:
    print('GJGJGJGJGJGJGJGJGJGJ\nGJGJGJGJGJGJGJGJGJGJGJ\nGJGJGJGJGJGJGJGJGJGJ')
    db.execwrite("insert into users values (NULL,%s,'RandUser',NULL,'user','NULL') "%(user_id))
    # if pending == 'group':
    #     db = Database()
    #     db.execwrite("UPDATE users SET pending = 'group' WHERE vkid = %s"%user_id)
    #     db.close()
