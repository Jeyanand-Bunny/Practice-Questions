n=int(input())
for i in range(n):
    num=int(input())
    s=input()
    if(num%2==0):
        d1={}
        flag=0
        for k in s:
            if k in d1:
                d1[k]+=1
            else:
                d1[k]=1
        for k in d1:
            if(d1[k]%2!=0):
                print("NO")
                flag=1
                break
        if(flag==0):    
            print("YES")
    else:
        print("NO")