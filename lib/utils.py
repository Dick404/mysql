from optparse import OptionParser
import shell


class Common(object):

    parser = None
    options = None
    args = None

    @classmethod
    def create_parser(cls):
        cls.parser = OptionParser()
        cls.parser.add_option("-p", "--path",
                              action="store",
                              dest="address",
                              default="/opt/mysql/",
                              help="indicate the location of mysql source code")
        (cls.options, cls.args) = cls.parser.parse_args()
#      if options.address == "/opt/mysql/":
#            print "yes"

    @classmethod
    def config(cls, path):
        if type(path) != 'str':
            raise BaseException("wrong path for mysql source code.")

    @classmethod
    def check(cls):
        if cls.args == "" or cls.options == "":
            cls.parser.help

if __name__ == '__main__':
    c = Common()
    c.create_parser()