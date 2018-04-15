import command_system
import vkapi
def info():
    message = 'Вот то, что я умею на данный момент. Всяко лучше, чем быть одноглазым и с палкой в ноге :)'
    st = [d.description +'['+' '.join(d.keys)+']' for d in command_system.command_list]
    desc = '\n'.join(st)
    attachment = vkapi,get_wall_picture()
    return message + '\n'+desc, attachment
info_command = command_system.Command()
info_command.keys = ['info','help','помощь','инфа','информация','что умеешь']
info_command.description = 'Расскажу о том, что я умею'
info_command.process = info