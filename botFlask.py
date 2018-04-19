

from flask import Flask, request, json
from settings import token, confirmation_token
import messageHandler
import vkapi
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/', methods=['POST'])
def processing():

     #Распаковываем json из пришедшего POST-запроса
     data = json.loads(request.data)
     #Вконтакте в своих запросах всегда отправляет поле типа
     if 'type' not in data.keys():
         print('return not vk')
         return 'not vk'
     if data['type'] == 'confirmation':
         return confirmation_token
     elif data['type'] == 'message_new':


         messageHandler.create_answer(data['object'], token)
         # Сообщение о том, что обработка прошла успешно
         return 'ok'

@app.route('/suckdick', methods=['POST'])
def processing():
    data = json.loads(request.data)
    i = data['vkid']
    messa = data['messa']
    secret = data['secret']
    if secret == 'suckmydick'
        vkapi.send_message(i, token, messa, '')
        return 'ok'
    else:
        return 'not vk'

