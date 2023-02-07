n=int(input())
for i in range(n):
    a=list(int(x) for x in input().split())
    if(a[0]+a[1]==a[2]) or (a[0]+a[2]==a[1]) or (a[1]+a[2]==a[0]):
        print('YES')
    else:
        print('NO')