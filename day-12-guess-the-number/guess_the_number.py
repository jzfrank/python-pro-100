from art import logo 
import random 
EASY_LEVEL_TURNS = 12
HARD_LEVEL_TURNS = 7
print(logo)

def set_difficulty():
	difficulty_level = input("What difficulty level do you choose?" + 
	" (type 'easy' or 'hard'): \n")
	if difficulty_level == "easy":
		return EASY_LEVEL_TURNS
	else:
		return HARD_LEVEL_TURNS

def check_answer(user_guess, generated_num):
	if user_guess == generated_num:
		print("Game over, you win!")
		return True
	elif user_guess > generated_num:
		print("Too large, try again.")
	else:
		print("Too small, try again.")
	return False 

generated_num = random.randint(1, 100)
print("I am thinking about a number between 1 and 100, can you guess it? ")
life_remains = set_difficulty()

while True:
	print(f"You have {life_remains} lives left.")
	user_guess = int(input("Take a guess: "))
	if check_answer(user_guess, generated_num):
		break 
	life_remains -= 1 
	if life_remains <= 0:
		print("You run out of life, game over!")
		print(f"This is what I think: {generated_num}")
		break


