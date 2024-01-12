import random
def game():
    guess = int(input("Guess a number(1-100): "))
    num = random.randint(1, 100)
    while guess != num:
        if guess > num:
            print("Wrong number. Too high")
            guess = int(input("Guess a number: "))

        elif guess < num:
            print("Wrong number. Too low")
            guess = int(input("Guess a number: "))

        
    print("You gussed correctly!! Good Job!")
    restart = input("Want to play again? Yes or No: ")
    while restart == "Yes":
        game()


game()



