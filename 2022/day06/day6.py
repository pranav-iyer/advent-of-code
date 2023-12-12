
f = open("input.txt", "r")
line = f.read().strip()
i = 13
while i < len(line):
    print(set(line[i-13:i+1]))
    if len(set(line[i-13:i+1])) == 14:
        print(i)
        break

    i += 1
