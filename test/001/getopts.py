import getopt
import sys
opts,args=getopt.getopt(sys.argv[1:],'ab:',['ccc','ddd=','eee='])
print(opts)
print(args)