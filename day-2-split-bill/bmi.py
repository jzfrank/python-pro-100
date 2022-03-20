height = input("What is your height? (in m) \n")
weight = input("What is your weight? (in kg)\n")

height = float(height)
weight = float(weight)

print("Your bmi is: ", int(weight / height ** 2))