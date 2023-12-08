

if __name__ == "__main__":
    with open("input", "r") as f:
        l = f.readlines()
        steps = 0
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
        pos = 'AAA'
        while pos != "ZZZ":
            if place > (len(movement) - 1):
                place = 0
            if movement[place] == 'L':
                pos = coord[pos][0]
            else:
                pos = coord[pos][1]
            place += 1
            steps += 1
        print(steps)

