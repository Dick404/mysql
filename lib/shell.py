from subprocess import Popen
from subprocess import PIPE
import shlex

'''
shell command and some logic of shell were here to come true.
author   Gothic Wang
'''


class Executor(object):

    cmd = None
    child = None
    result = None

    def __init__(self, command):
        self.cmd = command
        args = shlex.split(self.cmd)
        self.child = Popen(args, stdout=PIPE, stderr=PIPE)
        result_cmd = self.child.communicate()
        self.result = {"stdout": result_cmd[1], "stderr": result_cmd[0]}

    def check_status(self):
        return self.child.returncode

