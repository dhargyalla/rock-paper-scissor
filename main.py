rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choose = int(input("what do you choose, 0 for rock, 1 for paper, 2 for scissors\n"))

image = [rock, paper, scissors]

if choose >= 3 or choose < 0 :
  print("you typed an invalid number, you lose")
else:
  print(image[choose])
  computer_choose = random.randint(0,2)
  print("Computer choose: \n")
  print(image[computer_choose])
  
  if choose == computer_choose:
    print("it's a draw")
  elif choose > computer_choose or (choose == 0 and computer_choose == 2):
    print("you win")
  elif choose < computer_choose or (choose == 2 and computer_choose == 0):
    print("you lose")

  
   
  

