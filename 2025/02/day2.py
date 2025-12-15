with open("input.txt", "r") as f:
    data = f.readline()
ranges = data.strip().split(",")
ranges = [tuple(int(x) for x in rng.split("-")) for rng in ranges]


def is_invalid(ID: int) -> bool:
    idstr = str(ID)
    N = len(idstr)
    if N % 2 == 1:
        return False

    return idstr[: N // 2] == idstr[N // 2 :]


def is_invalid_2(ID: int) -> bool:
    idstr = str(ID)
    N = len(idstr)
    for i in range(1, (N // 2) + 1):
        if N % i != 0:
            continue
        ref = idstr[:i]
        for j in range(1, N // i):
            if idstr[j * i : (j + 1) * i] != ref:
                break
        else:
            return True

    return False


sum = 0
for rng in ranges:
    print("completed", rng)
    for i in range(rng[0], rng[1] + 1):
        if is_invalid_2(i):
            sum += i

print(sum)
