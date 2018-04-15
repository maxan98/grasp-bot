import command_system

def info():
    message = 'Привет, друг, я - новый бот SUAI. Пока я только учусь, но скоро я смогу помогать тебе не опаздывать на пары!'
    st = [d.description for d in command_system.command_list]
    return message, ""
info_command = command_system.Command()
info_command.keys = ['info','help','помощь','инфа','информация','что умеешь']
info_command.description = 'Расскажу о том, что я умею'
info_command.process = info