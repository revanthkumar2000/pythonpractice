#multiplication table
num1=int(input("enter the multiplication number"))
num2=int(input("enter the upto number"))
for i in range(0,num2+1,1):
    table=num1*i
    print(num1,"*",i,"=",table)