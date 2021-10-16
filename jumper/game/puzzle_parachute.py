
class Puzzle_parachute:

    def __init__(self):
        pass

    '''draw_parachute just makes the parachute and holds its value in a string whether is complete or gone'''

 #def display_jumper():    
    parachute = [" ___","/___\ ", "\   /", " \ /"]
    jumper = ["  0 "," /|\ ", " / \ "," ","^^^^^^^"]


    for x in range(len(parachute)):
        print (parachute[x])
    for x in range(len(jumper)):
        print (jumper[x])


    '''remove_parachute_piece is only called if the input of correct guess is false, 
    it removes a part of the parachute  like in the pictures of the game.'''
    def remove_parachute_piece(parachute,jumper):
        del parachute[0]

    '''keep_playing is dependent on if the parachute is all gone and the head of the jumper 
    is "x" instead of "o" like the picture. If the person died (''x") then keep playing is f
    alse. Otherwise it is true.'''
def keep_playing(jumper):
    if jumper[0] != "x":
         True

    '''remove_parachute_piece is only called if the input of correct guess is false, 
    it removes a part of the parachute  like in the pictures of the game.'''     
def change_parachute_gone():
  jumper = ["  x "," /|\ ", " / \ "," ","^^^^^^^"]