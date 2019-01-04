from CommandPattern.classes.AbstractClass import LockInterface


class Lock(LockInterface):

    def __init__(self):
        self.is_locked = False

    def toggle(self):
        if self.is_locked:
            self.off()
            self.is_locked = False
        else:
            self.on()
            self.is_locked = True

    def on(self):
        print("Door is locked. ")

    def off(self):
        print("Door is unlocked. ")


class BackdoorLock(LockInterface):

    def __init__(self):
        self.is_locked = False

    def toggle(self):
        if self.is_locked:
            self.off()
            self.is_locked = False
        else:
            self.on()
            self.is_locked = True

    def on(self):
        print("Backdoor is locked. ")

    def off(self):
        print("Backdoor is unlocked. ")
