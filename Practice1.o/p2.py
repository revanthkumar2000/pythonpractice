#maximum number b/w 3 numbers
num1=int(input("enter the number 1"))
num2=int(input("enter the number 2"))
num3=int(input("enter the number 3"))
if(num1>num2 and num1>num3):
    print("maximum number is ",num1)
elif(num2>num1 and num2>num3):
    print("maximum numberis ",num2)
else:
    print("maximum number is ",num3)