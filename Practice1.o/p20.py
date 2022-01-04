num=int(input("enter the number"))
lastdigit=num%10
print("last digit is",lastdigit)
while(num>0):
    firstdigit=num%10
    num=num//10
print("firast digit is",firstdigit)