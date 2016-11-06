from shell import Executor
from utils import Common
from utils import Detector
from utils import CommonNew

c = None
d = Detector("python")
if d.version['python'].split('.')[1] >= 7:
    c = CommonNew()
    if c.args.command not in ["build", "check", "install"]:
        c.parser.print_help()
        exit(1)
else:
    c = Common()
    c.create_parser()
    flag = c.check()
    if flag:
        exit(1)
