import re
import random

class Board(object):
    def __init__(self):
        self.spaces = [[" " for i in range(3)] for j in range(3)]
        self.turn_ctr = 0

    def display_board(self):
        print(self.spaces)

    def display_winner(self):
        if self.turn_ctr % 2 == 0:
            print("X won the game!")
        else:
            print("O won the game!")

char_look_up = {"A":0, "B":1, "C":2}
corners = [[0,0], [0,2], [2,0], [2,2]]
edges = [[0,1], [1,0], [1,2], [2,1]]
center = [1,1]

def place_x_o(Game_bd):
    if Game_bd.turn_ctr % 2 == 0:
        x_turn(Game_bd)
    else:
        o_turn(Game_bd)

def x_turn(Game_bd):
    board_x_y = str_to_int()
    print(board_x_y)
    if Game_bd.spaces[board_x_y[0]][board_x_y[1] - 1] == " ":
        Game_bd.spaces[board_x_y[0]][board_x_y[1] - 1] = "X"  #return this?
    else:
        print("That space is already occupied! Pick another square")
        x_turn(Game_bd)   #return this?

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
    int_list = [None, None] #why cant i leave as empty list???
    int_list[0] = char_look_up[str_coords[0]]
    int_list[1] = int(str_coords[1])
    return int_list

def o_turn(Game_bd):
    board_x_y = o_choices(Game_bd)
    Game_bd.spaces[board_x_y[0]][board_x_y[1]] = "O"

def o_choices(Game_bd):
    # Opening move for "O"
    if Game_bd.turn_ctr == 2:
        if Game_bd.spaces[1][1] == "X":
            return random.choice(corners)
        else:
            return center
    # Every other move for "0"
    else:



        #

def score_board(Game_bd):
    three_in_a_row = False
    if Game_bd.turn_ctr % 2 == 0:
        token = "X"
    else:
        token = "O"
    #Score diagonals
    if Game_bd.spaces[1][1] == token:
        if Game_bd.spaces[0][0] and Game_bd.spaces[2][2] == token:
            three_in_a_row = True
        if Game_bd.spaces[2][0] and Game_bd.spaces[0][2] == token:
            three_in_a_row = True
    #Score horizontals
    for i in range(3):
        if Game_bd.spaces[i][0] and Game_bd.spaces[i][1] and Game_bd.spaces[i][2] == token:
            three_in_a_row = True
    #Score verticals
    for j in range(3):
        if Game_bd.spaces[0][j] and Game_bd.spaces[1][j] and Game_bd.spaces[2][j] == token:
            three_in_a_row = True
    return three_in_a_row

def play_game(Game_bd):
    win = False
    while Game_bd.turn_ctr < 10:
        Game_bd.display_board()
        place_x_o(Game_bd)
        if Game_bd.turn_ctr > 4:
            win = score_board(Game_bd)
            if win == True
                Game_bd.display_winner()#make a fuc of the class?
        Game_bd.turn_ctr += 1
        if Game_bd.turn_ctr == 9 and win == False:  #take the dis winner func out of the class can combine all 3 options in a func
            print("The game ends in a stalemate")


Game_bd = Board()
play_game(Game_bd)
