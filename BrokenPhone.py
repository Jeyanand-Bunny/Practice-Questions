# cook your dish here
t=int(input())
for x in range(t):
    i=int(input())
    a=list(int(l) for l in input().split())
    ar=[0]*i
    count=0
    for j in range(i-1):
        if(a[j]!=a[j+1]):
            ar[j]+=1
            ar[j+1]+=1
    for k in ar:
        if k>0:
            count+=1
    print(count)