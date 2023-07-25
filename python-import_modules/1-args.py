# script.py
import sys

args = sys.argv[1:]
num_args = len(args)

if __name__ == "__main__":
    if num_args == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(num_args, "s" if num_args > 1 else ""))
   
        for i, arg in enumerate(args):
            print("{}: {}".format(i+1, arg))