import sys
stack = []
i_size = int(sys.stdin.readline())

def process(command, value=0):
    if command == "push":
        stack.append(value)
    elif command == "pop":
        print(stack.pop() if stack else -1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        print(0 if stack else 1)
    elif command == "top":
        print(stack[-1] if stack else -1)
    return

for i in range(i_size):
    inputs = sys.stdin.readline().split()
    if len(inputs) == 1:
        process(inputs[0])
    elif len(inputs) == 2:
        process(command=inputs[0], value=int(inputs[1]))
