import pprint
z=int(input())
lis=[]
for k in range(z):
    tempp=input()
    tempp=tempp.split()
    temp=[int(x) for x in tempp]
    #lis.append([int(x) for x in input().split()])
    lis.append(temp)
tt=int(input())
for k in range(tt):
    a,b=[int(x) for x in input().split()]
    a-=1
    b-=1
    ans=0
    for j in range(z):
        ans+=lis[a][j]
    for j in range(z):
        ans+=lis[j][b]
    print(ans)