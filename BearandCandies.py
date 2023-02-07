t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    i=1
    while True:
        if(i%2==0):
            if(b>0 and b>=i):
                b-=i
                i+=1
            else:
                print('Limak')
                break
        else:
            if(a>0 and a>=i):
                a-=i
                i+=1
            else:
                print('Bob')
                break