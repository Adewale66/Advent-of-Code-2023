
with open('input') as f:
    line = f.read().splitlines()
    
    grid = list(map(lambda x : [y for y in x], line))
    
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 'O':
                temp = r
                while temp > 0 and grid[temp-1][c] == '.':
                    grid[temp-1][c] = 'O'
                    grid[temp][c] = '.'
                    temp -= 1
    
    length = len(grid)
    total = 0
    for i in grid:
        total += i.count('O') * length
        length -= 1
    print(total)
        
                
