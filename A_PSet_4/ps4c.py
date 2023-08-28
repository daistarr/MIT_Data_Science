import json
import ps4b # Importing your work from Part B

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # inFile: file
    with open(file_name, 'r') as inFile:
        # wordlist: list of strings
        wordlist = []
        for line in inFile:
            wordlist.extend([word.lower() for word in line.split(' ')])
        return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"").lower()
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story[:-1]

def get_story_pads():
    with open('pads.txt') as json_file:
        return json.load(json_file)

WORDLIST_FILENAME = 'words.txt'
### END HELPER CODE ###

def decrypt_message_try_pads(ciphertext, pads):
    '''
    Given a string ciphertext and a list of possible pads
    used to create it find the pad used to create the ciphertext

    We will consider the pad used to create it the pad which
    when used to decrypt ciphertext results in a plaintext
    with the most valid English words. In the event of ties return
    the last pad that results in the maximum number of valid English words.

    ciphertext (EncryptedMessage): The ciphertext
    pads (list of lists of ints): A list of pads which might have been used
        to encrypt the ciphertext

    Returns: (PlaintextMessage) A message with the decrypted ciphertext and the best pad
    '''
    word_list = load_words(WORDLIST_FILENAME) # loads list of words
    best_pad = None # starts best pad variable 
    max_word_count = -1 # starts couting variable of words
    for pad in pads: # loop through pads
        plaintext = ciphertext.decrypt_message(pad).get_text() # decryphers the 'ciphertext' in the pad  running at that moment
        word_count = sum(is_word(word_list, word) for word in plaintext.split()) # counts # of words in 'plaintext'
        if word_count >= max_word_count: # checks if the pad running has more words than the pad before
            max_word_count = word_count  # new count of words
            best_pad = pad # updates 'bed_pad' variable
    return ciphertext.decrypt_message(best_pad) # returns plaintext msg decryphered according to the obtained best pad

    
def decode_story():
    '''
    Write your code here to decode Bob's story using a list of possible pads
    Hint: use the helper functions get_story_string and get_story_pads and your EncryptedMessage class.

    Returns: (string) the decoded story

    '''
    output = '' #starts variable
    encrypted_message = ps4b.EncryptedMessage(get_story_string()) # imports EncryptedMessage from ps4b; creates an objt from ciphertext
    pads = get_story_pads() # potential pads
    plaintext_message = decrypt_message_try_pads(encrypted_message, pads) # decrypher 'ciphertext' according to the best bad available
    output = plaintext_message.get_text() # stores decrypted plaintext
    return output # returns the decryphered Bob's story


if __name__ == '__main__':
    # # Uncomment these lines to try running decode_story()
    story = decode_story()
    print("Decoded story: ", story)
    

