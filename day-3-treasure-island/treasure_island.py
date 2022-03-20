print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island. Your mission is to find the treasure.")

direction = input("You just landed. There are two roads. "
	+ "Which direction will you go? (left/right):\n")
direction = direction.lower()
if direction == "right":
	print("Game Over. There is a giant tiger in the right road!")
else:
	action = input("You chose the left road. A guard showed up and started to chase after you. "
		+ "You run fast but meet a river. \nThe guard is coming closer, you can swim "
		+ "and get rid of him. But you can also wait and battle with the guard. "
		+ "(swim/wait):\n")
	action.lower()
	if action == "swim":
		print("Game Over. The river turns out to be poisonous!")
	else:
		door = input("You wait and have a good fight with the guard. He lost and offered "
			+ "to take you to the treasure. He led you to a cave. There are three doors. "
			+ "He told you the treasure is behind one of the door. But he forgot which one. "
			+ "Which door do you choose? (blue/red/yellow):\n")
		door = door.lower()
		if door == "red":
			print("Game Over. Fire bursts behind red door.")
		elif door == "blue":
			print("Game Over. Flood is behind blue door.")
		elif door == "yellow":
			print("You Win!")
			print('''
				                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           |'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'.U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-.U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
				''')
