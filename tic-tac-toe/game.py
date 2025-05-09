from player import HumanPalyer, RandomComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #using single list to replicate 3X3 board
        self.current_winner = None #keeping track of the winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        """ 0 | 1 | 2 etc (tells us what number crosponds to what box)"""
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' '] #list comprehension of the bellow code

        """
        moves =  []
        for (i, spot) in enumerate(self.board):
            ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
            if spot == ' ':
                moves.append(i)
        return moves
        """
    def empty_squares(self):
        return ' ' in self.board
        
    def num_empty_squares(self):
        # return len(self.available_moves())
        return self.board.count(' ') #we can replace the above line by this line
        
    def make_move(self, square, letter):
        """if valid move then make that move(assign square to letter)
        then return true, if invalid return false"""
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
        
    def winner(self, square, letter):
        """winner if 3 in a row anywhere, we have to check all of these!
        first lets check the row
        """
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        #chekc column
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        #check diagonal
        # but only if the square in an even number(0, 2, 4. 6, 8)
        # these are the only posssible move to win diagonaly
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
            
        #if all checks fail
        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    """
    iterate while the game still has empty squares
    we dont have to worry about the winner because we'll just return that which breaks the loop
    """
    while game.empty_squares():
        """ get the moves from the appropriate player"""
        if letter == 'O':
            square = o_player.get_move(game)

        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f'makes a move to square {square}')
                game.print_board()
                print(' ') #just an empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X' #switches player
            # the above line comprehense the bellow code
            #if letter == 'X':
            #    letter = 'O'
            # else:
            #     letter = 'X'
        
        #putting a little time delay
        time.sleep(0.8)

    if print_game:
        print('it\'s a tie!')

if __name__ == '__main__':
    x_player = HumanPalyer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)