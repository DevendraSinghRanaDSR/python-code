weight=float(input("enter weight in kg:"))
height=float(input("enter height in m:"))
bmi=weight/(height**2)
if bmi<18.5:
    print("Under weight")
elif 18.5<=bmi<25:
    print("normal weight")
elif 25<=bmi<30:
    print("over weight")