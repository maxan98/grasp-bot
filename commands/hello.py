import command_system

def hello():
    message = 'Привет, друг, я - новый бот SUAI. Пока я только учусь, но скоро я смогу помогать тебе не опаздывать на пары!'
    return message, ""
hello_command = command_system.Command()
hello_command.keys = ['привет','здорово','хай','ку','здравствуй','здравствуйте']
hello_command.description = 'Начать попиздошки с ботом'
hello_command.process = hello