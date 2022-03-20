age = input("What is your current age?\n")
age = int(age)
life_in_days = (90-age) * 365
life_in_weeks = (90-age) * 52
life_in_months = (90-age) * 12

print(f"You have {life_in_days} days, {life_in_weeks} weeks, and {life_in_months} months left.")