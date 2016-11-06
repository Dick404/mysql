import os
import sys


path = os.path.abspath(sys.argv[0])
sys.path.append(path)
reload(sys)
lib = __import__("lib.shell")


def checker(cmd, path):
    os.chdir(path)
    if cmd not in os.listdir(path):
        raise Exception(cmd + "not in " + path)
    e = lib.shell.Excutor("./" + cmd)
    if e.returncode != 0:
        raise Exception(e.result["stderr"])

