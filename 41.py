nums=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter x: "))
idx=0
while idx<len(nums):
    if (nums[idx]==x):
        print("found at idx is: ",idx)
    else:
        print("not found the x in tuple of nums")
        break
    

    idx+=1


 

