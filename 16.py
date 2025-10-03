a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))
if(a<b and a>c):
    print("a is middle number")
elif(b<a and b>c):
    print("b is middle")
elif(c<a and c>a):
    print("cis middle")