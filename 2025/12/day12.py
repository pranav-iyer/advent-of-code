from dataclasses import dataclass

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

shapes = list(zip(lines[1:24:4], lines[2:24:4], lines[3:24:4]))
shapes = [[[int(c == "#") for c in row] for row in shape] for shape in shapes]
shape_sizes = [sum(sum(row) for row in shape) for shape in shapes]


@dataclass
class Region:
    size: tuple[int, int]
    counts: list[int]

    @property
    def N_spaces(self):
        return self.size[0] * self.size[1]

    @property
    def N_shape_squares(self):
        total = 0
        for sz, cnt in zip(shape_sizes, self.counts):
            total += sz * cnt
        return total

    @property
    def N_shapes(self):
        return sum(self.counts)

    @property
    def N_3x3_grids(self):
        return (self.size[0] // 3) * (self.size[1] // 3)


regions = [
    (
        Region(
            tuple(int(n) for n in line.split(":")[0].strip().split("x")),
            [int(n) for n in line.split(":")[1].strip().split(" ")],
        )
    )
    for line in lines[24:]
]


N_bad = 0
N_indefinite = 0
N_good = 0
for reg in regions:
    if reg.N_shape_squares > reg.N_spaces:
        N_bad += 1
    elif reg.N_3x3_grids >= reg.N_shapes:
        N_good += 1
    else:
        print(reg, reg.N_shape_squares, reg.N_spaces, reg.N_3x3_grids, reg.N_shapes)
        N_indefinite += 1
print(N_bad, N_indefinite, N_good)
