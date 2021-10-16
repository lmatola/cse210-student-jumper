from game.console import Console


class Puzzle_Parachute:

    def __init__(self):
        self.parachute = [" ___","/___\ ", "\   /", " \ /"]
        self.jumper = ["  0 "," /|\ ", " / \ "," ","^^^^^^^"]


    '''draw_parachute just makes the parachute and holds its value in a string whether is complete or gone'''


    def draw_parachute(self):    
        for part in self.parachute:
            print (part)
        for part in self.jumper:
            print (part)


    '''remove_parachute_piece is only called if the input of correct guess is false, 
    it removes a part of the parachute  like in the pictures of the game.'''
    def remove_parachute_piece(self):
        self.parachute.pop(0)

    '''keep_playing is dependent on if the parachute is all gone and the head of the jumper 
    is "x" instead of "o" like the picture. If the person died (''x") then keep playing is f
    alse. Otherwise it is true.'''
    def keep_playing(self):
        keep_playing = True

        if len(self.parachute) == 0:
            keep_playing = False

        return keep_playing

    '''remove_parachute_piece is only called if the input of correct guess is false, 
    it removes a part of the parachute  like in the pictures of the game.'''     
    def change_parachute_gone(self):
        self.jumper = ["  x "," /|\ ", " / \ "," ","^^^^^^^"]