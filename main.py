import random


options = ("rock", "paper","scissors")
player2= None
computer = random.choice(options)

while player2 not in options:
   
    player2=input("Enter a choice (rock, paper, scissors): ")

print(f"(Player2) : {player2}")
print(f"(Computer) : {computer}")