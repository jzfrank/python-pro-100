from replit import clear
from art import logo 
#HINT: You can call clear() to clear the output in the console.
print(logo)

num_participants = input("How many people are participating the auction?\n")
num_participants = int(num_participants)

name2price = {}
highest_offer = -1

while num_participants > 0:
	clear()
	name = input("What is your name?\n")
	price = int(input("What is your offer?\n"))
	name2price[name] = price
	highest_offer = max(price, highest_offer)
	num_participants -= 1 

for name, price in name2price.items():
	if price == highest_offer:
		print(f"{name} offers the hight price {highest_offer}.")
		print("auction ends")
		break 

