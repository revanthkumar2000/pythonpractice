num=int(input("enter the number"))
sum=0
lastdigit=num%10
print("last digit is :",lastdigit)
while(num>0):
    firstdigit=num%10
    num=num//10
print("first digit is :",firstdigit)
sum=lastdigit+firstdigit
print("sum of first and last digit is :",sum)