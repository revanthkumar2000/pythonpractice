#product of digts in the given number
num=int(input("enter the number"))
product=1
while(num>0):
    digit=num%10
    product=product*digit
    num=num//10
print("product of digits in the given number :",product)