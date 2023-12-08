#!/usr/bin/python3

import math



if __name__ == "__main__":
    with open("input", "r") as f:
        l = f.readlines()
        movement = ""
        for line in l:
            if line == "\n":
                break
            else:
                movement += line.strip()
        coord = {}
        place = 0
        for i in range(l.index("\n") + 1, len(l)):
            c , p = l[i].strip().replace("(", "").replace(")", "").split("=")
            coord[c.strip()] = [x.strip() for x in p.split(",")]
        pos = []
        for i in coord:
            if i.endswith("A"):
                pos.append(i)
        le = len(pos)
        lc = [0] * le
        while True:
            if place > (len(movement) - 1):
                place = 0
            if movement[place] == 'L':
                pos = list(map(lambda x : x if x.endswith("Z") else coord[x][0], pos))
            else:
                pos = list(map(lambda x : x if x.endswith("Z") else coord[x][1], pos))
            place += 1
            for i, j in enumerate(pos):
                if not j.endswith('Z'):
                    lc[i] += 1
            if len(list(filter(lambda x : x.endswith("Z"), pos))) == le:
                break
        lcm = print(math.lcm(*(list(map(lambda x : x + 1, lc)))))
        