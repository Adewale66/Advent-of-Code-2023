
with open('input') as f:
    line = f.readline().strip().split(',')  
    
    total = 0
    for i in line:
        hash  = 0
        for c in i:
            hash += ord(c)
            hash *= 17
            hash %= 256
        total += hash
    print(total)
