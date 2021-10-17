import random

new_list = []


# open the file
with open("wordlist.txt") as file:
    #read the line
    for line in file.readlines():
        # Split the line into words
        for word in line.split("\n"):   
            #Check each word's length and add to the privided list.
            if len(word) == 5:
                new_list.append(word)

class wordDatabase:

    """
    Class wordgDatabase is to perform all operations.
    It reads the text file with all the words, stores it in a list named new_list.
    And enables the random selection of the words.
    """
    def __init__(self, list_n):
        """
        It enables the random selection/choice of the words from list 'new_list'.

        """
        word_random = random.SystemRandom()
        word_chosen = word_random.choice(list_n)
        self.word_chosen = word_chosen




      



