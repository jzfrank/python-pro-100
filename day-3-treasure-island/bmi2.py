height = input("What is your height? (in m) \n")
weight = input("What is your weight? (in kg)\n")

height = float(height)
weight = float(weight)

bmi = int(weight / height ** 2)


message = f"Your bmi is: {bmi}. "
if bmi < 18.5:
	message += "Underweight"
elif bmi < 25:
	message += "Normal weight"
elif bmi < 30:
	message += "Overweight"
elif bmi < 35:
	message += "Obese"
else:
	message += "Clinically obese"
print(message)