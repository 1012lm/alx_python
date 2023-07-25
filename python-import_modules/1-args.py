# script.py
import sys

args = sys.argv[1:]
num_args = len(args)

if num_args == 0:
    print("0 arguments.")
else:
    print("{} arguments: ".format(num_args))
   
    for i, arg in enumerate(args):
        print("{}: {}".format(i+1, arg))