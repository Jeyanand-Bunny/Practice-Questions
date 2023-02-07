s=input()
n=int(input())

for i in range(n):
    s1=input()
    flag=0
    for j in s1:
        if j not in s:
            print("No")
            flag=1
            break
    if(flag==0):
        print("Yes")