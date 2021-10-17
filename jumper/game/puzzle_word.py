from game.console import Console
import random

class Puzzle_word:

  def __init__(self):
    self.word_list = ["cat","book","house","no"]
    self.random_word = (random_word)
    self.user_guess = ""
    self.display_letters = []
    self.correct_letters =[]
    
  def pick_random_word(self):
    random_word = random.choice(self.word_list)
    return random_word.lower()


  def draw_word_blank(self):
    #draw word black function to start
    for letter in range(len(self.random_word)): 
      self.display_letters += "_"
      print(self.display_letters)


  def process_guess(self):

    for letter in self.random_word:
        if(letter in self.correct_letters):
          print(letter, end=" ")
        else:
          print('_', end =' ')
        print()
  #process_guess function 
    if self.user_guess in self.correct_letters:
      self.correct_guess = True
    else:
      self.orrect_guess = False
    if self.correct_guess == True:
      for x in range(len(self.random_word)):
        #this goes through each letter and checks if it matches the user guess
          if self.user_guess == self.correct_letters[x]:
            #if it matches it adds it to the correct position on the display
              display_letters[x] = user_guess


  def keep_playing():
    pass
  
#chooses random word from list pick_random_word function


# #draw word black function to start
#     for x in range(len(self.random_word)):
#       self.display_letters += "_"
#       print(display_letters)
# #initialize variables
# user_guess = ""
# display_letters = []
# correct_letters =[]

#converts random word into list of correct letters
correct_letters[:0] = random_word



#user input
user_guess =(input("Pick a letter[a-z]: "))

# #process_guess function 
# if user_guess in correct_letters:
#     correct_guess = True
# else:
#     correct_guess = False
# if correct_guess == True:
#     for x in range(len(random_word)):
#       #this goes through each letter and checks if it matches the user guess
#         if user_guess == correct_letters[x]:
#           #if it matches it adds it to the correct position on the display
#             display_letters[x] = user_guess

#probably another function like "def convert_list_to_string()""
#converts display letter list to a string
display_string = " ".join(display_letters)
print(display_string)

#The only function not finished is the keep playing function
#which just needs to check if all the items in the display_letters list
#and see if none of them = "_"

#once again dont worry if you dont finish, we will do better next time!

