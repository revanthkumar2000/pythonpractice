num=int(input("enter the multiplication number"))
num2=int(input("enter the maximum number"))
for i in range(0,num2+1,1):
    table=num*i
    print(num,"*",i,"=",table)