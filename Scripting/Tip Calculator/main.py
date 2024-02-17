print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_to_split = int(input("How many people to split the bill? "))
bill_per_person = (total_bill + (total_bill * percentage / 100)) / people_to_split
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
