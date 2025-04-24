import random
from english_words import get_english_words_set
web2lowerset = get_english_words_set(['web2'], lower=True)




word_list = list(web2lowerset)
rand_word = random.choice(word_list)
letters_guessed = []
word_map = ['_' for char in range(len(rand_word))]




def main()-> None:
    lives = 6
    game_over = False
    print(rand_word)


    while not game_over:
        user_guess = get_guess()
        word_map = check_word(rand_word=rand_word, guess=user_guess)
        word = to_string(word_map)


        if user_guess not in rand_word:
            print("That letter ain't there")
            lives -= 1
        else:
            print("Lucky guess")


        if lives < 0:
            print("...And they are dead. Great job.")
            game_over = True


        if word == rand_word:
            print("Chat clip this. Now I won't be hanged at the gallows :)")
            game_over = True


def get_guess()->str:
    """Gets the users guess on the word"""
    user_guess = str(input("\nGuess a letter: ")).lower()
    if len(user_guess) != 1:
        print("That ain't one letter\nTry again!")
        get_guess()


    if check_guessed(guess = user_guess):
        letters_guessed.append(user_guess)
    else:
        print("You already tried that one\nTry again!")
        get_guess()
    return user_guess


def check_guessed(guess: str)->bool:
    """Checks if user has already guessed a letter"""
    if guess in letters_guessed:
        return False
    return True


def check_word(rand_word: str, guess: str)->list[str]:
    """Checks each index of word with user guess
        returns the apearence at each index"""
    index = 0
    for char in rand_word:
        if guess == char:
            word_map[index] = guess
        index += 1
    return word_map


def to_string(char_list: list[str])->None:
    """Turns a list[str] into one readable string"""
    final = ""
    for char in char_list:
        final += char
    print(final)
main()