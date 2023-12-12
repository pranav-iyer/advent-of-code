# from pprint import pprint

# stacks = [[] for _ in range(9)]

# with open('input.txt', 'r') as f:
#     line = f.readline().strip()
#     while True:
#         print(line)
#         if line[0] == '1':
#             break

#         for i in range(9):
#             c = line[1 + 4*i]
#             if c != ' ':
#                 stacks[i].append(c)

#         line = f.readline().strip()

#     for i in range(9):
#         stacks[i] = list(reversed(stacks[i]))

#     f.readline()

#     line = f.readline().strip()
#     while True:
#         print(line)
#         if line == '':
#             break

#         num, frm, to = [int(x) for x in line.split()[1::2]]
#         for _ in range(num):
#             stacks[to-1].append(stacks[frm-1].pop())

#         line = f.readline().strip()



# for s in stacks:
#     print(s[-1], end='')

from pprint import pprint

stacks = [[] for _ in range(9)]

with open('input.txt', 'r') as f:
    line = f.readline().strip()
    while True:
        print(line)
        if line[0] == '1':
            break

        for i in range(9):
            c = line[1 + 4*i]
            if c != ' ':
                stacks[i].append(c)

        line = f.readline().strip()

    for i in range(9):
        stacks[i] = list(reversed(stacks[i]))

    f.readline()

    line = f.readline().strip()
    while True:
        print(line)
        if line == '':
            break

        num, frm, to = [int(x) for x in line.split()[1::2]]

        to_move = stacks[frm-1][-num:]
        stacks[frm-1] = stacks[frm-1][:-num]
        stacks[to-1].extend(to_move)

        line = f.readline().strip()



for s in stacks:
    print(s[-1], end='')
