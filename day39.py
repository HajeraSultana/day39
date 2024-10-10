import random, os, time
listOfWords = ["black", "grey", "red", "blue", "orange","white", "brown", "pink", "yellow","green"]

myWord = random.choice(listOfWords)

lives = 6

letterPicked = []

while True:
    time.sleep(1)
    os.system("clear")
    print("🌟Hangman🌟")
    print()
    userInput = input("Choose a letter: ").lower()

    if userInput in letterPicked:
        print("You've tried that before!")
        continue

    letterPicked.append(userInput)

    if userInput in myWord:
        print("Correct")
    else:
        print("Nope, not in there.")
        lives -= 1

    allLetters = True
    print()
    for i in myWord:
        if i in letterPicked:
            print(i, end="")
        else:
            print("_", end="")
            allLetters = False
    print()

    if allLetters:
        print()
        print(f"You won with {lives} left!")
        break


    if lives <= 0:
        print(f"You lost! and the word is {myWord}")
        break 
    else:
        print()
        print(f"You left with {lives}")
