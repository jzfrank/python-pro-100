import random 

rock = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
'''

paper = '''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'    
'''


scissor = '''

    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.

'''

choices = [rock, paper, scissor]

print("Welcome to rock paper scissor game! Your oppenent is computer. ")
user = input("What do you want to give? (0: rock, 1: paper, 2: scissor)\n")
user = int(user)
computer = random.randint(0, 2)

print("Your give: ")
print(choices[user])
print("Computer give: ")
print(choices[computer])

if user == computer:
  print("It's a tie!")
elif (user == 0) and (computer == 2): # rock vs scissor
  print("You Win!")
elif (user == 1) and (computer == 0): # paper vs rock 
  print("You Win!")
elif (user == 2) and (computer == 1): # scissor vs paper 
  print("You Win!")
else:
  print("Computer win!")

