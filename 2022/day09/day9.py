
with open('input.txt', 'r') as f:
    inst = [tuple(l.strip().split()) for l in f.readlines()]
    inst = [(x, int(y)) for x,y in inst]


visited = set()
visited.add((0,0))

hpos = [0,0]
tpos = [0,0]

def go(d):
    if d == 'L':
        hpos[0] -= 1
        if tpos[0] - hpos[0] > 1:
            tpos[0] -= 1
            tpos[1] = hpos[1]

    elif d == 'R':
        hpos[0] += 1
        if hpos[0] - tpos[0] > 1:
            tpos[0] += 1
            tpos[1] = hpos[1]

    elif d == 'U':
        hpos[1] += 1
        if hpos[1] - tpos[1] > 1:
            tpos[1] += 1
            tpos[0] = hpos[0]

    elif d == 'D':
        hpos[1] -= 1
        if tpos[1] - hpos[1] > 1:
            tpos[1] -= 1
            tpos[0] = hpos[0]

    visited.add(tuple(tpos))

for i in inst:
    for j in range(i[1]):
        go(i[0])

print(len(visited))