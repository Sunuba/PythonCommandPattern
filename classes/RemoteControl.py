from CommandPattern.classes.AbstractClass import Command, LockInterface


class RemoteControl(Command):
    def __init__(self, lock: LockInterface):
        self.lock = None
        self.lock_status = None
        self.lock = lock

    def execute(self, command: Command):
        self.lock.toggle()
