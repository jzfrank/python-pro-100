from art import logo 

print(logo)

def add(n1, n2):
	return n1+n2

def subtract(n1, n2):
	return n1-n2

def divide(n1, n2):
	return n1 / n2 

def multiply(n1, n2):
	return n1 * n2 

operations = {
	"+": add,
	"-": subtract,
	"/": divide,
	"*": multiply
}

def calculator():
	num1 = float(input("What is the first number?: "))
	for symbol in operations:
		print(symbol)

	should_continue = True 
	while should_continue:
		op = input("Pick an operation: ")
		num2 = float(input("What is the next number?: "))
		res = operations[op](num1, num2)
		num1 = res 
		print(f"{num1} {op} {num2} = {res}")
		yes_or_no = input(f"Type 'y' to continue calculating with {res}, or type 'n' to exit, or type 'c' to restart: ")
		if yes_or_no == 'n':
			should_continue = False 
		elif yes_or_no == 'c':
			calculator()
			return 


calculator()


