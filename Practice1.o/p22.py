num=int(input("enter the number"))
orgnum=num
revenum=0
while(num>0):
    reminder=num%10
    revenum=revenum*10+reminder
    num=num//10
if(revenum==orgnum):
    print(orgnum,"yes it is a palandrome number")
else:
    print(orgnum,"no it is not a palandrome number")