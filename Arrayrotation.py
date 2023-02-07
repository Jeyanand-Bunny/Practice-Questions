n=int(input())
a=list(int(x) for x in input().split())
sum=0
for i in a:
    sum+=i
    sum%=(1000000007)
q=int(input())
l1=list(int(x) for x in input().split())

for i in range(q):
    sum*=2
    sum%=(1000000007)
    print(sum)