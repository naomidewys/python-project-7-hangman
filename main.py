import random
import hangman_words
import hangman_art

# Create word list and lives total
word_list = hangman_words.word_list
lives = 6

# Print logo and randomly select word
print(hangman_art.logo)
chosen_word = random.choice(word_list)

# Shows length of word to guess and chosen word updates with correct guesses
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

#Establishes current game setting and list of letters
game_over = False
correct_letters = []

while not game_over:

    # Establishes lives left and converts guesses into lowercase
    print(f"****************************{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display = ""

    # Shows if letter already guessed. No lives lost.
    if guess in correct_letters:
        print(f"You have already guessed '{guess}'. Try another letter.")

    # If letter is correct, it is added to letters list and displayed in the guessed word. If incorrect, underscore remains.
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # If guess not in chosen word, lives reduce.
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess},' which is not in the word. You lose a life.")

        # When lives reach nil, game over. Correct word is revealed.
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word.upper()}. GAME OVER**********************")

    # If all letters correctly guessed, user wins.
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Shows hangman art depending on how many lives are left.
    print(hangman_art.stages[lives])
