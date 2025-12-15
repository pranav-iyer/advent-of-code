from dataclasses import dataclass
import bisect
import math
import functools
from uuid import UUID, uuid4

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]


@dataclass
class Point:
    guid: UUID
    x: int
    y: int
    z: int

    def __str__(self):
        return f"{str(self.guid)[:5]} [{self.x}, {self.y}, {self.z}]"

    def __repr__(self):
        return f"Pt {str(self.guid)[:5]} [{self.x}, {self.y}, {self.z}]"


edges: set[tuple[int, int]] = set()
points = [Point(uuid4(), *(int(x) for x in line.split(","))) for line in lines]
distances: dict[tuple[str, str], float] = dict()


def distance(i, j):
    return math.sqrt(
        (points[i].x - points[j].x) ** 2
        + (points[i].y - points[j].y) ** 2
        + (points[i].z - points[j].z) ** 2
    )


N = len(points)


@dataclass
class Info:
    dist: float
    i: int
    j: int

    def __str__(self):
        return f"{self.dist:.0f} [{self.i} {self.j}]"

    def __repr__(self):
        return f"{self.dist:.0f} [{self.i} {self.j}]"


N_top = 999
N_to_keep = N_top * 13

# find 1000 closest distances
closest: list[Info] = []
for i in range(N):
    for j in range(i + 1, N):
        bisect.insort_left(closest, Info(distance(i, j), i, j), key=lambda x: x.dist)
        if len(closest) > N_to_keep:
            closest = closest[:N_to_keep]


def clump_id(clumps, guid: str) -> int | None:
    matching = [i for i, clump in enumerate(clumps) if guid in clump]
    if matching:
        return matching[0]
    else:
        return None


# now closest stores the edges, we have to sort them into clumps
print(closest)
num_added = 0
clumps: list[set[str]] = []
for inf in closest:
    if num_added >= N_top:
        break
    left = points[inf.i]
    right = points[inf.j]
    leftid = clump_id(clumps, str(left.guid))
    rightid = clump_id(clumps, str(right.guid))
    print(num_added, leftid, rightid)
    if leftid is not None and rightid is not None:
        if leftid == rightid:
            # same clump, doesn't count
            continue
        else:
            # merge clumps
            rightclump = clumps[rightid]
            clumps[leftid] |= rightclump
            clumps.pop(rightid)
    elif rightid is not None:
        # add left node to right clump
        clumps[rightid].add(str(left.guid))
    elif leftid is not None:
        # add right node to left clump
        clumps[leftid].add(str(right.guid))
    else:
        clumps.append({str(left.guid), str(right.guid)})
    num_added += 1

print(left, right)
print(sorted([len(s) for s in clumps]))
