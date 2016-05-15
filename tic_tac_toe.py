# TODONE 1. Remove randomness from O's decsions, always go for the draw
# TODONE 2. Write a better display func, show the board properly
# TODO 3. Refactor functions, remove import random -> use dicts for lists
# TODO 4. PEP8 cleanup
# TODO 5. Ask whether the user wants to go first or not (will need to rewite O's decsions?)
# TODO 6. Write unit tests

import re
import random

class Board(object):
    def __init__(self):
        self.spaces = [[" " for i in range(3)] for j in range(3)]
        self.turn_ctr = 0
        self.char_look_up = {"A":0, "B":1, "C":2}
        # The 9 possible spaces
        self.corners = [[0,0], [0,2], [2,0], [2,2]] #make into dicts, then no need for importing rand??????????/
        self.edges = [[0,1], [1,0], [1,2], [2,1]]
        self.center = [[1,1]]
        # O's blocking move
        self.blocking = []

    def display_board(self):
        abc = ["A", "B", "C"]
        print("   1   2   3\n")
        for i in range(3):
            if i > 0:
                print("     |   |  ")
            print(abc[i]+"  "+self.spaces[i][0]+" | "+self.spaces[i][1]+" | "+self.spaces[i][2])
            if i < 2:
                print("   __|___|__")
        print("\n")

    def display_winner(self):
        if self.turn_ctr % 2 == 0:
            print("X won the game!")
        else:
            print("O won the game!")

    def place_x_o(self):
        if self.turn_ctr % 2 == 0:
            self.x_turn()
        else:
            self.o_turn()

    def x_turn(self):
        x_coord = self.str_to_int()
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
        if self.turn_ctr == 1:
            if self.spaces[1][1] == "X":
                random.shuffle(self.corners)
                return self.corners.pop()
            else:
                return self.center.pop()
        # Every other move for "0"
        else:
            if self.turn_ctr > 2:
                self.o_block()

            if self.blocking != []:
                return self.blocking.pop()
            else:
                remaining_spaces = (self.corners + self.edges + self.center)
                try:
                    remaining_spaces.remove([])
                except:
                    pass
                return random.choice(remaining_spaces)

    def o_block(self):
        #TAKE THIS FUNC, USE TOKENS TO SEE WHEN A POSSIBLE 3 IN A ROW FOR 0 IS POSSIBLE AND UTILIZE ###############3
        #MAKE TOKENS PART OF THE CLASS? Make a func to change tokens at end of every turn? ##################
        #Need to check each of the 8 possibilities (is there a better way?) #######################
        # Permutations of case #1 (Diagonal \)
        if (self.spaces[0][0] == "X") and (self.spaces[1][1] == "X") and (self.spaces[2][2] == " "):
            self.blocking.append([2,2])
        elif (self.spaces[0][0] == "X") and (self.spaces[2][2] == "X") and (self.spaces[1][1] == " "):
            self.blocking.append([1,1])
        elif (self.spaces[1][1] == "X") and (self.spaces[2][2] == "X") and (self.spaces[0][0] == " "):
            self.blocking.append([0,0])
        # Permutations of case #2 (Diagonal /)
        elif (self.spaces[2][0] == "X") and (self.spaces[1][1] == "X") and (self.spaces[0][2] == " "):
            self.blocking.append([0,2])
        elif (self.spaces[2][0] == "X") and (self.spaces[0][2] == "X") and (self.spaces[1][1] == " "):
            self.blocking.append([1,1])
        elif (self.spaces[1][1] == "X") and (self.spaces[0][2] == "X") and (self.spaces[2][0] == " "):
            self.blocking.append([2,0])
        # Permutations of case #3 (Row 1 Horizontal)
        elif (self.spaces[0][0] == "X") and (self.spaces[0][1] == "X") and (self.spaces[0][2] == " "):
            self.blocking.append([0,2])
        elif (self.spaces[0][0] == "X") and (self.spaces[0][2] == "X") and (self.spaces[0][1] == " "):
            self.blocking.append([0,1])
        elif (self.spaces[0][1] == "X") and (self.spaces[0][2] == "X") and (self.spaces[0][0] == " "):
            self.blocking.append([0,0])
        # Permutations of case #4 (Row 2 Horizontal)
        elif (self.spaces[1][0] == "X") and (self.spaces[1][1] == "X") and (self.spaces[1][2] == " "):
            self.blocking.append([1,2])
        elif (self.spaces[1][0] == "X") and (self.spaces[1][2] == "X") and (self.spaces[1][1] == " "):
            self.blocking.append([1,1])
        elif (self.spaces[1][1] == "X") and (self.spaces[1][2] == "X") and (self.spaces[1][0] == " "):
            self.blocking.append([1,0])
        # Permutations of case #5 (Row 3 Horizontal)
        elif (self.spaces[2][0] == "X") and (self.spaces[2][1] == "X") and (self.spaces[2][2] == " "):
            self.blocking.append([2,2])
        elif (self.spaces[2][0] == "X") and (self.spaces[2][2] == "X") and (self.spaces[2][1] == " "):
            self.blocking.append([2,1])
        elif (self.spaces[2][1] == "X") and (self.spaces[2][2] == "X") and (self.spaces[2][0] == " "):
            self.blocking.append([2,0])
        # Permutations of case #6 (Col 1 Vertical)
        elif (self.spaces[0][0] == "X") and (self.spaces[2][0] == "X") and (self.spaces[1][0] == " "):
            self.blocking.append([1,0])
        elif (self.spaces[0][0] == "X") and (self.spaces[1][0] == "X") and (self.spaces[2][0] == " "):
            self.blocking.append([2,0])
        elif (self.spaces[1][0] == "X") and (self.spaces[2][0] == "X") and (self.spaces[0][0] == " "):
            self.blocking.append([0,0])
        # Permutations of case #7 (Col 2 Vertical)
        elif (self.spaces[0][1] == "X") and (self.spaces[2][1] == "X") and (self.spaces[1][1] == " "):
            self.blocking.append([1,1])
        elif (self.spaces[0][1] == "X") and (self.spaces[1][1] == "X") and (self.spaces[2][1] == " "):
            self.blocking.append([2,1])
        elif (self.spaces[1][1] == "X") and (self.spaces[2][1] == "X") and (self.spaces[0][1] == " "):
            self.blocking.append([0,1])
        # Permutations of case #8 (Col 3 Vertical)
        elif (self.spaces[0][2] == "X") and (self.spaces[2][2] == "X") and (self.spaces[1][2] == " "):
            self.blocking.append([1,2])
        elif (self.spaces[0][2] == "X") and (self.spaces[1][2] == "X") and (self.spaces[2][2] == " "):
            self.blocking.append([2,2])
        else:
            self.blocking.append([0,2])

        # Removing the coordinate from possible moves to prevent dupes
        if self.blocking[0] in self.corners:
            self.corners.remove(self.blocking[0])
        if self.blocking[0] in self.edges:
            self.edges.remove(self.blocking[0])
        if self.blocking[0] in self.center:
            self.center.remove(self.blocking[0])

    def score_board(self):
        three_in_a_row = False
        if self.turn_ctr % 2 == 0:
            token = "X"
        else:
            token = "O"
        # Score diagonals
        if self.spaces[1][1] == token:
            if (self.spaces[0][0] == token) and (self.spaces[2][2] == token):
                three_in_a_row = True
            if (self.spaces[0][2] == token) and (self.spaces[2][0] == token):
                three_in_a_row = True
        # Score horizontals
        for i in range(3):
            if (self.spaces[i][0] == token) and (self.spaces[i][1] == token) and (self.spaces[i][2] == token):
                three_in_a_row = True
        # Score verticals
        for j in range(3):
            if (self.spaces[0][j] == token) and (self.spaces[1][j] == token) and (self.spaces[2][j] == token):
                three_in_a_row = True
        return three_in_a_row

    def play_game(self):
        win = False
        while self.turn_ctr < 10:
            self.display_board()
            self.place_x_o()
            if self.turn_ctr > 3:
                win = self.score_board()
                if win == True:
                    self.display_board()
                    self.display_winner()
                    break
            self.turn_ctr += 1
            if self.turn_ctr == 9 and win == False:  #take the dis winner func out of the class can combine all 3 options in a func###########
                self.display_board()
                print("The game ends in a stalemate")
                break


Game_bd = Board()
Game_bd.play_game()
