num=int(input("entyer the number"))
reversenum=0
while(num>0):
    reminder=num%10
    reversenum=reversenum*10+reminder
    num=num//10
print(reversenum)