import math

minValue = int(input("Enter the Minimum Value: "))
maxValue = int(input("Enter the Maximum Value: "))
for Number in range(minValue, maxValue):
    Temp = Number
    Sum = 0
    while(Temp > 0):
        Reminder = Temp % 10
        Factorial = math.factorial(Reminder)
        Sum = Sum + Factorial
        Temp = Temp // 10

    if (Sum == Number):
        print("%d is a Strong Number" %Number)
        totalStrongNo = totalStrongNo + 1
print(totalStrongNo)