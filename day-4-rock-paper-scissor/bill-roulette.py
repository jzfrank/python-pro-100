import random 


names = input("Input the participants' name, seperated by a comma.\n")
print(names.split(","))
names = names.split(",")
random_index = random.randint(0, len(names)-1)
# person_to_pay = names[random_index]
person_to_pay = random.choice(names)
print(f"{person_to_pay} should pay the bill!")

