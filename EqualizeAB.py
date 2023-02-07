n=int(input())
for i in range(n):
    a,b,x=map(int,input().split())
    diff=abs(a-b)
    if(diff%(2*x)==0):
        print("YES")
    else:
        print("NO")

# https://www.codechef.com/problems/EQUALIZEAB