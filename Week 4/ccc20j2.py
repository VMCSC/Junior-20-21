p = int(input())
n = int(input())
r = int(input())
total = 0
d = 0

if r == 1:
    print(p//n)
else:
    while True:
        if total > p:
            break
        total += (r**d)*n
        d+=1
    print(d-1)