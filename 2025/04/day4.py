import itertools

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

grid = [[1 if c == "@" else 0 for c in line] for line in lines]
N = len(grid)  # it's square


def num_adjacent(i, j):
    total = 0
    for test_i, test_j in itertools.product([i - 1, i, i + 1], [j - 1, j, j + 1]):
        if test_i == i and test_j == j:
            continue
        if test_i < 0 or test_i >= N:
            continue
        if test_j < 0 or test_j >= N:
            continue
        total += grid[test_i][test_j]
    return total


rolls_removed = 0
while sum(sum(row) for row in grid) > 0:
    print(sum(sum(row) for row in grid))
    print("removed", rolls_removed)
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1 and num_adjacent(i, j) < 4:
                rolls_removed += 1
                grid[i][j] = 0

print(rolls_removed)
