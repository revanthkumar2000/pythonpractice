#check alphabet or number or specal char
ch=(input("enter the char or number"))
if(ch>='A' and ch<='Z' or ch>='a' and ch<='z'):
    print("alphabet")
elif(ch>='0' and ch<='9'):
    print("number")
else:
    print("specal char")