import os
import sys
import shutil

from cleo.application import Application
from cleo.io.io import IO
from cleo.io.inputs.string_input import StringInput
from cleo.commands.command import Command
from cleo.helpers import argument

def run(args=None):
    application = Application(name='gh-py', version='1.2.0')
    application.add(CreateCommand())
    if args:
        input = StringInput(args)
        input.set_stream(sys.stdin)
        application.run(input)
    else:
        application.run()

# make a create command.
class CreateCommand(Command):
    name = "create"
    description = "Creates a GH extension with python scaffolding."
    arguments = [
        argument(
            "name",
            description="The name of the gh extension to create.",
            optional=True
        )
    ]

    def handle(self):
        name = self.argument("name")
        if not name:
            name = self.ask("Extension name:")
        if not name.startswith("gh-"):
            self.line(f"Extension name {name} does not start with 'gh-', adding that to the name, because of gh extension requirements.") if self.io.output.is_debug() else None
            name = f"gh-{name}"
        self.line(f"Creating extension {name}")
        if os.path.exists(os.path.join(os.getcwd(),name)):
            self.line(f"Extension {name} already exists.")
            return
        self.line("Creating scaffolding...")
        ext_dir = os.path.join(os.getcwd(), name)
        self._create_scaffolding(name, ext_dir)
        self.line(f"Created extension {name}")

    def _create_scaffolding(self, name, ext_dir):
        # print that we are creating the scaffolding in the cwd.
        self.line(f"Creating scaffolding in {ext_dir}") if self.io.output.is_debug() else None
        shutil.copytree(os.path.join(os.path.dirname(__file__), "scaffolding"), ext_dir)
        os.rename(os.path.join(ext_dir, "scaffolding"), os.path.join(ext_dir, name))
        os.chmod(os.path.join(ext_dir, name), 0o755)
        os.remove(os.path.join(ext_dir, "__init__.py"))
        self.line(f"Scaffolding created in {ext_dir}") if self.io.output.is_debug() else None

