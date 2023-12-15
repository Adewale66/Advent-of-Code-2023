
with open('input') as f:
    line = f.readline().strip().split(',')  
    
    box = [[] for _ in range(256)]
    for i in line:
        hash = 0
        for c in i:
            if c == '-' or c == '=':
                break
            hash += ord(c)
            hash *= 17
            hash %= 256
        temp = box[hash]
        if '=' in i:
            if len(temp) == 0:
                box[hash].append(i.replace('=', ' '))
            else:
                for j in temp:
                    if j.split(" ")[0] == i.split("=")[0]:
                        box[hash][temp.index(j)] = i.replace('=', ' ')
                        break
                else:
                    box[hash].append(i.replace('=', ' '))
        if '-' in i:
            if len(temp) != 0:
                for j in temp:
                    if j.split()[0] == i.split("-")[0]:
                        temp.remove(j)
                        break
        
total = 0
box_pos = 1      
for i in box:
    pos = 1
    for j in i:
        total += pos * int(j.split(" ")[1]) * box_pos
        pos += 1
    box_pos += 1
print(total)
