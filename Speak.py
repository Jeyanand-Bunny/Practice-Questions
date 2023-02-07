vow='aeiou'
def main():
    n=int(input())
    s=input()
    flag=0
    for i in s:
        if i in vow:
            flag=0
        else:
            flag+=1
        if(flag>=4):
            print("NO")
            break
    if(flag<4):
        print("YES")

t=int(input())
for i in range(t):
    main()
