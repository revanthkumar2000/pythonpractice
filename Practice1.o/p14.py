englisgh=int(input("enter the english marks:"))
math=int(input("enter the math marks:"))
physics=int(input("enter the physics marks:"))
chemistry=int(input("enter the chemistry marks:"))
oriya=int(input("enter the oriya marks:"))
total=englisgh+math+physics+chemistry+oriya
percentage=(total//500)*100
    if(percentage>=90):
        print("A grade")
    elif englisgh>=80:
        print("B grade")
    elif englisgh>=70:
        print("C grade")
    else:
        print("fail")
for j in range(math): 
    if math>=90:
        print("A grade")
    elif math>=80:
        print("B grade")
    elif math>=70:
        print("C grade")
    else:
        print("fail")