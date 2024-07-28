import random

rock = '🪨 🪨 🪨'

paper = '📃 📃 📃'

scissors = '✂️ ✂️ ✂️'

#Write your code below this line 👇
game_images=[rock , paper , scissors]

user_move=int(input("choose '0' for rock , '1' for paper , '2' for scissor.\n"))
print("User have choosen ",game_images[user_move])

computer_move=random.randint(0,2)
print("computer have choosen ",computer_move)
print([game_images[computer_move]])
if user_move >=3 or user_move < 0 :
  print("You have entered an invalid number , You lost !.")
elif computer_move==user_move:
  print("It's a tie between both of you.")
elif computer_move > user_move:
  print("you lost !")
elif user_move > computer_move:
  print("You won !")
