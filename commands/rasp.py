import command_system
from litedb import *
import subprocess as sp
def rasp(data):
    db = Database()
    answer = db.execread("SELECT gr FROM users WHERE vkid = %s"%data['user_id'])
    db.close()
    child=sp.Popen(['grasp','-f','%s'%(answer)],stdout=sp.PIPE) 
    s=' '
    res = '' 
    while s: 
        s=child.stdout.readline() 
        res +=s.decode('utf-8')
    message = res+' \nЕсли тут пусто - вероятно ты еще не задал номер своей группы(/группа xxxx)'
    return message, "", None
rasp_command = command_system.Command()
rasp_command.keys = ['расписание','расп','полное','tt','rasp','timetable']
rasp_command.description = 'Полное расписание твоей группы'
rasp_command.process = rasp