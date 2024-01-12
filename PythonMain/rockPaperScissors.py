import random 

choices = "Rock Paper Scissors"
start = input("Do you want to play the game (Yes or No)? ")

while start != "No":
    choice = input("Rock Paper or Scissors \n")
    gameChoice = random.choice(choices.split())

    if choice == gameChoice:
        print("It's a draw")
    elif choice == "Rock" and gameChoice == "Paper":
        print(gameChoice)
        print("You lose, paper beats rock. ")
    elif choice == "Rock" and gameChoice == "Scissors":
        print(gameChoice)
        print("You Win, rock beats Scissors. ")
    elif choice == "Paper" and gameChoice == "Rock":
        print(gameChoice)
        print("You Win, paper beats rock. ")
    elif choice == "Paper" and gameChoice == "Scissors":
        print(gameChoice)
        print("You lose, scissors beats paper. ")
    elif choice == "Scissors" and gameChoice == "Rock":
        print(gameChoice)
        print("You win, scissors beats paper")
    elif choice == "Scissors" and gameChoice == "Paper":
        print(gameChoice)
        print("You win, scissors beats paper")
    
    start = input("Do you want to play the game again?(Yes or No) ")



