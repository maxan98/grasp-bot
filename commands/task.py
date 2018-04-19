import command_system
from litedb import *
import subprocess as sp
def task(data):
    pending = data['body']
    message = 'Напоминание на завтра. Формат [напоминание 12 00 Сообщение]\n Если до тебя вдруг чисто случайно доперло, что ты написал все не правильно - исправь ошибку и напиши еще раз'
    db = Database()
    db.execwrite("UPDATE users SET pending = '%s' WHERE CustomerID = %s"%(pending, data['user_id']))
    db.close()
    return message, "", None
task_command = command_system.Command()
task_command.keys = ['таймер','напоминание']
task_command.description = 'Установить напоминание(Синтаксис - ||напоминание 12 00 Сообщение||)'
task_command.process = task