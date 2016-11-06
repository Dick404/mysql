import sys
import os

path = os.path.abspath(sys.argv[0])
sys.path.append(path)
system = reload(sys)

shell = __import__("lib.shell")