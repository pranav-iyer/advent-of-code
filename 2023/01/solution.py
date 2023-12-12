with open("input.txt", "r") as f:
    input = f.read()

three_letter_digits = {
    "one": 1,
    "two": 2,
    "six": 6,
}
four_letter_digits = {
    "four": 4,
    "five": 5,
    "nine": 9,
}
five_letter_digits = {
    "three": 3,
    "seven": 7,
    "eight": 8,
}

result = 0
for line in input.splitlines():
    print(line)
    first_digit = -1
    for i, c in enumerate(line):
        if c.isdigit():
            first_digit = int(c)
            break
        if line[i : i + 3] in three_letter_digits:
            first_digit = three_letter_digits[line[i : i + 3]]
            break
        if line[i : i + 4] in four_letter_digits:
            first_digit = four_letter_digits[line[i : i + 4]]
            break
        if line[i : i + 5] in five_letter_digits:
            first_digit = five_letter_digits[line[i : i + 5]]
            break

    last_digit = -1
    for i, c in enumerate(line):
        if c.isdigit():
            last_digit = int(c)
        if line[i : i + 3] in three_letter_digits:
            last_digit = three_letter_digits[line[i : i + 3]]
        if line[i : i + 4] in four_letter_digits:
            last_digit = four_letter_digits[line[i : i + 4]]
        if line[i : i + 5] in five_letter_digits:
            last_digit = five_letter_digits[line[i : i + 5]]

    result += 10 * first_digit + last_digit
print(result)
