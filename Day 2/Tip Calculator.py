print("Welcom to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total = (total_bill + (total_bill * percentage / 100)) / people

print(f"Each person should pay: ${total:.2f}")
