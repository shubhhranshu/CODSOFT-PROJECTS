import random

print("Let's play Rock-Paper-Scissors!")
print("Type exactly: rock, paper or scissors.")

while True:
    user = input("Choose rock, paper, or scissors: ")
    if user not in ["rock", "paper", "scissors"]:
        print("Please enter a valid choice (all lowercase).")
        continue

    computer = random.choice(["rock", "paper", "scissors"])
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win!")
    else:
        print("You lose!")

    again = input("Play again? (yes/no): ")
    if again != "yes":
        print("Thanks for playing!")
        break
