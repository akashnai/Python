import random
import os

# [] - list - slow - mutables
# () - tuples - faster - nonmutables

# word[0]
# word(0) ???????

def hangman():
    word = random.choice(["pugger", "littlepugger","tiger", "akki", "lion", "GOT", "avengers", "power", "lord", "dragon"])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessMade = ""

    while len(word) > 0:
        main = ""

        for letter in word:
            if letter in guessMade:
                main += letter

            else:
                main += ' _ '

        if main == word:
            print(f"The word was {main}")
            print("Congratulations! You win!")
            break

        print("Guess the word: ", main)
        guess = input()


        if guess in validLetters:
            guessMade += guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns -= 1
            if turns == 9:
                os.system('cls')
                print("9 Turns left")
                print("------------")
            if turns == 8:
                os.system('cls')
                print("9 Turns left")
                print("------------")
                print("      O     ")
            if turns == 7:
                os.system('cls')
                print("7 Turns left")
                print("------------")
                print("      O     ")
                print("      |     ")
            if turns == 6:
                os.system('cls')
                print("6 Turns left")
                print("------------")
                print("      O     ")
                print("      |     ")
                print("     /      ")
            if turns == 5:
                os.system('cls')
                print("5 Turns left")
                print("------------")
                print("      O     ")
                print("      |     ")
                print("     / \    ")
            if turns == 4:
                os.system('cls')
                print("4 Turns left")
                print("------------")
                print("      O /   ")
                print("      |     ")
                print("     / \    ")
            if turns == 3:
                os.system('cls')
                print("3 Turns left")
                print("------------")
                print("    \ O /   ")
                print("      |     ")
                print("     / \    ")
            if turns == 2:
                os.system('cls')
                print("2 Turns left")
                print("------------")
                print("    \ O |/  ")
                print("      |     ")
                print("     / \    ")
            if turns == 1:
                os.system('cls')
                print("Last breath counting, Take care!")
                print("------------")
                print("    \ O_|/  ")
                print("      |     ")
                print("     / \    ")
            if turns == 1:
                os.system('cls')
                print("You lose, You let the kind man die!")
                print("------------")
                print("      O_|   ")
                print("     /|\    ")
                print("     / \    ")
                break

name = input("Enter your name: ")
print(f"Welcome ${name}")
print("---------------------")
print("Try to guess the word in less than 10 attempts :)")
hangman()