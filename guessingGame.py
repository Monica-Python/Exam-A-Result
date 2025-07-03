"""
PGR107 Python Programming Exam 2025
Authors: Candidate 63 and 13
Sources: https://emojipedia.org/ 

Question 1 - Word Guessing Game

Reads words from files/words.txt and lets the player guess letters until the
word is revealed or the max wrong guesses (word length) is reached.
Supports replay on win/lose.
    
Emojis and separators were included to make the output more visual and improve 
readability.

"""

import random

filepath = "files/words.txt"  # Imports the text file

def gameFunctions(): #Functions used in the game
    with open(filepath, "r") as textFile: #Reads the textfile to use
        words = [line.strip() for line in textFile if line.strip()] #using strip to avoid any space or empty lines
        secret_word = random.choice(words)
        

    incorrect = set()  # Incorrect letters
    correct = set()    # Correct letters
    max_attempts = len(secret_word)  # Max wrong guesses
    attempts = 0       # Track wrong guesses

    print(f"The word you need to guess has '{len(secret_word)}' letters.")
    
    # Game loop that continues until you win or run out of guesses
    while attempts < max_attempts:
        display_word = ''.join([letter if letter in correct else '_' for letter in secret_word])
        print(f"Correct guessed letters: {display_word}")
        print(f"You have '{max_attempts - attempts}' attempts left\n")
        
        
        # Ask for a guess
        guess = input("Give me a letter: ").lower().strip()

        # Validate the player input to make sure its a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in correct or guess in incorrect: #Prevents duplicate guesses
            print("Silly you! You have already guessed this letter! 🤭\n")
            continue

        if guess in secret_word: #Checks if the letter is in the word and prints a message if it is
            print(f"Good job! '{guess}' is in the word! 🎉\n")
            correct.add(guess)
        else: #Or prints another message is it isn't
            print(f"Oops! '{guess}' is not in my secret word 😔\n")
            incorrect.add(guess)
            attempts += 1

        # Checks if the player has guessed the word
        if all(letter in correct for letter in secret_word):
            print(f"\nCongratulations! You guessed the word: {secret_word} 🏆💪🎉")
            again()
            return
      
        if attempts == max_attempts: #Checks if there is still any attempts left
            print(f"\nGame over! You've run out of attempts. The word was: {secret_word}")
            again()
            return
        
        
        
def again(): #Function to restart the game
    again_input = input("\nWould you like to go again? 🎉 (yes/no)").lower()
    
    if again_input == "yes":
        print("Good, you got this!💯\n")
        main()        
    elif again_input == "no" :
        print("Okay, goodbye😔")
    else :
        print("Invalid choice, please try again!")
        again()


def main(): #Function for main
    print("Welcome to the guessing game! 🎉")
    startGame = input("I have a secret word, can you guess it? 🔍 (yes/no): ").lower().strip() #Using lower and strip to prevent spaces and match the word
    print("-----------------------------------------\n")

    if startGame == "yes": #Check if the user wants to play
        print("Let's go! 🔥") #Starts the game
        print("Write a letter to start guessing!💯\n")
        gameFunctions()
    elif startGame == "no": #Ends the game
        print("Bummer, I was cheering for you 😔")
    else:
        print("Invalid choice, please try again!")
        main() #restarts the menu


main()


           