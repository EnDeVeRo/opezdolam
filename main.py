import vk_api
from dataclasses import dataclass
from typing import Callable, Any
from vk_api.longpoll import VkLongPoll, VkEventType

H_type = Callable[[str], Any]


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

    def comparison(self):

        def it_im(data):
            if data.event.from_me == data.cmd.me:
                return True
            else: 
                return False

        def it_he():
            if not data.event.from_me: return True
            else: return False

        def it_commands(data):
            if data.event.text.split(" ")[1] in data.all_commands: return True
            else: return False

        def it_trusted(data):
            if data.event.user_id in data.trusted_list: return True
            else: return False

        def it_trigger(data):
            if data.event.text.split(" ")[0] in data.trigger_list: return True
            else: return False

        def it_ignore(data):
            if data.event.user_id in data.ignore_list: return True
            else: return False

        def it_alias(data):
            if data.event.text.split(" ")[0] in data.alias_list: return True
            else: return False

        def get_prefix(data):
            if data.event.text.split(' ')[0] == data.cmd.prefix:
                return True
            else:
                return False

        return it_im

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
                    print(self.cmd)
                    if self.comparison():
                        print(self.cmd.prefix)
                        if self.event.text.split(" ")[0] in self.cmd.prefix and self.event.text.split(" ")[1] in self.cmd.cmd:
                            print(self.comparison())
                            cmd.func(self)


dp = User("")


from mod import datas


if __name__ == '__main__':
    for data in datas:
        for items in data.commands:
            dp.put_message_handler(items)
    dp.start()
