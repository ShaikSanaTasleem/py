
def print_list(list,index=0):
    if(len(list)==index):
        return
    print(list[index])
    print_list(list,index+1)
        
        
numbers=[10,20,30,40,50]   
print_list(numbers)




