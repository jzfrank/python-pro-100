print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? \n$")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? \n")
num_person = input("How many people to split the bill? \n")

total_bill = float(total_bill)
percentage = float(percentage)
num_person = int(num_person)

avg = total_bill * (1 + percentage * 0.01) / num_person
avg = round(avg, 2)

print(f"Each person should pay ${avg}")

