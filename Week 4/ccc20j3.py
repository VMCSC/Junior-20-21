drops = int(input())
xA = []
yA = []
for i in range(drops):
    x, y = map(int, input().split(","))
    xA.append(x)
    yA.append(y)

xA.sort()
yA.sort()
print("%i,%i" %(xA[0]-1, yA[0]-1))
print("%i,%i" %(xA[-1]-1, yA[-1]-1))