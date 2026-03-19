import random

# List of words
words = ["python", "computer", "science", "program", "hangman"]

# Randomly select a word
word = random.choice(words)

# Create empty list for guessed letters
guessed = ["_"] * len(word)

attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

# Check result
if "_" not in guessed:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
