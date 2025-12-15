def count_zeros(lines) -> int:
    zero_count = 0
    curr = 50
    for line in lines:
        amount = int(line[1:])
        if line.startswith("L"):
            curr = (curr - amount) % 100
        else:
            curr = (curr + amount) % 100
        if curr == 0:
            zero_count += 1
    return zero_count


def count_all_zeros(lines) -> int:
    zero_count = 0
    curr = 50
    for line in lines:
        amount = int(line[1:])
        if line.startswith("L"):
            next = curr - amount
            while next < 0:
                next += 100
                zero_count += 1
            curr = next
        else:
            next = curr + amount
            while next > 99:
                next -= 100
                zero_count += 1
            curr = next
    if curr == 0:
        zero_count += 1
    return zero_count


with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines() if l.strip() != ""]

print(count_zeros(lines))
print(count_all_zeros(lines))

print(
    count_all_zeros(
        ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    )
)
