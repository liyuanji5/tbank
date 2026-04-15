import sys

class MyStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        if self.items:
            self.items.append((item, min(item, self.items[-1][1])))
        else:
            self.items.append((item, item))

    def pop(self):
        return self.items.pop()[0]

    def min(self):
        return self.items[-1][1]


input = sys.stdin.readline
out_lines = []

n = int(input())
stack = MyStack()

for _ in range(n):
    operation = input().split()
    if operation[0] == '1':
        stack.push(int(operation[1]))
    elif operation[0] == '2':
        stack.pop()
    else:  # operation[0] == '3'
        out_lines.append(str(stack.min()))

sys.stdout.write('\n'.join(out_lines))
