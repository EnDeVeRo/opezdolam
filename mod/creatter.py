from BaseReuests.Base_Requests import Base
from mod import desp
import json


base = Base()
dp = desp.User()


@dp.message_handler(['f', 's'], ['q'], True)
def tests(msg):
    filter = dict(user_id=msg.owner_id)
    params = dict(user_id=msg.owner_id, balance=300)
    responce = base.creater(filter, params)
    print(responce)
    if responce['data'] is None:
        msg.apia.messages.send(peer_id=msg.event.peer_id, message=f" |  не Создал юзера", random_id=0)
    else:
        msg.apia.messages.send(peer_id=msg.event.peer_id, message=f" | Создал юзера", random_id=0)