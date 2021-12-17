import random
import time

# Defining functions using the def statement
def displayIntro():
  # Using triple quotes here allows to multiline strings.. easier to read.
  print('''You are in a land full of dragons. In front of you, 
  you see two caves. In one cave, the dragon is friendly
  and will share his treasure with you. The other dragon is 
  greedy and hungry, and will eat you on sight''')
  print()

# while loop will run as long as a condition is true
def chooseCave():
  # cave is a locally scoped variable
  cave = ''
  while cave != '1' and cave != '2':
    print('Which cave will you go into?(1 or 2)')
    # assigning the users input to the cave variable
    cave = input()

    return cave

def checkCave(chosenCave):
  #chosenCave is the parameter here in the definition. During the execution of the function the chosenCave from the chooseCave() function is being passed here.
  print('You approach the cave....')
  time.sleep(2)
  print('It is dark and spooky.....')
  time.sleep(2)
  print('A large dragon jumps out in front of you! He opens his jaws and...')
  print()
  time.sleep(2)

  friendlyCave = random.randint(1,2)

  if chosenCave == str(friendlyCave):
    print('Gives you his treasure!')
  else:
      print('Gobbles you down in one bite!')

# This is the games whole flow
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
  displayIntro()
  caveNumber= chooseCave()
  #caveNumber from above is passed to checkCave as an argument
  checkCave(caveNumber)
  print('Do you want to play again? (Yes or no)')
  playAgain = input()