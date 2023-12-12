from heapq import nlargest


def main():
    data = []
    with open("input.txt", 'r') as f:
        curr = []
        line = f.readline()
        while line != '':
            if line.strip() == '':
                data.append(curr)
                curr = []
            else:
                curr.append(int(line.strip()))
            line = f.readline()

        data.append(curr)

    sums = [sum(row) for row in data]
    print(sum(nlargest(3, sums)))




if __name__ == '__main__':
    main()