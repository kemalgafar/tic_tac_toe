

class Board(object):
    def __init__(self):
        self.initial_board = [[" " for i in range(3)] for j in range(3)]
        #self.is_x_turn = True
        self.total_moves = 0 #if you get to 9 then its a stale mate automatically? check this

    def active_board():
        current_board = 

    def display_board(self):


def play_turn():
    if self.total_moves % 2 == 0: #if zero it means its X's turn
        piece_to_place = "X"
    else:
        piece_to_place = "O"

    if piece_to_place == "X":
        #prompt user to play
        #user function
    else:
        #call automatic placment function for comp
        #use strategy

def x_turn():


def o_turn():


#determines if there is a winner for the game
#only need to check for the user that just went as they are the only ones changing state
#can use a simple counter for each of the 8 ways to check if won
# two for loops can check the horizontal and vertical cases
# diagonals will be taken care of each case
# if a " " appears anywhere in the check then its not a winner
def score_board():
