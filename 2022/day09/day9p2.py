with open("input.txt", "r") as f:
    insts = [tuple(l.strip().split()) for l in f.readlines()]
    insts = [(x, int(y)) for x, y in insts]


visited = set()
visited.add((0, 0))


class Knot:
    def __init__(self, before: "Knot | None", after: "Knot | None"):
        self.before = before
        self.after = after
        self.i = 0
        self.j = 0

    def adjust(self):
        if self.before is None:
            return

        before_i, before_j = self.before.i, self.before.j

        if before_j > self.j + 1:
            # above
            if before_i < self.i - 1:
                # above left
                self.j = before_j - 1
                self.i = before_i + 1
            elif before_i > self.i + 1:
                # above right
                self.j = before_j - 1
                self.i = before_i - 1
            else:
                # above center
                self.j = before_j - 1
                self.i = before_i
        elif before_j < self.j - 1:
            # below
            if before_i < self.i - 1:
                # below left
                self.j = before_j + 1
                self.i = before_i + 1
            elif before_i > self.i + 1:
                # below right
                self.j = before_j + 1
                self.i = before_i - 1
            else:
                # below center
                self.j = before_j + 1
                self.i = before_i
        else:
            # middle horizontally
            if before_i < self.i - 1:
                # left center
                self.i = before_i + 1
                self.j = before_j
            elif before_i > self.i + 1:
                # right center
                self.i = before_i - 1
                self.j = before_j
            else:
                # center center, no adjustment
                pass


class Rope:
    def __init__(self):
        self.head = Knot(None, None)
        curr = self.head

        for _ in range(9):
            new_node = Knot(curr, None)
            curr.after = new_node
            curr = new_node

        self.tail = curr

    def go(self, d):
        oldi, oldj = self.head.i, self.head.j
        if d == "L":
            self.head.i -= 1
        elif d == "R":
            self.head.i += 1
        elif d == "U":
            self.head.j += 1
        elif d == "D":
            self.head.j -= 1

        print("go direction", d)

        print("head", oldi, oldj, "==>", self.head.i, self.head.j)

        self.propagate()

        print("visited", (self.tail.i, self.tail.j))
        visited.add((self.tail.i, self.tail.j))

    def propagate(self):
        curr = self.head.after
        while curr is not None:
            curr.adjust()
            curr = curr.after


r = Rope()
for inst in insts:
    for j in range(inst[1]):
        r.go(inst[0])

print(len(visited))
