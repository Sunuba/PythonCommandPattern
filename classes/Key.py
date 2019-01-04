from CommandPattern.classes.AbstractClass import Command


class Key(Command):
    def execute(self, command: Command):
        command.execute(command)