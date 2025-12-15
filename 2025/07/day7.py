from dataclasses import dataclass
import uuid

with open("input.txt", "r") as f:
    grid = [
        list("." * 1) + list(line.strip()) for line in f.readlines() if line.strip()
    ]

N = len(grid[0])
K = len(grid) - 1
S = grid[0].index("S")
grid = grid[1:]


def part1():
    beams = [S]
    split_ct = 0
    for k in range(K):
        print(k, beams)
        # check for splitters
        splitter_locs = []
        for i, val in enumerate(grid[k]):
            if val == "^":
                splitter_locs.append(i)
        split_beams = list(filter(lambda beam: beam in splitter_locs, beams))
        for beam in split_beams:
            split_ct += 1
            # beam splits
            if beam - 1 > 0 and beam - 1 not in beams:
                beams.append(beam - 1)
            if beam + 1 < N and beam + 1 not in beams:
                beams.append(beam + 1)
            beams.remove(beam)
        beams.sort()
    return split_ct


@dataclass
class Node:
    guid: uuid.UUID
    pos: int
    left: "Node | None"
    right: "Node | None"

    def __str__(self):
        left = self.left.pos if self.left else None
        right = self.right.pos if self.right else None
        return f"{self.pos} [{left}, {right}]"


def count_paths(root: Node):
    # root stores the binary tree now, we need to count the number of paths to the bottom
    pathcount = dict()
    to_visit = [root]
    num_paths = 0
    while len(to_visit) > 0:
        print(len(pathcount))
        curr = to_visit.pop()
        if curr.guid in pathcount:
            num_paths += pathcount[curr.guid]
        elif curr.left is None and curr.right is None:
            num_paths += 1
            pathcount[curr.guid] = 1
        else:
            try:
                pathcount[curr.guid] = (
                    pathcount[curr.left.guid] + pathcount[curr.right.guid]
                )
                num_paths += pathcount[curr.guid]
            except KeyError:
                if curr.left:
                    to_visit.append(curr.left)
                if curr.right:
                    to_visit.append(curr.right)
    return num_paths


def part2():
    root = Node(uuid.uuid4(), S, None, None)
    beams = [root]
    for k in range(K):
        # check for splitters
        splitter_locs = [i for i, val in enumerate(grid[k]) if val == "^"]
        split_beams = list(filter(lambda beam: beam.pos in splitter_locs, beams))
        for beam in split_beams:
            # beam splits
            if beam.pos - 1 > 0:
                try:
                    left_beam = [b for b in beams if b.pos == beam.pos - 1].pop()
                except IndexError:
                    left_beam = Node(uuid.uuid4(), beam.pos - 1, None, None)
                    beams.append(left_beam)
                beam.left = left_beam
            if beam.pos + 1 < N:
                try:
                    right_beam = [b for b in beams if b.pos == beam.pos + 1].pop()
                except IndexError:
                    right_beam = Node(uuid.uuid4(), beam.pos + 1, None, None)
                    beams.append(right_beam)
                beam.right = right_beam
            beams.remove(beam)

    return count_paths(root)


if __name__ == "__main__":
    print(part2())
