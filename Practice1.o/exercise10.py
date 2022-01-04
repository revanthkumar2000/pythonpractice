list1=[]
num=int(input("enter the size of list"))
print("enter the elements")
for i in range(0,num):
    data=int(input())
    list1.append(data)
print(list1)
for j in list1:
    if(j%2!=0):
        print(j,end=" ")