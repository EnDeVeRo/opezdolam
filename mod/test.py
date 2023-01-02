from mod import desp


dp = desp.User()

@dp.message_handler(["qq"], ['q'], False)
def hello_1(msg):
    msg.apia.messages.send(peer_id=msg.event.peer_id, message=f"{msg} | хуй", random_id=0)


@dp.message_handler(["qq"], ['qwe'], True)
def hello_1(msg):
    msg.apia.messages.send(peer_id=msg.event.peer_id, message=f"{msg} | залупа", random_id=0)


@dp.message_handler(["qq"], ['w'], True)
def hello_2(msg):
    msg.apia.messages.send(peer_id=msg.event.peer_id, message=f"{msg} | пизда", random_id=0)


@dp.message_handler(["qq"], ['e'], True)
def hello_2(msg):
    msg.apia.messages.send(peer_id=msg.event.peer_id, message=f"{msg} | сука ", random_id=0)
