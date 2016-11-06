#!/usr/bin/env python

from lib.utils import Common
import lib
import sys
import os
import lib.mysql.common as mysql


def main():
    xx = mysql.init()
    e = xx.shell.Executor("ls -l")
    print e
    if not os.path.exists(lib.c.args.path):
        raise Exception(lib.c.args.path+" is not existed.")
    return 0


def get_configure():
    return 0


if __name__ == "__main__":
    main()
