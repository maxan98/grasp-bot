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

def get_answer(body):
    # Сообщение по умолчанию если распознать не удастся
    message = "Прости, не понимаю тебя. Напиши 'помощь', чтобы узнать мои команды"
    attachment = ''
    pending = ''
    for c in command_list:
        if body in c.keys:
            message, attachment, pending = c.process()
    return message, attachment, pending

def create_answer(data, token):
   load_modules()
   user_id = data['user_id']
   message, attachment, pending = get_answer(data['body'].lower())
   
   if pending == 'group':
        db = Database()
        answer = db.execread("SELECT vkid FROM users WHERE vkid = %s"%user_id)
        if answer != user_id:
            db.execwrite("insert into users values (NULL,%s,'RandUser',NULL,'user','%s') "%(user_id,pending))
        else:
            message = 'Жду группу'
        if 'группа' in data['body'] or 'Группа' in data['body']:
            gr = data['body'][7:]
            db.execwrite("UPDATE users SET gr = '%s' WHERE vkid = %s"%(gr,user_id))
            db.execwrite("UPDATE users SET pending = 'NULL' WHERE vkid = %s"%user_id)
            message = 'Твоя группа '+ gr

        db.close()
   vkapi.send_message(user_id, token, message, attachment)
