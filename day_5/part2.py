#!/usr/bin/python3

import sys


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
   
    lines = "".join(lines).split("\n\n")
    input_range = [int(x) for x in lines[0].split(":")[1].strip().split(" ")]

    seeds = []

    for i in range(0, len(input_range), 2):
        seeds.append((input_range[i], input_range[i+1] + input_range[i]))
   
    for i in lines[1:]:
        range_value = []
        for j in i.strip().split("\n")[1:]:
            range_value.append(list(map(int, j.split())))
        new = []

        while len(seeds) > 0:
            start, end  = seeds.pop()
            for dest, src, length in range_value:
                os = max(start, src)
                oe = min(end, src + length)
                if os < oe:
                    new.append((os - src + dest, oe - src + dest))
                    if os > start:
                        seeds.append((start, os))
                    if oe < end:
                        seeds.append((oe, end))
                    break
            else:
                new.append((start, end))
        seeds = new
    print(min(seeds)[0])
    