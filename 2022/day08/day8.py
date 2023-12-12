import operator
from functools import reduce

grid = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        grid.append([int(c) for c in line])

visible = set()
for i in range(len(grid)):
    largest_so_far = -1
    for j in range(len(grid[0])):
        if grid[i][j] > largest_so_far:
            visible.add((i,j))
            largest_so_far = grid[i][j]

for i in range(len(grid)):
    largest_so_far = -1
    for j in reversed(range(len(grid[0]))):
        if grid[i][j] > largest_so_far:
            visible.add((i,j))
            largest_so_far = grid[i][j]

for j in range(len(grid[0])):
    largest_so_far = -1
    for i in range(len(grid)):
        if grid[i][j] > largest_so_far:
            visible.add((i,j))
            largest_so_far = grid[i][j]

for j in range(len(grid[0])):
    largest_so_far = -1
    for i in reversed(range(len(grid))):
        if grid[i][j] > largest_so_far:
            visible.add((i,j))
            largest_so_far = grid[i][j]

# print(len(visible))


def get_scenic_score(i,j):
    scores = [1,1,1,1]
    here = grid[i][j]

    # up
    curr = i - 1
    while curr > 0 and grid[curr][j] < here:
        scores[0] += 1
        curr -= 1

    # down
    curr = i + 1
    while curr < len(grid)-1 and grid[curr][j] < here:
        scores[1] += 1
        curr += 1

    # left
    curr = j - 1
    while curr > 0 and grid[i][curr] < here:
        scores[2] += 1
        curr -= 1

    # right
    curr = j + 1
    while curr < len(grid[0]) - 1 and grid[i][curr] < here:
        scores[3] += 1
        curr += 1

    return scores


lrg = -1
for i in range(len(grid)):
    for j in range(len(grid[0])):
        scr = get_scenic_score(i,j)
        tot = reduce(operator.mul, scr, 1)
        if tot > lrg:
            print(i,j)
            print(scr, tot)
            lrg = tot

print(lrg)