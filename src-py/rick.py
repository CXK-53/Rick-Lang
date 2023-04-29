from argparse import ArgumentParser
from sys import stdout
import time
from sys import stdout

def read_file(file_name):
     with open(file_name, 'r', encoding='utf-8') as f:
          return f.read()

def main():
     arg_parser = ArgumentParser()
     arg_parser.add_argument("file", nargs='?', default="")
     arg_parser.add_argument("-cpp", action="store_true")
     arg_parser.add_argument("-intpr", action="store_true")
     arg_parser.add_argument("--time", action="store_true")
     arg_parser.add_argument("--audio", action="store_true")
     args = arg_parser.parse_args()

     start = time.time()


     if args.intpr:
          pass
     elif args.cpp:
          pass
     else:
          import Pyrun
          src = read_file(args.file)
          Pyrun.py_run(src)
     if args.time:
          stdout.write(f"{time.time()} mill secs")



if __name__ == '__main__':
     main()