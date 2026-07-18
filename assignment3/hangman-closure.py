#Task4

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        displayed = ""
        for ch in secret_word:
            if ch in guesses:
                displayed += ch
            else:
                displayed += "_"

        print(displayed)

    
        return all(ch in guesses for ch in secret_word)

    return hangman_closure


if __name__ == "__main__":
    secret = input("Enter the secret word: ").strip().lower()
    hangman = make_hangman(secret)

    print("\nLet's play Hangman!")
    print("Guess one letter at a time.\n")

    while True:
        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        done = hangman(guess)

        if done:
            print("\nYou guessed the word!")
            break
