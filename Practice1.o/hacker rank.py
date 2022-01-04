string=input("enter the string")
slength = len(string)
for s in range(slength):
  if s%2==0:
    print(string[s])