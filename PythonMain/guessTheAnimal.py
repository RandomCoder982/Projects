import random

words = '''ant babboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle 
ferret fox frog goat goose hawk lion lizard llama mole rat raven rhino shark sheep spider toad turkey turtle 
wolf wombat zebra'''

randomWord = random.choice(words.split())
name = input("What is your name? ")
print("Good luck guessing the animal", name)
userInput = ""

correctLetters = []
underScores = []
guessedLetters = ""
    

for i in range(len(randomWord)):
    correctLetters.append(randomWord[i])
        
for i in range(len(randomWord)):
    underScores.append("_")    


while userInput != randomWord:
    

    userGuess = input("Guess a letter: ")
    guessedLetters += userGuess
    
    for i in range(len(correctLetters)):
        if userGuess == correctLetters[i]:
            underScores[i] = userGuess

    print("\n" +  str(underScores))
    print(f"\nGuessed letters: {guessedLetters}")

    if underScores == correctLetters:
        print(f"You've guessed the animal, it was a {randomWord} good job!")
        userInput = randomWord
    
