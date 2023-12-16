import copy

all_pos = []
with open("input") as f:
    lines = f.read().splitlines()
    grid = list(map(lambda x : [y for y in x], lines))
    grid_cpy = copy.deepcopy(grid)
    
    
    for i in range(len(grid)):
        all_pos.append([i, 0, "col-right"])
    for i in range(len(grid[0])):
        all_pos.append([0, i, "row-down"])
   
    for i in range(len(grid)-1, -1, -1):
        all_pos.append([i, len(grid[0]) -1, "col-left" ])
    for i in range(len(grid[0]) -1, -1, -1):
        all_pos.append([len(grid)-1, i, "row-up"])
    
    
    total_max = 0
    for i in all_pos:
        visited = []
        pos = [i]
        start_visited = [[i[0], i[1]]]
        special = ['-', '|', '/', '\\']
        with open("input") as f:
            lines = f.read().splitlines()
            grid = list(map(lambda x : [y for y in x], lines))
            
            while len(pos) > 0:
                curr_pos = pos.pop()
                while (curr_pos[0] < len(grid) and curr_pos[0] >= 0) and (curr_pos[1] < len(grid[curr_pos[0]]) and curr_pos[1] >= 0):    
                    if grid[curr_pos[0]][curr_pos[1]] == '|':
                        if curr_pos[2] == "col-right" or curr_pos[2] == "col-left":
                            if [curr_pos[0]-1, curr_pos[1]] in start_visited:
                                break
                            else:
                                start_visited.append([curr_pos[0]-1, curr_pos[1]])
                                pos.append([curr_pos[0]-1, curr_pos[1], "row-up"])
                                curr_pos[2] = "row-down"
                        
                    elif grid[curr_pos[0]][curr_pos[1]] == '-':
                        if curr_pos[2] == "row-up" or curr_pos[2] == "row-down":
                            if [curr_pos[0], curr_pos[1]-1] in start_visited:
                                break
                            else:
                                start_visited.append([curr_pos[0], curr_pos[1]-1])
                                pos.append([curr_pos[0], curr_pos[1]-1, "col-left"])
                                curr_pos[2] = "col-right"
                    elif grid[curr_pos[0]][curr_pos[1]] == '/':
                        if curr_pos[2] == "col-right":
                            curr_pos[2] = "row-up"
                        elif curr_pos[2] == "col-left":
                            curr_pos[2] = "row-down"
                        elif curr_pos[2] == "row-up":
                            curr_pos[2] = "col-right"
                        elif curr_pos[2] == "row-down":
                            curr_pos[2] = "col-left"
                    elif grid[curr_pos[0]][curr_pos[1]] == '\\':
                        if curr_pos[2] == "col-right":
                            curr_pos[2] = "row-down"
                        elif curr_pos[2] == "row-up":
                            curr_pos[2] = "col-left"
                        elif curr_pos[2] == "col-left":
                            curr_pos[2] = "row-up"
                        elif curr_pos[2] == "row-down":
                            curr_pos[2] = "col-right"
                        
                
                    if grid[curr_pos[0]][curr_pos[1]] not in special:
                        grid[curr_pos[0]][curr_pos[1]] = '#'
                    else:
                        visited.append([curr_pos[0], curr_pos[1]])
                    
                    if curr_pos[2] == "col-right":
                        curr_pos[1] += 1
                    elif curr_pos[2] == "col-left":
                        curr_pos[1] -= 1
                    elif curr_pos[2] == "row-up":
                        curr_pos[0] -= 1
                    elif curr_pos[2] == "row-down":
                        curr_pos[0] += 1

            visited = set(map(tuple, visited))
            for i in visited:
                grid[i[0]][i[1]] = '#'
            total = 0
            for i in grid:
                total += i.count('#')
            if total > total_max:
                total_max = total
            grid = copy.deepcopy(grid_cpy)
    print(total_max)
        