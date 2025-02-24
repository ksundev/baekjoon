import sys
word = list(sys.stdin.readline().strip().upper())
chars = set(word.copy())
ans = "?"
tmp = -1

for c in chars:
    if word.count(c) > tmp:
        tmp = word.count(c)
        ans = c
    elif word.count(c) == tmp:
        ans = "?"

print(ans)