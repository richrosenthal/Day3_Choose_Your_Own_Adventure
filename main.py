#Day 3 Making a choose your own Adventur game 
#Author Richard Rosenthal 
#Date 5-11-21

import time 

print("Welcome to escape Ikea!")
user_name = input("What is your name?")

print(f"Hello {user_name}")

print("\nYou awake on a couch in a darken building")
print("\nAs you come to your senses you realize you fell asleep in an IKEA show room")
time.sleep(2)
print("\nYou start to panic, however, you see what looks like an exit sign to your right and a long dark hallway to your left")
time.sleep(2)
print("\nTo make matters worse you hear footsteps behind you.")

answer_one = input("Do you go 'left' or 'right'?")

if answer_one == 'left':
  answer_two = input("\nGood choice, your bravery shall be rewarded. You reach another corner a closet to the right or another long hallway to the left? 'left' or 'right'?")

  if answer_two == 'right':
    answer_three = input("\nPhew the closet was just an allusion. It lead to a hidden staircase. But the footsteps are getting closer. You can either run to the bottom of the stairs to the left or you can jump out the window to the right. Do you go 'left' or 'right?'")

    if answer_three == 'right':
      print(f"\nThat was the correct choice {user_name}! You thankfully landed on top of a dumpster and made it out the building. Just drive away and never look back.")
else:
      print(f"\nYou died {user_name}")
