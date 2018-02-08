import argparse
parser=argparse.ArgumentParser()
# parser.add_argument('-a','-aa',help='aaaaaaaaaaaaaaaaaaa',action='store_true')
args=parser.parse_args()


if args.a:
	print(1)
	print(args.a )
