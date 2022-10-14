import sys

from cleo.application import Application
from cleo.io.io import IO
from cleo.io.inputs.string_input import StringInput
from cleo.commands.command import Command

def run(args=None):
    # Set your name and version here.
    application = Application(name='My Awesome GH Extension', version='0.1.0')
    # add your commands here.
    application.add(HelloCommand())

    # below here we run. You don't need to modify this.
    if args:
        input = StringInput(args)
        input.set_stream(sys.stdin)
        application.run(input)
    else:
        application.run()

class HelloCommand(Command):
    name = "hello"
    description = "Say hello to the console."

    def handle(self):
        self.line('Hello World')
    