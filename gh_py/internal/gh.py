import subprocess

from gh_py.exceptions import GhPyGhException

def exec(args):
    if not verify_gh():
        raise GhPyGhException("gh is not installed.")
    result = subprocess.run("gh " + args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # encode stdout and stderr, in a try.
    # if it fails, return the raw bytes
    try:
        stdout = result.stdout.decode("utf-8")
    except UnicodeDecodeError:
        stdout = result.stdout
    try:
        stderr = result.stderr.decode("utf-8")
    except UnicodeDecodeError:
        stderr = result.stderr
    if result.returncode != 0:
        raise GhPyGhException("gh failed with code {}\n\nSTDout:\n{}\n\nSTDErr:\n{}\n".format(result.returncode, stdout, stderr))
    return stdout

def verify_gh():
    try:
        # silent all output
        subprocess.run(["gh", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        return False
    else:
        return True
    