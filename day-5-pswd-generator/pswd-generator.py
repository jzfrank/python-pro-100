import random 
letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!@#$%^&*()")

print("Welcome to the pyPassword Generator! ")
nr_letters = int(input("How many letter would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like\n"))

pswd = []
for i in range(nr_symbols):
	pswd.append(random.choice(symbols))
for i in range(nr_numbers):
	pswd.append(random.choice(numbers))
for i in range(nr_letters):
	pswd.append(random.choice(letters))
random.shuffle(pswd)
pswd = "".join(pswd)

print(f"You generated password is: {pswd}")