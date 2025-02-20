iter = int(input())
for i in range(iter):
    string = input()
    sum = 0
    is_valid = True

    for k in string:
        if k == ")" :
            sum -= 1
            if sum < 0 :
                is_valid = False
                break
        else :
            sum += 1
    if sum != 0 or not is_valid:
        print("NO")
    else:
        print("YES")