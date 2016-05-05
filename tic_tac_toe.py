import re

class Board(object):
    def __init__(self):
        self.initial_board = [[" " for i in range(3)] for j in range(3)]
        self.turn_ctr = 0 #if you get to 9 then its a stale mate automatically? check this

    def display_board(self):
        print(self.initial_board)

char_look_up = {"A":0, "B":1, "C":2}

def place_x_o(Test):

    if Test.turn_ctr % 2 == 0:
        x_turn(Test)
    else:
        o_turn(Test)

def x_turn(Test):
    board_x_y = str_to_int()
    print(board_x_y)

    if Test.initial_board[board_x_y[0]][board_x_y[1] - 1] == " ":
        Test.initial_board[board_x_y[0]][board_x_y[1] - 1] = "X"
    else:
        x_turn(Test)

    Test.turn_ctr += 1


'''
def o_turn(Test):
    #look up strat
'''

def user_input():
    print("X's turn!\nPlease enter in a coordinate to place an X")
    user_string = input(">  ")
    return user_string

def check_input():
    str = user_input().upper()
    matches = re.search(r'([a-cA-C])([1-3])', str)
    if matches:
        return [match for match in matches.groups()]
    else:
        print("Erroneous input, please try again")
        return check_input()

def str_to_int():

    str_coords = check_input()
    int_list = [None, None] #why cant i leave as empty list
    int_list[0] = char_look_up[str_coords[0]]
    int_list[1] = int(str_coords[1])

    return int_list

'''
#determines if there is a winner for the game
#only need to check for the user that just went as they are the only ones changing state
#from turn 5 onward score
#can use a simple counter for each of the 8 ways to check if won
# two for loops can check the horizontal and vertical cases
# diagonals will be taken care of each case
# if a " " appears anywhere in the check then its not a winner
def score_board():
'''

def play_game():


Test = Board()
x_turn(Test)
Test.display_board
