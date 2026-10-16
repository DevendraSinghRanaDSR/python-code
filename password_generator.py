import random
print("This is a password generator")
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number=['0','1','2','3','4','5','6','7','8','9']
symbol=['!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','<','>','?','/']

password_list=[]
n_letter=int(input("Enter the number of letters: "))
n_number=int(input("Enter the number of numbers: "))
n_symbol=int(input("Enter the number of symbols: "))

for i in range(0,n_letter):
   password_list+=random.choice(letter)
for i in range(0,n_number):
    password_list+=random.choice(number)
for i in range(0,n_symbol):
    password_list+=random.choice(symbol)

random.shuffle(password_list)

password=""
for char in password_list:
    password+=char

print(f"Generated password: {password}")




