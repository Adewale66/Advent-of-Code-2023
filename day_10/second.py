with open("input") as f:
    lines = f.read().splitlines()
    grid = list(map(lambda x : [y for y in x], lines))
    
    total = 0
    speccial = ['J', 'F', 'L', '|', '-', '7']
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                around = 0
                if j > 0 and grid[i][j-1] in speccial:
                    around += 1
                if j < (len(grid[i]) - 1) and grid[i][j+1] in speccial:
                    around += 1
                if i > 0 and grid[i-1][j] in speccial:
                    around += 1
                if i < (len(grid) -1)  and grid[i+1][j] in speccial:
                    around += 1
                if around > 2:
                    total += 1
    print(total)
                    
                    
