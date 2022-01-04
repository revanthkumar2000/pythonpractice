num=int(input("enter the number"))
count=0
while(num>0):
    reminder=num%10
    count=count+1
    num=num//10
print("no of digits in the given number is :" ,count)