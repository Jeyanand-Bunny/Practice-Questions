n=int(input())
for i in range(n):
    num=int(input())
    if(num%2==0):
        a=['0']*num
        flag=0
        for i in range(int(num/2)):
            if(flag==0):
                a[i]=a[num-i-1]=1
                flag=1
            elif(flag==1):
                a[i]=a[num-i-1]=0
                flag=0
    else:
        a=['1']*num
        flag=0
        for i in range(int(num/2)):
            if(flag==0):
                a[i]=a[num-i-1]=0
                flag=1
            elif(flag==1):
                a[i]=a[num-i-1]=1
                flag=0
    
    
    for i in a:
        print(i,end='')
    print('')