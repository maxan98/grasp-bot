import command_system
from litedb import *
import subprocess as sp
def tomorrow(data):
    db = Database()
    answer = db.execread("SELECT gr FROM users WHERE vkid = %s"%data['user_id'])
    db.close()
    res = '' 
    if len(answer)>0:
        child=sp.Popen(['grasp','-f','-d','tom','-g','%s'%(answer[0])],stdout=sp.PIPE) 
        s=' '
        
        while s: 
            s=child.stdout.readline() 
            res +=s.decode('utf-8')
    message = res+' Если тут пусто - вероятно ты еще не задал номер своей группы(/группа xxxx)'
    return message, "", None
tomorrow_command = command_system.Command()
tomorrow_command.keys = ['Завтра','Tom']
tomorrow_command.description = 'Расписание на завтра'
tomorrow_command.process = tomorrow