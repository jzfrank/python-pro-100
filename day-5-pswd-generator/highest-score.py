
scores = input("Input a list of scores:\n")
scores = scores.split()
for i in range(len(scores)):
	scores[i] = int(scores[i])

MM = scores[0]
for score in scores:
	if score > MM:
		MM = score 

print(f"The highest score is {MM}")