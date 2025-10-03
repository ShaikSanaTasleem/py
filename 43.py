nums=(1,4,9,16,25,36,49,64,81)
x=int(input("enter x: "))
index=0
for el in nums:
    if(el==x):
        print("found at index: ",index)
        break
    index+=1
    