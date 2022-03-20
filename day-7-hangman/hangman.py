import random 
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear
# import os

# word_list = ["aardvark", "baboon", "camel"]
life_left = 7


# game start and 
clear()
print(logo)
word = random.choice(word_list)
n = len(word)
revealed_word = ["_" for _ in range(n)]
print(f"The word generated is of length {n}, try to guess its characters one at a time.")
print(" ".join(revealed_word))
input("Press enter to continue\n")

while True:
	user_guess = input("Please have a guess (one character): \n")
	if len(user_guess) != 1:
		continue
	user_guess = user_guess.lower()
	if user_guess in revealed_word:
		print(f"You already guessed {user_guess}, try new one")
	elif user_guess not in word:
		life_left -= 1
		if life_left <= 0:
			print("You run out of life, game over!")
			print(f"The word is: {word}")
			break 
		else:
			print(stages[life_left-1])
			print(f"You guessed wrong, you got {life_left} lives.")
	else:
		revealed_word_len = 0
		for i in range(n):
			if word[i] == user_guess:
				revealed_word[i] = user_guess
			if revealed_word[i] != "_":
				revealed_word_len += 1 
		print(" ".join(revealed_word))
		if revealed_word_len == n:
			print("You Win, game over!")
			break 
	

