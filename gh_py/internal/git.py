import subprocess

from .internal import exe_runner

def exec(args):
    if not verify_git():
        raise RuntimeError("Git is not installed.")
    return exe_runner.exec("git", args)

def verify_git():
    return exe_runner.verify("git", "version")

