import command_system
def hello(data):
    
    message = '''Привет, друг, я - новый бот SUAI. Пока я только учусь, но скоро я смогу помогать тебе не опаздывать на пары!\n Если ты тут впервые - отправь мне номер своей группы и я сразу начну подсказывать тебе с парами :)\n
    Например: /Группа 5512 или /группа 8431К\n
    Если в номере твоей группы присутствуют буквы - пиши их, пожалуйста заглавными И русскими, скоро я научусь различать любые твои каракули, но пока - так :)
    '''
    return message, "", None
hello_command = command_system.Command()
hello_command.keys = ['привет','здорово','хай','ку','здравствуй']
hello_command.description = 'Начать попиздошки с ботом'
hello_command.process = hello
