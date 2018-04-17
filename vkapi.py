import vk
import random

session = vk.Session()
api = vk.API(session, v=5.0)
def getname(id):
    profiles = api.users.get(user_id=id)
    if len(profiles)>0:
        return profiles[0]
    return 'RandUser'
def send_message(user_id, token, message, attachment=""):
    api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment)

def get_wall_picture():

    max_num = api.photos.get(owner_id=-164325230, album_id='252800525', count=0)['count']
    num = random.randint(1, max_num)
    photo = api.photos.get(owner_id=str(-164325230), album_id='252800525', count=1, offset=num)['items'][0]['id']
    attachment = 'photo' + str(-164325230) + '_' + str(photo)
    return attachment
