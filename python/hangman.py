import random

def hangman():
    words = ['python', 'hangman', 'programming', 'developer', 'challenge']
    secret_word = random.choice(words)
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        # Display the current state of the word
        current_state = ''.join(letter if letter in guessed_letters else '_' for letter in secret_word)
        print(f"Word: {current_state}")
        print(f"Attempts left: {attempts}")

        # Get player's guess
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            if all(letter in guessed_letters for letter in secret_word):
                print(f"Congratulations! You've guessed the word: {secret_word}")
                return
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word.")

    print(f"You've run out of attempts! The word was: {secret_word}")

if __name__ == "__main__":
    hangman()
