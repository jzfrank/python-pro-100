
student_heights = input("Input a list of student heights (in cm) seperated by space:\n")
student_heights = student_heights.split()
for i in range(len(student_heights)):
	student_heights[i] = int(student_heights[i])
print(student_heights)

ss = 0 
l = 0 
for height in student_heights:
	l += 1
	ss += height

average_height = round(ss / l)
print(f"The average height of student is {average_height} cm")