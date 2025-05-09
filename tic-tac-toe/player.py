import math
import random

class Player:
    def __init__(self, letter):
        # letter is X or Y
        self.letter = letter

    #we want all players to get their next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPalyer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            """we are going to check if it is a correct value by trying to cast
            it to an integer, and if it is not, theb we say its valid
            if that spot is not vailable on the board, we also say its invalid"""

            square = input(self.letter + '\'s turn. input move (0-8):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True #if these are sucessfull, hurrah 
            
            except ValueError:
                print("invalid square! try again.")

        return val
    
