from collections import deque


class Dir:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.dirs = []
        self.size = 0

    def add_file(self, filename, size):
        self.files.append(filename)
        self.size += size

    def add_dir(self, dirname):
        self.dirs.append(Dir(dirname))

    def get_child_dir(self, dirname):
        for d in self.dirs:
            if d.name == dirname:
                return d

        raise ValueError(f"dirname {dirname} not found under {self.name}.")

    def get_child_file(self, filename):
        for f in self.files:
            if f == filename:
                return f

        raise ValueError(f"filename {filename} not found under {self.name}.")





f = open('input.txt', 'r')
lines = [l.strip() for l in f.readlines()]
f.close()

root = Dir('/')
cwd_stack = []

for line in lines:
    if line[0] == '$':
        # command line
        line = line[2:]
        if line[:2] == 'cd':
            if line[3:] == '..':
                cwd_stack.pop()
            elif line[3:] == '/':
                cwd_stack = [root]
            else:
                cwd_stack.append(cwd_stack[-1].get_child_dir(line[3:]))
    else:
        currDir = cwd_stack[-1]
        size, name = line.split()
        if size == 'dir':
            try:
                currDir.get_child_dir(name)
            except ValueError:
                currDir.add_dir(name)
        else:
            try:
                currDir.get_child_file(name)
            except ValueError:
                currDir.add_file(name, int(size))


# traverse and emit directories with size less than 
def get_size(d: Dir):
    size = 0
    size += d.size
    for c in d.dirs:
        size += get_size(c)
    return size

fs_size = 70000000
curr_used = get_size(root)
needed = 30000000 - (fs_size - curr_used)
print(needed)
total = 0
to_check = deque()
to_check.append(root)
min_found = curr_used
while len(to_check) > 0:
    curr = to_check.pop()
    currsize = get_size(curr)
    if currsize >= needed and currsize < min_found:
        print(currsize)
        min_found = currsize

    for d in curr.dirs:
        to_check.appendleft(d)

print(min_found)