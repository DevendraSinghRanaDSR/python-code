#tip calculator
bill=float(input("Enter the total bill amount $:"))
tip=int(input("Enter the tip percentage you would like to give (10,15,20): "))
total_bill=((100+tip)/100)*bill
n=int(input("Enter the number of person who will divide the bill: "))
print(f"each person should pay $:{total_bill/n:.2f}")
