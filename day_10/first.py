with open("input") as f:
    lines = f.read().splitlines()
    grid = list(map(lambda x : [y for y in x], lines))
    curr = []
    
    for i in grid:
        for j in i:
            if j == 'S':
                curr = [grid.index(i), i.index(j), 'row-down']
                break
    max_dis = []   
    steps = 0
    starting = [curr[0] + 0, curr[1]+ 0]
    while True:            
        if curr[2] == "col-right":
            curr[1] += 1
            if grid[curr[0]][curr[1]] == '7':
                curr[2] = "row-down"
            elif grid[curr[0]][curr[1]] == 'J':
                curr[2] = "row-up"
        elif curr[2] == "col-left":
            curr[1] -= 1
            if grid[curr[0]][curr[1]] == 'L':
                curr[2] = "row-up"
            elif grid[curr[0]][curr[1]] == 'F':
                curr[2] = "row-down"
        elif curr[2] == "row-up":
            curr[0] -= 1
            if grid[curr[0]][curr[1]] == '7':
                curr[2] = "col-left"
            elif grid[curr[0]][curr[1]] == 'F':
                curr[2] = "col-right"
        elif curr[2] == "row-down":
            curr[0] += 1
            if grid[curr[0]][curr[1]] == 'J':
                curr[2] = "col-left"
            elif grid[curr[0]][curr[1]] == 'L':
                curr[2] = "col-right"
        steps += 1
        max_dis.append(steps)
        if grid[curr[0]][curr[1]] == 'S':
            break
    print(max(max_dis) // 2)
