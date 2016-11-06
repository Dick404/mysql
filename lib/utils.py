from optparse import OptionParser
import argparse
import sys
import re
from shell import Executor


# old version python(<= 2.7) use this module to create command interface
class Common(object):

    parser = None
    options = None
    args = None
    command = ["install", "build", "check"]

    @classmethod
    def create_parser(cls):
        usage = "usage: %prog [options] command"
        cls.parser = OptionParser(usage=usage)
        cls.parser.add_option("-p", "--path",
                              action="store",
                              dest="address",
                              default="/opt/mysql/",
                              help="indicate the location of mysql source code")
        (cls.options, cls.args) = cls.parser.parse_args()

    @classmethod
    def config(cls, path):
        if type(path) != 'str':
            raise BaseException("wrong path for mysql source code.")

    @classmethod
    def check(cls):
        if len(cls.args) != 1 or cls.args[0] not in cls.command:
            cls.parser.print_help()
            return 1
        else:
            return 0


# new module for optparse python 2.7 or higher use this
class CommonNew(object):

    parser = None
    args = None

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="build and install mysql for system.")
        self.parser.add_argument("command", metavar="command", type=str, help="include check build and install.")
        self.parser.add_argument("-p",
                                 "--path",
                                 dest='path',
                                 action='store',
                                 default='/usr/local/mysql',
                                 help='describe the location of MYSQL source code.')
        self.args = self.parser.parse_args()


# detect the OS and software's version, can be used alone
class Detector(object):

    version = {}
    OS = None
    software = None

    def __init__(self, *software):
        self.OS = sys.platform
        self.software = software
        for s in software:
            exe = Executor(s.lower()+" --version")
            if exe.check_status() != 0:
                raise Exception(exe.result["stderr"])
            self.version[s] = exe.result["stdout"]
        self.deal()

    @classmethod
    def deal(cls):
        for k in cls.version.keys():
            finder = re.compile(r'v?(\d+.\d+.\d+)').search(cls.version[k])
            if finder:
                cls.version[k] = finder.group(1)
        return 0

if __name__ == '__main__':
    x = Detector("python", "gcc")
#    c = CommonNew()
