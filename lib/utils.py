from optparse import OptionParser
import shell


class Common(object):

    @classmethod
    def create_parser(cls):
        parser = OptionParser()
        parser.add_option("-p", "--path",
                          action="store_true",
                          dest="address",
                          default="/opt/mysql/",
                          help="indicate the location of mysql source code")
        (options, args) = parser.parse_args()
        if options.address == "/opt/mysql/":
            print "yes"
        print args

    @classmethod
    def config(cls, path):
        if type(path) != 'str':
            raise BaseException("wrong path for mysql source code.")



if __name__ == '__main__':
    c = Common()
    c.create_parser()