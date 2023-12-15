
with open('input') as f:
    line = f.read().splitlines()
    
    grid = list(map(lambda x : [y for y in x], line))
    
    for i in range(1):
        #North
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 'O':
                    temp = r
                    while temp > 0 and grid[temp-1][c] == '.':
                        grid[temp-1][c] = 'O'
                        grid[temp][c] = '.'
                        temp -= 1
        print("North")
        for i in grid:
            print("".join(i))
        #West
        for r in range(len(grid)):
                    for c in range(len(grid[r])):
                        if grid[r][c] == 'O':
                            temp = c
                            while temp != 0 and grid[r][temp-1] == '.':
                                grid[r][temp-1] = 'O'
                                grid[r][temp] = '.'
                                temp -= 1
                            if temp == 0 and grid[r][temp] == '0':
                                grid[r][temp] = '.'
        print("West")
        for i in grid:
            print("".join(i))
        print("South")
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 'O':
                    temp = r
                    while temp != len(grid) - 1 and grid[temp+1][c] == '.':
                        grid[temp+1][c] = 'O'
                        grid[temp][c] = '.'
                        temp -= 1
                    if temp == len(grid) - 1 and grid[temp][c] == '0':
                        grid[temp][c] = '.'
        for i in grid:
            print("".join(i))
        
        #East
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 'O':
                    temp = c
                    while temp != len(grid[r]) - 1 and grid[r][temp+1] == '.':
                        grid[r][temp+1] = 'O'
                        grid[r][temp] = '.'
                        temp -= 1
                    if temp == len(grid[r]) - 1 and grid[r][temp] == '0':
                        grid[r][temp] = '.'
        print("East")
        for i in grid:
            print("".join(i))
        #South
        
    
    length = len(grid)
    total = 0
    # for i in grid:
        # print("".join(i))
        # total += i.count('O') * length
        # length -= 1
    print(total)
        
                
