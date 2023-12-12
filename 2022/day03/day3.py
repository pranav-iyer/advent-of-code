import string

# total = 0
# with open('input.txt', 'r') as f:
#     for line in f.readlines():
#         line = line.strip()
#         ln = len(line)
#         assert ln % 2 == 0
#         left = set(line[:ln//2])
#         right = set(line[ln//2:])

#         c = left.intersection(right).pop()

#         if c in string.ascii_lowercase:
#             total += 1 + string.ascii_lowercase.index(c)
#         else:
#             total += 27 + string.ascii_uppercase.index(c)

# print(total)



total = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        line1 = lines[i].strip()
        line2 = lines[i + 1].strip()
        line3 = lines[i + 2].strip()

        c = set(line1).intersection(line2).intersection(line3).pop()

        if c in string.ascii_lowercase:
            total += 1 + string.ascii_lowercase.index(c)
        else:
            total += 27 + string.ascii_uppercase.index(c)

print(total)