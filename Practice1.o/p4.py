# number is divisible by 5 and 11
num=int(input("enter the number"))
if(num%5==0):
    print("divisible by 5")
elif(num%11==0):
    print("divisible by 11")
else:
    print("given number is not divisible by 5 and 11")