
import random
item_list = ["rock", "paper", "scissors"]
wins = 0
loses = 0
while True:
    print("Welcome to Rock, Paper, Scissors Game! 🎯")
    user_choice = input("Enter your move (rock, paper, scissors): ").lower().strip()

    if user_choice not in item_list:
        print("Invalid choice 😤. Please choose rock, paper, or scissors.😌")
        continue

    computer_choice = random.choice(item_list)
    print(f"👤 User choice: {user_choice}")
    print(f"💻 Computer choice:{computer_choice}")
    
    if user_choice == computer_choice:
        print("Same Choice. Match Tie 😢")
    elif user_choice == "rock" and computer_choice == "paper":
        print("Paper covers rock. You Lost ❌ ")
        loses += 1
    elif user_choice == "rock" and computer_choice == "scissors":
        print("Rock crushes scissors. You Won 🏆")
        wins += 1
    elif user_choice == "paper" and computer_choice ==  "rock":
        print("Paper covers rock. You Won 🏆")
        wins += 1
    elif user_choice == "paper" and computer_choice == "scissors":
        print("Scissors cut paper. You Lost ❌")
        loses += 1
    elif user_choice == "scissors" and computer_choice == "rock":
        print("Rock crushes scissors. You Lost ❌")
        loses += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("Scissors cut paper. You Won 🏆")
        wins += 1
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 😊")
        if wins > loses:
            print("You are the winner! 🥇😍")
        else:
            print("Computer is the winner! 🥇💔")
        print(f"Your Score: {wins}")
        print(f"Computer Score: {loses}")
        break

