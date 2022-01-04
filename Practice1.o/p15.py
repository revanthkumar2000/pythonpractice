#sum of all natural numbers from 1 to n
i=int(input("enter the starting value"))
num=int(input("enter the upto number"))
sum=0
while(i<num):
    print(i)
    sum=sum+i
    print("sum of all natural numbers is:",sum)
    i=i+2