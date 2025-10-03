n=int(input("enter a number: "))
def natural_sum(n):
    
    if(n==0):
        return 0
    return natural_sum(n-1)+n



print(natural_sum(n))
natural_sum(n)

