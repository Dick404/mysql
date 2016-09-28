import os
import sys


def execute():
    (file_stdin, file_stdout, file_stderr) = os.popen3()
    return 0


def callback():
    return 0