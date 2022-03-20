print("Welcome to the Love Calculator!")
name1 = (input("What is your name? \n")).lower()
name2 = (input("What is your partner naem? \n")).lower()
combined_string = name1 + name2

letter2freq = {i: 0 for i in "truelov"}

for k, v in letter2freq.items():
	letter2freq[k] += combined_string.count(k)

love_score = (
	  (letter2freq['t'] + letter2freq['r'] + letter2freq['u'] + letter2freq['e']) * 10 
	+ (letter2freq['l'] + letter2freq['o'] + letter2freq['v'] + letter2freq['e'])
	)

if (love_score < 10) or (love_score > 90):
	print(f"Your score is {love_score}, you go together like coke and mentor.")
elif (love_score > 40) and (love_score < 50):
	print(f"Your score is {love_score}, you are alright together.")
else:
	print(f"Your score is {love_score}")

