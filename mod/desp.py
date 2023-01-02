from dataclasses import dataclass
from typing import Callable, Any

H_type = Callable[[str], Any]


@dataclass
class Handler:
    prefix: list
    cmd: list
    me: bool
    func: H_type


class User:
    def __init__(self) -> None:
        self.commands: list[Handler] = []

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
            print(prefix)
            return func

        return decorator
