# A simple tic-tac-toe game

import re
import random

class Board(object):
    def __init__(self):
        self.spaces = [[" " for i in range(3)] for j in range(3)]
        self.turn_counter = 0
        # 'token' is just that, a token value that can be either 'X' or 'O'
        self.token = ""
        self.char_look_up = {"A":0, "B":1, "C":2}
        # The 9 possible spaces
        self.corners = [[0,0], [0,2], [2,0], [2,2]]
        self.edges = [[0,1], [1,0], [1,2], [2,1]]
        self.center = [[1,1]]
        # O's blocking or_winning move
        self.win_block_coord = []

    def display_board(self):
        abc = ["A", "B", "C"]
        print("   1   2   3\n")
        for i in range(3):
            if i > 0:
                print("     |   |  ")
            print(abc[i]
                  + "  "
                  + self.spaces[i][0]
                  + " | " +self.spaces[i][1]
                  + " | " +self.spaces[i][2])
            if i < 2:
                print("   __|___|__")
        print("\n")

    def decide_turn(self):
        if self.turn_counter % 2 == 0:
            self.token = "X"
        else:
            self.token = "O"

    def display_winner(self):
        if self.token == "X":
            print("X won the game!")
        else:
            print("O won the game!")

    def place_x_o(self):
        if self.token == "X":
            self.x_turn()
        else:
            self.o_turn()

    def x_turn(self):
        x_coord = self.str_to_int()
        # x_coord is a two element array where index[0]
        # is the x-coordinate index[1] is the y-coordinate
        # Since user input/counting starts at '1' simple
        # subtraction is needed to make the coordinate useful
        if self.spaces[x_coord[0]][x_coord[1] - 1] == " ":
            if [x_coord[0], x_coord[1] - 1] in self.corners:
                self.corners.remove([x_coord[0], x_coord[1] - 1])
            elif [x_coord[0], x_coord[1] - 1] in self.edges:
                self.edges.remove([x_coord[0], x_coord[1] - 1])
            else:
                self.center.remove([x_coord[0], x_coord[1] - 1])
            self.spaces[x_coord[0]][x_coord[1] - 1] = "X"
        else:
            print("That space is already occupied! Pick another square")
            self.x_turn()

    def user_input(self):
        print("X's turn!\nPlease enter in a coordinate to place an X")
        user_string = input(">  ")
        return user_string

    def check_input(self):
        str = self.user_input().upper()
        matches = re.search(r'([a-cA-C])([1-3])', str)
        if matches:
            return [match for match in matches.groups()]
        else:
            print("Erroneous input, please try again")
            return self.check_input()

    def str_to_int(self):
        str_coords = self.check_input()
        int_list = []
        int_list.append(self.char_look_up[str_coords[0]])
        int_list.append(int(str_coords[1]))
        return int_list

    def o_turn(self):
        print("O's turn!")
        o_coord = self.o_choices()
        self.spaces[o_coord[0]][o_coord[1]] = "O"

    def o_choices(self):
        # Opening move for "O"
        if self.turn_counter == 1:
            if self.spaces[1][1] == "X":
                random.shuffle(self.corners)
                return self.corners.pop()
            else:
                return self.center.pop()
        # Every other move for "0"
        else:
            if self.turn_counter > 2:
                self.o_win_or_block("O")
                if self.win_block_coord == []:
                    self.o_win_or_block("X")
                if self.win_block_coord != []:
                    return self.win_block_coord.pop()
            if self.turn_counter == 3 and len(self.corners) == 2:
                return self.edges.pop()
            else:
                remaining_spaces = (self.corners + self.edges + self.center)
                try:
                    remaining_spaces.remove([])
                except:
                    pass
                return random.choice(remaining_spaces)

    def o_win_or_block(self, win_or_block):
        # Permutations of case #1 (Diagonal \)
        if (self.spaces[0][0] == win_or_block and
                self.spaces[1][1] == win_or_block and
                self.spaces[2][2] == " "):
            self.win_block_coord.append([2,2])
        elif (self.spaces[0][0] == win_or_block and
                self.spaces[2][2] == win_or_block and
                self.spaces[1][1] == " "):
            self.win_block_coord.append([1,1])
        elif (self.spaces[1][1] == win_or_block and
                self.spaces[2][2] == win_or_block and
                self.spaces[0][0] == " "):
            self.win_block_coord.append([0,0])
        # Permutations of case #2 (Diagonal /)
        elif (self.spaces[2][0] == win_or_block and
                self.spaces[1][1] == win_or_block and
                self.spaces[0][2] == " "):
            self.win_block_coord.append([0,2])
        elif (self.spaces[2][0] == win_or_block and
                self.spaces[0][2] == win_or_block and
                self.spaces[1][1] == " "):
            self.win_block_coord.append([1,1])
        elif (self.spaces[1][1] == win_or_block and
                self.spaces[0][2] == win_or_block and
                self.spaces[2][0] == " "):
            self.win_block_coord.append([2,0])
        # Permutations of case #3 (Row 1 Horizontal)
        elif (self.spaces[0][0] == win_or_block and
                self.spaces[0][1] == win_or_block and
                self.spaces[0][2] == " "):
            self.win_block_coord.append([0,2])
        elif (self.spaces[0][0] == win_or_block and
                self.spaces[0][2] == win_or_block and
                self.spaces[0][1] == " "):
            self.win_block_coord.append([0,1])
        elif (self.spaces[0][1] == win_or_block and
                self.spaces[0][2] == win_or_block and
                self.spaces[0][0] == " "):
            self.win_block_coord.append([0,0])
        # Permutations of case #4 (Row 2 Horizontal)
        elif (self.spaces[1][0] == win_or_block and
                self.spaces[1][1] == win_or_block and
                self.spaces[1][2] == " "):
            self.win_block_coord.append([1,2])
        elif (self.spaces[1][0] == win_or_block and
                self.spaces[1][2] == win_or_block and
                self.spaces[1][1] == " "):
            self.win_block_coord.append([1,1])
        elif (self.spaces[1][1] == win_or_block and
                self.spaces[1][2] == win_or_block and
                self.spaces[1][0] == " "):
            self.win_block_coord.append([1,0])
        # Permutations of case #5 (Row 3 Horizontal)
        elif (self.spaces[2][0] == win_or_block and
                self.spaces[2][1] == win_or_block and
                self.spaces[2][2] == " "):
            self.win_block_coord.append([2,2])
        elif (self.spaces[2][0] == win_or_block and
                self.spaces[2][2] == win_or_block and
                self.spaces[2][1] == " "):
            self.win_block_coord.append([2,1])
        elif (self.spaces[2][1] == win_or_block and
                self.spaces[2][2] == win_or_block and
                self.spaces[2][0] == " "):
            self.win_block_coord.append([2,0])
        # Permutations of case #6 (Col 1 Vertical)
        elif (self.spaces[0][0] == win_or_block and
                self.spaces[2][0] == win_or_block and
                self.spaces[1][0] == " "):
            self.win_block_coord.append([1,0])
        elif (self.spaces[0][0] == win_or_block and
                self.spaces[1][0] == win_or_block and
                self.spaces[2][0] == " "):
            self.win_block_coord.append([2,0])
        elif (self.spaces[1][0] == win_or_block and
                self.spaces[2][0] == win_or_block and
                self.spaces[0][0] == " "):
            self.win_block_coord.append([0,0])
        # Permutations of case #7 (Col 2 Vertical)
        elif (self.spaces[0][1] == win_or_block and
                self.spaces[2][1] == win_or_block and
                self.spaces[1][1] == " "):
            self.win_block_coord.append([1,1])
        elif (self.spaces[0][1] == win_or_block and
                self.spaces[1][1] == win_or_block and
                self.spaces[2][1] == " "):
            self.win_block_coord.append([2,1])
        elif (self.spaces[1][1] == win_or_block and
                self.spaces[2][1] == win_or_block and
                self.spaces[0][1] == " "):
            self.win_block_coord.append([0,1])
        # Permutations of case #8 (Col 3 Vertical)
        elif (self.spaces[0][2] == win_or_block and
                self.spaces[2][2] == win_or_block and
                self.spaces[1][2] == " "):
            self.win_block_coord.append([1,2])
        elif (self.spaces[0][2] == win_or_block and
                self.spaces[1][2] == win_or_block and
                self.spaces[2][2] == " "):
            self.win_block_coord.append([2,2])
        elif (self.spaces[1][2] == win_or_block and
                self.spaces[2][2] == win_or_block and
                self.spaces[0][2] == " "):
            self.win_block_coord.append([0,2])
        # Removing the coordinate from possible moves to prevent dupes
        try:
            if self.win_block_coord[0] in self.corners:
                self.corners.remove(self.win_block_coord[0])
            if self.win_block_coord[0] in self.edges:
                self.edges.remove(self.win_block_coord[0])
            if self.win_block_coord[0] in self.center:
                self.center.remove(self.win_block_coord[0])
        except:
            pass

    def score_board(self):
        three_in_a_row = False
        # Score diagonals
        if self.spaces[1][1] == self.token:
            if (self.spaces[0][0] == self.token and
                    self.spaces[2][2] == self.token):
                three_in_a_row = True
            if (self.spaces[0][2] == self.token and
                    self.spaces[2][0] == self.token):
                three_in_a_row = True
        # Score horizontals
        for i in range(3):
            if (self.spaces[i][0] == self.token and
                    self.spaces[i][1] == self.token and
                    self.spaces[i][2] == self.token):
                three_in_a_row = True
        # Score verticals
        for j in range(3):
            if (self.spaces[0][j] == self.token and
                    self.spaces[1][j] == self.token and
                    self.spaces[2][j] == self.token):
                three_in_a_row = True
        return three_in_a_row

    def play_game(self):
        win = False
        while self.turn_counter < 10:
            self.display_board()
            self.decide_turn()
            self.place_x_o()
            if self.turn_counter > 3:
                win = self.score_board()
                if win == True:
                    self.display_board()
                    self.display_winner()
                    break
            self.turn_counter += 1
            if self.turn_counter == 9 and win == False:
                self.display_board()
                print("The game ends in a stalemate")
                break


Game_bd = Board()
Game_bd.play_game()
