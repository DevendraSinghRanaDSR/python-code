a=int(input("enter 1:"))
b=int(input("Enter 2:"))
c=int(input("Enter 3:"))
d=int(input("Enter 4:"))
e=int(input("Enter 5:"))

total_marks=a+b+c+d+e
print("total marks:",total_marks)

p= (total_marks*100)/500
print(str(p)+"%")
if p>=40:
    print("pass")
else :
    print("fail")
print("thank you")    
