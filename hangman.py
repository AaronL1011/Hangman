# Requirements

"""
word to guess
array for disguised word
Current errors:
Guesses left: 10

"""
import random
import draw
listFile = open("guessingWords.txt", "r")
wordGuessList = listFile.read().splitlines()

def gameMain():
    #initialize the randomly selected word to guess
    wordToGuessSTRING = wordGuessList[random.randint(0, len(wordGuessList))]
    wordToGuess = list(wordToGuessSTRING)
    wordToGuess2 = list(wordToGuessSTRING)
    print("A word has been chosen...\n")
    #initialize variables requireda
    errorCount = 0
    missedLetters = []
    correctLetters = ["_"] * (len(wordToGuess))
    #main game start
    print(correctLetters)
    while correctLetters != wordToGuess: #10 is maximum number of errors until hangman is drawn completely
        guess = input("Enter a guess!: ")
        # guess = guess.lower
        if guess in wordToGuess and guess not in correctLetters:
            for c in wordToGuess:
                if c == guess:
                    correctLetters[wordToGuess2.index(guess)] = guess
                    wordToGuess2[wordToGuess2.index(guess)] = "0"
        elif guess in correctLetters:
            print("You already guessed that!")
        else:
            errorCount += 1
            missedLetters.append(guess)
        
        if errorCount == 10 or correctLetters == wordToGuess:
            break
        drawScreen(errorCount, missedLetters, correctLetters)
    
    if errorCount != 10:
        print("\n"*30)
        print(wordToGuess)
        print("CONGRATS! YOU WON!")
    else:
        print("\n"*30)
        draw.drawEnd()
        print(wordToGuess)
        print("Damn, you lost! Better luck next time.")
        
def drawScreen(errorCount, missedLetters, correctLetters):
    print("\n"*30)
    if errorCount == 0:
        draw.drawNone()
    elif errorCount == 1:
        draw.drawStart()
    elif errorCount == 2:
        draw.drawTwo()
    elif errorCount == 3:
        draw.drawThree()
    elif errorCount == 4:
        draw.drawFour()
    elif errorCount == 5:
        draw.drawFive()
    elif errorCount == 6:
        draw.drawSix()
    elif errorCount == 7:
        draw.drawSeven()
    elif errorCount == 8:
        draw.drawEight()
    elif errorCount == 9:
        draw.drawNine()
    print("\n")
    print("________________________________________")
    print("Current Word:")
    print(correctLetters)
    print("\n")
    print("Missed Letters:")
    print(missedLetters)


print("Welcome to Hangman!")
gameMain()
    
