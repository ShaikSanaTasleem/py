a=int(input("enter a: "))

if(a%3==0 and a%5==0):
    print("QUIZZ BUZZ")
elif(a%5==0):
    print("BUZZ")
elif(a%3==0 ):
    print("FIZZ ")
else:
    print("not divisible by 3 and 5")