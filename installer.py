import os
import sys

if not os.path.exists("bin"):
     os.mkdir("bin")

files = [i for i in os.walk("bin")]

def check_present(x):
    for i in files:
        if x in i[2]:
            sys.exit("App already present!")
        else:
            pass