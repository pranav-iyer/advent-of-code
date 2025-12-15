from dataclasses import dataclass

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

type Indicators = list[bool]
type Button = list[int]


def push_button(ind: Indicators, button: Button) -> Indicators:
    return [not x if i in button else x for i, x in enumerate(ind)]


@dataclass
class Machine:
    target_indicators: Indicators
    buttons: list[Button]
    target_joltages: list[int]

    @property
    def N(self):
        return len(self.target_indicators)

    def test_button_presses(self, n: int, start=None):
        """can this machine's indicators be satisfied in n presses starting at start"""
        if start is None:
            start = [False for _ in range(self.N)]
        if n == 0:
            return self.target_indicators == start
        if n == 1:
            for button in self.buttons:
                if push_button(start, button) == self.target_indicators:
                    return True
        for button in self.buttons:
            if self.test_button_presses(n - 1, push_button(start, button)):
                return True
        return False

    def count_button_presses(self):
        for i in range(10):
            if self.test_button_presses(i):
                return i
        raise RuntimeError("Unsatisfiable in 10 presses")


def parse_machine(line: str) -> Machine:
    items = line.split(" ")
    target_indicators = [c == "#" for c in items[0][1:-1]]
    buttons = [[int(x) for x in item[1:-1].split(",")] for item in items[1:-1]]
    target_joltages = [int(x) for x in items[-1][1:-1].split(",")]
    return Machine(target_indicators, buttons, target_joltages)


machines = [parse_machine(line) for line in lines]


def part1():
    total = 0
    for machine in machines:
        bp = machine.count_button_presses()
        print(bp)
        total += bp
    print("total", total)


def part2():
    for machine in machines:
        p = 1
        for j in machine.target_joltages:
            p *= j
        print(p)


print(part2())
