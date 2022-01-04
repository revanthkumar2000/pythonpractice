str1=input("enter the string 1:")
str2=input("enter the string 2:")
count=0
for i in range(len(str1)):
    for j in range(i,i+1):
        if str1[i]==str2[j]:
            count=count+1
print(count)