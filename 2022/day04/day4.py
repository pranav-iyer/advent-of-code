from itertools import chain

total = 0

def inrange(x, a, b):
    return a <= x and x <= b

def overlap(x, y, a, b):
    if x < a and inrange(y, a,b):
        return True
    elif inrange(x,a,b) and y > b:
        return True

with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        lo1, hi1, lo2, hi2 = [int(x) for x in chain(*(rng.split('-') for rng in line.split(',')))]

        if lo1 <= lo2 and hi1 >= hi2:
            total += 1
        elif lo2 <= lo1 and hi2 >= hi1:
            total += 1
        elif inrange(lo1, lo2, hi2) or inrange(hi1, lo2, hi2) or inrange(lo2, lo1, hi1) or inrange(hi2, lo1, hi1):
            total += 1
        

print(total)
