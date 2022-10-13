import subprocess

def exec(exe, args):
    result = subprocess.run(exe + " " + args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise RuntimeError("{} command failed.".format(exe))
    return result.stdout

def verify(exe, arg="version"):
    try:
        subprocess.run([exe, arg], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        return False
    else:
        return True

