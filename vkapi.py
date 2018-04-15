import vk

session = vk.Session()
api = vk.API(session, v=5.0)

def send_message(user_id, token, message, attachment=""):
    api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment)

def get_wall_picture():
    photo = api.photos.get(owner_id=str(-164325230), album_id='252800525', count=1, offset=0)
    attachment = 'photo' + str(-164325230) + '_' + str(photo)
    return attachment