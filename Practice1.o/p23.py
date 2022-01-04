#sum of digits in the given nuumber
num=int(input("enter the number"))
sum=0
while(num>0):
    reminder=num%10
    sum=sum+reminder
    num=num//10
print("sum of digits in the given number is :",sum)