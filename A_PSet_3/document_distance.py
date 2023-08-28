
"""
Description:
    Computes the similarity between two texts using two different metrics:
    (1) shared words, and (2) term frequency-inverse document
    frequency (TF-IDF).
"""

import string
import math
import re

### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def prep_data(input_text):
    """
    Args:
        input_text: string representation of text from file,
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    
    list_return = input_text.split()
    
    return list_return


### Problem 1: Get Frequency ###
def get_frequencies(word_list):
    """
    Args:
        word_list: list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a word in l and the corresponding int
        is the frequency of the word in l
    """
    
    all_freq = {}
 
    for i in word_list: # count how many times a word occurs
        if i in all_freq:
            all_freq[i] += 1
        else:
                all_freq[i] = 1 
                
    return all_freq


### Problem 2: Get Words Sorted by Frequency
def get_words_sorted_by_frequency(frequencies_dict):
    """
    Args:
        frequencies_dict: dictionary that maps a word to its frequency
    Returns:
        list of words sorted by increasing frequency with ties broken
        by alphabetical order
    """
    
    new_list = sorted(frequencies_dict, key=lambda x: (frequencies_dict.get(x), x)) # sorted function for the counting
    
    return new_list
                    
        

### Problem 3: Most Frequent Word(s) ###
def get_most_frequent_words(dict1, dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        dict1: frequency dictionary for one text
        dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          frequencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """

    
    combined_dict = {}  # Combine the two dictionaries
    for word in dict1:
        if word in dict2:
            combined_dict[word] = dict1[word] + dict2[word]
        else:
            combined_dict[word] = dict1[word]
    for word in dict2:
        if word not in combined_dict:
            combined_dict[word] = dict2[word]

    max_freq = max(combined_dict.values())  # Find the highest frequency

    most_frequent_words = []    # Get all the words with the highest frequency
    for word in combined_dict:
        if combined_dict[word] == max_freq:
            most_frequent_words.append(word)

    return sorted(most_frequent_words)  # Sort alphabetically and return
    

### Problem 4: Similarity ###
def calculate_similarity_score(dict1, dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        dict1: frequency dictionary of words of text1
        dict2: frequency dictionary of words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    unique_words = set(dict1.keys()) | set(dict2.keys()) # union of keys in both dictionaries    
    diff = sum(abs(dict1.get(word, 0) - dict2.get(word, 0)) for word in unique_words) # difference in words/text frequencies
    all_freq = sum(dict1.values()) + sum(dict2.values()) #The total frequencies of dict1 and dic22
    similarity_score = round(1 - diff / all_freq, 2)

    return similarity_score

### Problem 5: Finding TF-IDF ###
def get_tf(text_file):
    """
    Args:
        text_file: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    
    a = load_file(text_file) # return string, contains file contents
    b = prep_data(a) #list representation of input_text, where each word is a different
    c = get_frequencies(b) #dictionary that maps string
    
    tf ={}
    total = len(b) #total number of words in the document
    
    for word, count in c.items():
        tf[word] = count/float(total)
    
    return tf

    

def get_idf(text_files):
    """
    Args:
        text_files: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
       
    word_counts = {}
    
    #load the file
    num_docs = len(text_files)
    for filename in text_files:
        with open(filename) as f:
            text = f.read().lower()
            
            #prep the data, remove punctuation
            text = text.translate(str.maketrans('', '', string.punctuation))
            words = set(text.split())
            for word in words:
                if word not in word_counts:
                    word_counts[word] = 1
                else:
                    word_counts[word] += 1

    
    #get idf for each word
    idf = {}    
    for word in word_counts:
        idf[word] = math.log10(num_docs / word_counts[word])

    return idf


def get_tfidf(text_file, text_files):
    """
    Args:
        text_file: name of file in the form of a string (used to calculate TF)
        text_files: list of names of files, where each file name is a string
        (used to calculate IDF)
    Returns:
       a sorted list of tuples (in increasing TF-IDF score), where each tuple is
       of the form (word, TF-IDF). In case of words with the same TF-IDF, the
       words should be sorted in increasing alphabetical order.

    * TF-IDF(i) = TF(i) * IDF(i)
    """
    
    #calculate TF of each word in text_file
    tf = {}
    
    with open(text_file, 'r') as file:  #open file
        text = file.read().lower().translate(str.maketrans('', '', string.punctuation)) #remove punctuation
        words = text.split() 
        for word in words:
            if word in tf:
                tf[word] += 1
            else:
                tf[word] = 1
                
        # frequency = / each word count by the total number of words
        total_words = len(words)
        for word in tf:
            tf[word] = tf[word] / total_words

    #calculate idf of each word in the given list of text_files
    df = {}
    for file in text_files:
        with open(file, 'r') as f: #open file
            text = f.read().lower().translate(str.maketrans('', '', string.punctuation)) #remove punctuation
            words = set(text.split())
            for word in words:
                if word in df:
                    df[word] += 1
                else:
                    df[word] = 1

    idf = {}
    total_files = len(text_files)
    for word in df:
        idf[word] = math.log10(total_files / df[word])

    #calculate the TF-IDF score for each word
    tf_idf = []
    for word in tf:
        if word in idf:
            tf_idf.append((word, tf[word] * idf[word])) #store TF-IDF in a list of tuples

    #sort list of tuples by first increasing TF-IDF score
    #then, sort the list alphabetically
    tf_idf = sorted(tf_idf, key=lambda x: (x[1], x[0]))

    return tf_idf
    

   


if __name__ == "__main__":
    pass
    # ##Uncomment the following lines to test your implementation
    # ## Tests Problem 1: Prep Data
    test_directory = "tests/student_tests/"
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = prep_data(hello_world), prep_data(hello_friend)
    print(world) ## should print ['hello', 'world', 'hello', 'there']
    print(friend) ## should print ['hello', 'friends']

    # ## Tests Problem 2: Get Frequencies
    world_word_freq = get_frequencies(world)
    friend_word_freq = get_frequencies(friend)
    print(world_word_freq) ## should print {'hello': 2, 'world': 1, 'there': 1}
    print(friend_word_freq) ## should print {'hello': 1, 'friends': 1}

    # ## Tests Problem 3: Get Words Sorted by Frequency
    world_words_sorted_by_freq = get_words_sorted_by_frequency(world_word_freq)
    friend_words_sorted_by_freq = get_words_sorted_by_frequency(friend_word_freq)
    print(world_words_sorted_by_freq) ## should print ['there', 'world', 'hello']
    print(friend_words_sorted_by_freq) ## should print ['friends', 'hello']

    # ## Tests Problem 4: Most Frequent Word(s)
    freq1, freq2 = {"hello":5, "world":1}, {"hello":1, "world":5}
    most_frequent = get_most_frequent_words(freq1, freq2)
    print(most_frequent) ## should print ["hello", "world"]

    # ## Tests Problem 5: Similarity
    word_similarity = calculate_similarity_score(world_word_freq, friend_word_freq)
    print(word_similarity) ## should print 0.33

    # ## Tests Problem 6: Find TF-IDF
    text_file = 'tests/student_tests/hello_world.txt'
    text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    tf = get_tf(text_file)
    idf = get_idf(text_files)
    tf_idf = get_tfidf(text_file, text_files)
    print(tf) ## should print {'hello': 0.5, 'world': 0.25, 'there': 0.25}
    print(idf) ## should print {'there': 0.3010299956639812, 'world': 0.3010299956639812, 'hello': 0.0, 'friends': 0.3010299956639812}
    print(tf_idf) ## should print [('hello', 0.0), ('there', 0.0752574989159953), ('world', 0.0752574989159953)]
