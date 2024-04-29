import random

words = ["apple", "tea", "omega"]
random_word = random.choice(words)
display_word = []
for letters in words:
    display_word += "_"
print(display_word)

lives = 6
while lives:
    guess = input("Guess a letter: ")
    if guess in random_word:
        for i in range(len(random_word)):
            if random_word[i] == guess:
                display_word[i] = guess
        print(' '.join(display_word))
        if "_" not in display_word:
            print("Congratulations! You've guessed the word correctly!")
            break
    else:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")
        if lives == 0:
            print("You've run out of lives! Game Over.")
            print(f"The word was: {random_word}")
            break
