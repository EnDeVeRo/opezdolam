import vk_api
from dataclasses import dataclass
from typing import Callable, Any
from vk_api.longpoll import VkLongPoll, VkEventType
import functools

H_type = Callable[[str], Any]


def user_repeat_non_stop(func):
    @functools.wraps(func)
    def wrapper(self):
        while True:
            try:
                return func(self)
            except Exception as error:
                print(error)

@dataclass
class Handler:
    prefix: str
    cmd: str
    me: bool
    func: H_type


class User:
    def __init__(self, token: str) -> None:
        self.all_commands: list = None
        self.commands: list[Handler] = []
        self.data: bool = False
        self.cmd: object = None
        self.vka: object = vk_api.VkApi(token=token)
        self.lpa: object = VkLongPoll(self.vka)
        self.apia: object = self.vka.get_api()
        self.event: object = None
        self.owner_id: int = self.apia.account.getProfileInfo()['id']

    def message_handler(self, prefix: str, cmd: str, me: bool):
        def decorator(func: H_type):
            self.commands.append(
                Handler(
                    prefix=prefix,
                    cmd=cmd,
                    me=me,
                    func=func
                )
            )
            return func

        return decorator

    def put_message_handler(self, data):
        self.commands.append(data)

    def it_im(self):
        print(11111111111111111111)
        if self.event.from_me == self.cmd.me:
            return True
        else: 
            return False

    def it_he(self):
        if not self.event.from_me: return True
        else: return False
    @user_repeat_non_stop
    def it_commands(self):
        if self.event.text.split(" ")[1] in self.cmd.cmd: return True
        else: return False

    def it_trusted(self):
        if self.event.user_id in self.trusted_list: return True
        else: return False
    @user_repeat_non_stop

    def it_trigger(self):
        if self.event.text.split(" ")[0] in self.trigger_list: return True
        else: return False

    def it_ignore(self):
        if self.event.user_id in self.ignore_list: return True
        else: return False

    @user_repeat_non_stop
    def it_alias(self):
        if self.event.text.split(" ")[0] in self.alias_list: return True
        else: return False

    @user_repeat_non_stop
    def get_prefix(self):
        print(3333333)
        if self.event.text.split(' ')[0] in self.cmd.prefix:
            return True
        else:
            return False


        #if self.event.text.split(" ")[0] == self.cmd.prefix and self.event.text.split(" ")[1] == self.cmd.cmd:
            #return True
        #else: return False

    def start(self) -> None:
        self.all_commands = [all_commands.cmd for all_commands in self.commands]
        for event in self.lpa.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                self.event = event
                for cmd in self.commands:
                    self.cmd = cmd
                    if self.it_im() and self.get_prefix  and self.it_commands():
                        cmd.func(self)


dp = User("-PpJ4H1i5-v5phrLEbhGM74ImbISZBkA")


from mod import datas


if __name__ == '__main__':
    for data in datas:
        for items in data.commands:
            dp.put_message_handler(items)
    dp.start()