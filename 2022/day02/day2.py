
# opp_symbs = {'A': 1, 'B': 2, 'C': 3}
# my_symbs = {'X': 1, 'Y': 2, 'Z': 3}

# total = 0
# with open('input.txt', 'r') as f:
#     for line in f.readlines():
#         opp, my = line.strip().split()
#         opp = opp_symbs[opp]
#         my = my_symbs[my]
#         if (my, opp) in [(1,3), (2,1), (3,2)]:
#             total += 6
#         elif my == opp:
#             total += 3
         
#         total += my
        


# print(total)

opp_symbs = {'A': 1, 'B': 2, 'C': 3}

out_symbs = {'X': -1, 'Y': 0, 'Z': 1}
total = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        opp,out = line.strip().split()
        opp = opp_symbs[opp]
        out = out_symbs[out]

        if out == 0:
            total += 3
        elif out == 1:
            total += 6

        my = opp + out
        if my == 0: my = 3
        if my == 4: my = 1
        total += my


print(total)