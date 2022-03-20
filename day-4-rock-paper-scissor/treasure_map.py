row1 = ["#", "#", "#"]
row2 = ["#", "#", "#"]
row3 = ["#", "#", "#"]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? (e.g. 12): \n")

#---------------
treasure_map = [row1, row2, row3]
x = int(position[0]) - 1
y = int(position[1]) - 1
treasure_map[x][y] = "x"

print(f"{treasure_map[0]}\n{treasure_map[1]}\n{treasure_map[2]}")