#code alpha task 1
import random

words = ["python", "jupiter", "coding", "galaxy", "starlight"]
secret_word = random.choice(words)
guessed_letters = []
attempts = 6

print("--- Welcome to Hangman! ---")

while attempts > 0:
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print(f"\nWord: {display_word}")
    print(f"Attempts left: {attempts}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")

    if "_" not in display_word:
        print("Congratulations! You won! 🎉")
        break
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
    
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try again.")
        continue

    guessed_letters.append(guess)
    if guess in secret_word:
        print(f"Good job! '{guess}' is in the word.")
    else:
        attempts -= 1
        print(f"Sorry, '{guess}' is not there.")
if attempts == 0:
    print(f"\nGame Over! The word was: {secret_word}")