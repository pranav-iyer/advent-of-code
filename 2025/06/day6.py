with open("input.txt", "r") as f:
    lines = [line for line in f.readlines() if line.strip()]


assert all(len(line) == len(lines[0]) for line in lines)


def part1():
    N = len(lines[0])

    i = 0
    iprev = 0
    result = 0
    while i < N:
        if all(line[i] == " " for line in lines):
            print(i, iprev)
            # it's a blank space, compute result
            op = lines[-1][iprev:i].strip()
            if op == "*":
                prod = 1
                for line in lines[:-1]:
                    prod *= int(line[iprev:i].strip())
                result += prod
            elif op == "+":
                result += sum(int(line[iprev:i].strip()) for line in lines[:-1])
            else:
                raise RuntimeError(f"Unknown operation {op}")

            i += 1
            iprev = i
        else:
            i += 1

    result += sum(int(line[iprev:].strip()) for line in lines[:-1])
    print(result)


def part2():
    N = len(lines[0])

    i = 0
    iprev = 0
    result = 0
    while i < N:
        if all(line[i] == " " for line in lines):
            # it's a blank space, compute result
            op = lines[-1][iprev:i].strip()
            if op == "*":
                prod = 1
                for j in range(iprev, i):
                    prod *= int("".join(line[j] for line in lines[:-1]).strip())
                result += prod
            elif op == "+":
                result += sum(
                    int("".join(line[j] for line in lines[:-1]).strip())
                    for j in range(iprev, i)
                )
            else:
                raise RuntimeError(f"Unknown operation {op}")

            i += 1
            iprev = i
        else:
            i += 1

    result += sum(
        int("".join(line[j] for line in lines[:-1]).strip())
        for j in range(iprev, N - 1)
    )
    print(result)


part2()
