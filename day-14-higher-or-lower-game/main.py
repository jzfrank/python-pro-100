from art import logo, vs 
from game_data import data 
import random 
from replit import clear

def describe(person):
	res = f"{person['name']}, a {person['description']}, from {person['country']}"
	return res 

def get_winner(A, B):
	if A['follower_count'] > B['follower_count']:
		winner = 'A'
	else:
		winner = 'B'
	return winner


score = 0 
A = random.choice(data)

while True:
	clear()
	print(logo)
	B = random.choice(data)
	while B == A:
		B = random.choice(data)

	winner = get_winner(A, B)
	print("Compare A: " + describe(A))
	print(vs)
	print("Against B: " + describe(B))

	guess =  input("Who has more followers? Type 'A' or 'B': ")
	if guess == winner:
		score += 1
		print(f"You are right! Current score: {score}.")
		A = B 
	else:
		print(f"Sorry, that's wrong. Final score: {score}")
		break 
