import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('number', type=int)
args = parser.parse_args()

dirname = "math"+str(args.number).zfill(3)

if os.path.exists(dirname):
    print(f"Directory {dirname} already exists.")
else:
    os.mkdir(dirname)
    fp = open(os.path.join(dirname, "solution.py"), "w")
    fp.close()
    fp = open(os.path.join(dirname, "solution.txt"), "w")
    fp.close()