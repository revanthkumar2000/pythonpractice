#to print the given number in reverse order
num=int(input("enter the number"))
reversenum=0
while(num>0):
    digit=num%10
    reversenum=reversenum*10+digit
    num=num//10
print("the number in reverse order is :" ,reversenum)