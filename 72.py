n=int(input("enter n: "))
def num(n):
    if(n==-1):
        return -1
    print(n)
    num(n-1)

num(n)