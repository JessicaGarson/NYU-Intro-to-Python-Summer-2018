class Hangman():
    def __init__(self, word, guesses=0, guessed_letters=[]):
        self.word = word
        self.guesses = guesses
        self.guessed_letters = guessed_letters
        self.word = word

    def guesses_less_than_5(self, word, guesses, guessed_letters):
        while guesses < 5:
            guess = input("Hi. Please guess a letter.")

            if set(word).intersection(set(guessed_letters)) == set(word):
                break

            if guess in word and guess not in guessed_letters:
                print("Correct!")
                guessed_letters.append(guess)
                print("So far you've used ", guessed_letters, "as letters.")
                print("You've got", 5-guesses, "guesses left.")

            elif guess not in word and guess not in guessed_letters:
                guesses += 1
                print("Wrong!")
                guessed_letters.append(guess)
                print("So far you've used ", guessed_letters, "as letters.")
                print("You've got", 5-guesses, "guesses left.")

            elif guess in guessed_letters:
                print("You've already guessed that letter, please guess again.")

            else:
                print("ERROR")

    def set_intersection(self, word, guesses, guessed_letters):
        if set(word).intersection(set(guessed_letters)) == set(word):
            print("You won!")
        else:
            print("You lost!")


def main():
    dorrito = Hangman('dorito')
    dorrito.guesses_less_than_5(word=dorrito.word, guesses=dorrito.guesses, guessed_letters=dorrito.guessed_letters)
    dorrito.set_intersection(word=dorrito.word, guesses=dorrito.guesses, guessed_letters=dorrito.guessed_letters)


if __name__ == "__main__":
    main()
