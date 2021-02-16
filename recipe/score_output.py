import os

with open("out.txt",'r') as f:
    line = f.readlines()[0].strip()
    speaker = line[0:15]
    words = line.split()
    print(" ".join([speaker]+words[1:-1]))