#!/usr/bin/python3

import sys

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
   
    lines = "".join(lines).split("\n\n")
    seeds = [int(x) for x in lines[0].split(":")[1].strip().split(" ")]
   
    for i in lines[1:]:
        range_value = []
        for j in i.strip().split("\n")[1:]:
            range_value.append(list(map(int, j.split())))
        new = []
        for x in seeds:
            for dest, src, length in range_value:
                if src <= x < src + length:
                    new.append(dest + (x - src))
                    break
            else:
                new.append(x)
        seeds = new
    print(min(seeds))
    