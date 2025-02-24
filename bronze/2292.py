import sys
num = int(sys.stdin.readline())

depth = 1
sum = 1
i = 0

while num > sum:
    depth += 1
    i += 1
    sum += i*6
print(depth)