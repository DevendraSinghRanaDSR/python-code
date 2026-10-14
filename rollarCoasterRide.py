print("Welcome to the rollar coaster!")
height=float(input("enter height in cm:"))
bill=0
if height>=120:
    print("you are tall enoghf to ride the roller coster")
    age=int(input("enter your age:"))
    if age<12:
        bill=12
        print("pay 12 dollars")
    elif 12<=age<=18:
        bill=15
        print("pay 15 dollars")
    elif age>=45 and  age<=55:
        bill=0
        print("you can ride for free")
    else:
        bill=20
        print("pay 20 dollars")

    want_photo=input("do you want a photo taken? Y or N: ")
    if want_photo=="Y":
        bill+=2

    print(f"your totl bill is ${bill}")
else:
    print("Sorry! you are not tall enough to ride a rollar coaster")