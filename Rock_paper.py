import random

options= ["rock","paper","scissors"]

is_running = True

while is_running:
    player = None
    computer = random.choice(options)

    
    
while player not in options:
    player = input("Enter a choice (rock , paper ,scissor): ")

print(f"Player: {player}")
print(f"Computer : {computer}")

if player == computer:
    print("It is tie! ")
elif player == "rock" and computer == "scissors":
    print("You won! ")
elif player == "paper" and computer == "rock":
    print("You won! ")
elif player == "scissors" and computer == "paper":
    print("You win! ")
else:
    print("You lose! ")



