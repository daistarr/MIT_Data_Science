
import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()


def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"  
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True

   
def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letter = ""
    for i in secret_word:
        if i not in letters_guessed:
            letter += '*'
        else:
            letter += i
    return letter



def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letter = (string.ascii_lowercase)    
    for i in letter[:]:
        if i in letters_guessed:
            letter = letter.replace(i, '')
    return letter


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '$'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol $, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    print('Welcome to Hangman!')
    word = len(secret_word)
    print(f"I am thinking of a word that is {word} letters long.")
    print('--------------')
    
    letter_guessed = ''
    guesses_remaining = 10
    

    while with_help == False:
        if guesses_remaining == 1:
            print ("You have " + str(guesses_remaining) + " guess left.")
        else:          
            print ("You have " + str(guesses_remaining) + " guesses left.")  
        print ("Available letters: " + get_available_letters(letter_guessed))
        letter = str.lower(input("Please guess a letter: "))
        if letter == '$' and guesses_remaining > 3:
            with_help == True
        elif letter == '$' and guesses_remaining <= 3:
            with_help == True
            print('Oops! Not enough guesses left: ' + get_word_progress(secret_word, letter_guessed))
            break
        elif letter in secret_word and letter not in letter_guessed:
            letter_guessed += letter
            print ("Good guess: " + get_word_progress(secret_word, letter_guessed))
        elif letter in letter_guessed:
            print ("Oops! You've already guessed that letter: " + get_word_progress(secret_word, letter_guessed))
        elif letter.isalpha() == False and letter != '$':
            print("Oops! That is not a valid letter. Please input a letter from the alphabet: " + get_word_progress(secret_word, letter_guessed))
        elif letter != '$':
            letter_guessed += letter
            if letter in ('a', 'e', 'i', 'o', 'u'):
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
            print ("Oops! That letter is not in my word: " + get_word_progress(secret_word, letter_guessed))
        print ("------------")
        if guesses_remaining <= 0:
            print ("Sorry, you ran out of guesses. The word was " + secret_word + ".")
            break
        if get_word_progress(secret_word, letter_guessed) == secret_word:
            total_score = (guesses_remaining + 2 * len(set(secret_word)) + (3 * len(secret_word)))
            print ("Congratulations, you won!")
            print(f'Your total score for this game is: {total_score}')
            break
    
    while with_help == True:
        if guesses_remaining == 1:
            print ("You have " + str(guesses_remaining) + " guess left.")
        else:          
            print ("You have " + str(guesses_remaining) + " guesses left.")
        print ("Available letters: " + get_available_letters(letter_guessed))
        letter = str.lower(input("Please guess a letter: "))
        if '$' not in letter:
            if letter in secret_word and letter not in letter_guessed:
                letter_guessed += letter
                print ("Good guess: " + get_word_progress(secret_word, letter_guessed))
            elif letter in letter_guessed:
                print ("Oops! You've already guessed that letter: " + get_word_progress(secret_word, letter_guessed))
            elif letter.isalpha() == False and letter != '$':
                print("Oops! That is not a valid letter. Please input a letter from the alphabet: " + get_word_progress(secret_word, letter_guessed))
            elif letter != '$':
                letter_guessed += letter
                if letter in ('a', 'e', 'i', 'o', 'u'):
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
                print ("Oops! That letter is not in my word: " + get_word_progress(secret_word, letter_guessed))
            print ("------------")
            with_help == False
        elif letter == '$' and guesses_remaining > 3:
            help_letter = random.choice(secret_word)
            while help_letter in (get_word_progress(secret_word, letter_guessed)):
                help_letter = random.choice(secret_word)
            else:
                letter_guessed += help_letter
            print('Letter revealed: ' + help_letter)
            print(get_word_progress(secret_word, letter_guessed))
            guesses_remaining -= 3
            print ("------------")
            with_help == False
            if get_word_progress(secret_word, letter_guessed) == secret_word:
                total_score = (guesses_remaining + 2 * len(set(secret_word)) + (3 * len(secret_word)))
                print ("Congratulations, you won!")
                print(f'Your total score for this game is: {total_score}')
                break
        elif letter == '$' and guesses_remaining <= 3:
            print('Oops! Not enough guesses left: ' + get_word_progress(secret_word, letter_guessed))
            break
    
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

     secret_word = choose_word(wordlist)
     with_help = False
     hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "$" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run test_ps2_student.py
    # one more time before submitting to make sure all the tests pass.
    #pass
