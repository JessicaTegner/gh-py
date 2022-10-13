import subprocess

from . import exe_runner

def exec(args):
    if not verify_gh():
        raise RuntimeError("gh is not installed.")
    return exe_runner.exec("gh", args)

def verify_gh():
    try:
        # silent all output
        subprocess.run(["gh", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        return False
    else:
        return True