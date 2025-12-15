with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]


def max_joltage(line: str) -> int:
    first_digit = max(line[:-1])
    first_idx = line.find(first_digit)
    last_digit = max(line[first_idx + 1 :])
    return int(first_digit) * 10 + int(last_digit)


def max_joltage_12(line: str) -> int:
    sum = 0
    left_idx = 0
    for digit_idx in range(12):
        if digit_idx == 11:
            next_digit = max(line[left_idx:])
        else:
            next_digit = max(line[left_idx : digit_idx - 11])
        left_idx += line[left_idx:].find(next_digit) + 1
        sum += int(next_digit) * 10 ** (11 - digit_idx)
    print(line)
    print(sum)
    return sum


print(sum(max_joltage_12(line) for line in lines))
