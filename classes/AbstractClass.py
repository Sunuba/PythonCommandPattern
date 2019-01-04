from abc import ABC, abstractmethod


class Command(ABC):
    def execute(self, command):
        raise NotImplementedError


class LockInterface(ABC):
    def toggle(self):
        raise NotImplementedError

    def on(self):
        raise NotImplementedError

    def off(self):
        raise NotImplementedError
