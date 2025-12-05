# Tip Calculator
print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill: \n>$"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15\n> "))
people = int(input("To how many people are you splitting the bill: \n> "))
total_bill = tip / 100 * bill + bill
print(f"The total bill is: {total_bill}")
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")

