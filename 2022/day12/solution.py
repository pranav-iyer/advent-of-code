import copy
import sys
from collections import deque
from dataclasses import dataclass


def get_height(c: str) -> int:
    if c == "S":
        return 0
    if c == "E":
        return 25
    return ord(c) - ord("a")


class Node:
    def __init__(self, position: tuple[int, int], height: int, neighbors: set["Node"]):
        self.position = position
        self.height = height
        self.neighbors = neighbors

    def __str__(self):
        return f"{self.position} ({self.height}) [{' '.join(str(x.position) for x in self.neighbors)}]"


def get_grid(input: str):
    grid = [[c for c in line.strip()] for line in input.splitlines()]
    _M = len(grid[0])
    grid = [["|" for _ in range(_M)]] + grid + [["|" for _ in range(_M)]]
    _N = len(grid)
    for i in range(_N):
        grid[i] = ["|"] + grid[i] + ["|"]
    return grid


DIRECTIONS: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Graph:
    def __init__(self):
        self.nodes: set[Node] = set()

    @property
    def positions(self):
        return [n.position for n in self.nodes]

    def get_node(self, position: tuple[int, int]):
        return [n for n in self.nodes if n.position == position][0]

    def distance_from(self, source: tuple[int, int], dest: tuple[int, int]):
        start_node = self.get_node(source)
        end_node = self.get_node(dest)

        seen: set[tuple[int, int]] = {start_node.position}
        nodes: deque[tuple[int, Node]] = deque()
        nodes.append((0, start_node))
        while True:
            distance, curr = nodes.popleft()
            if curr.position == end_node.position:
                return distance

            seen.add(curr.position)
            for n in curr.neighbors:
                if n.position not in seen:
                    seen.add(n.position)
                    nodes.append((distance + 1, n))


def part1(input: str):
    grid = get_grid(input)
    N = len(grid)
    M = len(grid[0])

    start_pos, end_pos = (0, 0), (0, 0)
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "S":
                start_pos = (i, j)
            if grid[i][j] == "E":
                end_pos = (i, j)

    start_node = Node(start_pos, 0, set())
    graph = Graph()
    nodes: deque[Node] = deque()
    nodes.append(start_node)
    while True:
        try:
            curr = nodes.popleft()
        except IndexError:
            break
        curr_height = get_height(grid[curr.position[0]][curr.position[1]])

        for i in range(4):
            cmp_pos = (
                curr.position[0] + DIRECTIONS[i][0],
                curr.position[1] + DIRECTIONS[i][1],
            )
            cmp_height = get_height(grid[cmp_pos[0]][cmp_pos[1]])
            if curr.position == (21, 128):
                print(cmp_pos, cmp_height)
            if cmp_height - curr_height <= 1:
                if cmp_pos not in graph.positions:
                    new_node = Node(cmp_pos, cmp_height, set())
                    graph.nodes.add(new_node)
                    curr.neighbors.add(new_node)
                    nodes.append(new_node)
                else:
                    curr.neighbors.add(graph.get_node(cmp_pos))

    print("graph constructed.")
    print(graph.get_node((21, 128)))

    return graph.distance_from(start_pos, end_pos)


def part2(input: str):
    grid = get_grid(input)
    N = len(grid)
    M = len(grid[0])

    start_pos, end_pos = (0, 0), (0, 0)
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "S":
                start_pos = (i, j)
            if grid[i][j] == "E":
                end_pos = (i, j)

    start_node = Node(start_pos, 0, set())
    graph = Graph()
    nodes: deque[Node] = deque()
    nodes.append(start_node)
    while True:
        try:
            curr = nodes.popleft()
        except IndexError:
            break
        curr_height = get_height(grid[curr.position[0]][curr.position[1]])

        for i in range(4):
            cmp_pos = (
                curr.position[0] + DIRECTIONS[i][0],
                curr.position[1] + DIRECTIONS[i][1],
            )
            cmp_height = get_height(grid[cmp_pos[0]][cmp_pos[1]])
            if curr.position == (21, 128):
                print(cmp_pos, cmp_height)
            if cmp_height - curr_height <= 1:
                if cmp_pos not in graph.positions:
                    new_node = Node(cmp_pos, cmp_height, set())
                    graph.nodes.add(new_node)
                    curr.neighbors.add(new_node)
                    nodes.append(new_node)
                else:
                    curr.neighbors.add(graph.get_node(cmp_pos))

    print("graph constructed.")
    return graph.get_nearest_a(grid, start_pos, end_pos)


if __name__ == "__main__":
    if "2" not in sys.argv:
        with open("input.txt") as f:
            input1 = f.read()
        print("Part 1".center(80, "="))
        print("Solution:", part1(input1))

    if "1" not in sys.argv:
        with open("input.txt") as f:
            input2 = f.read()
        print("Part 2".center(80, "="))
        print("Solution:", part2(input2))
