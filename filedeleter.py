
from argparse import ArgumentParser
import os

# python filedeleter.py -d C:\Users\... -s 50000


ArgumentParser = ArgumentParser()
ArgumentParser.add_argument("-s", "--size", help="min size of files to delete", type=int)
ArgumentParser.add_argument("-d", "--directory", help="Directory", type=str)
args = ArgumentParser.parse_args()


for filename in os.scandir(args.directory):
    if filename.is_file():
        if os.path.getsize(filename.path) > args.size:
            print("removing " + filename.path)
            os.remove(filename.path)