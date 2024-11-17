import sys

from board import Board
from player import Player

class Game:
    def __init__(self):
        self.my_board = Board()
        self.player1=None
        self.player2 = None
        self.current_player = None

    def start_game(self):
        self.main_menu()

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        elif self.current_player == self.player2:
            self.current_player = self.player1

    def is_draw(self):
        empty_flag = False
        for i in range(0, 3):
            for j in range(0, 3):
                if self.my_board.map[i][j] == " ":
                    empty_flag = True
        if not empty_flag:
            print("DRAW")
            print(f"{self.current_player.player_name} with score = {self.current_player.player_score} \n ")
            self.switch_player()
            print(f"{self.current_player.player_name} with score = {self.current_player.player_score} \n ")
            self.main_menu()

    def winnig_action(self):
        self.current_player.player_add_score()
        print(f"winner is {self.current_player.player_name} with score = {self.current_player.player_score}")
        self.main_menu()


    def is_win(self):
        """column winner"""
        for i in range(0, 2):
            if self.my_board.map[0][i] == self.my_board.map[1][i] == self.my_board.map[2][i] != " ":
                self.winnig_action()
        """row winner"""
        for i in range(0,2):
            if self.my_board.map[i][0] == self.my_board.map[i][1] == self.my_board.map[i][2] != " ":
                self.winnig_action()

        """diagonal winner"""
        if self.my_board.map[0][0] == self.my_board.map[1][1] == self.my_board.map[2][2] != " ":
            self.winnig_action()
        elif self.my_board.map[0][2] == self.my_board.map[1][1] == self.my_board.map[2][0] != " ":
            self.winnig_action()

            self.is_draw()


    """could be in separate class"""
    def main_menu(self):
        print("welcome to x_o game")
        ret = False
        option =None
        while not ret:
            option = str(input("1) enter start to start playing \n2) enter quit to leave\n"))
            ret = self.check_main_menu_input(option)
        if option == str("start"):
            self.game()
        elif option == str("quit"):
            sys.exit(0)
    def  creat_players(self):
        while True:
            try:
                name, sign = map(str, input("enter the name then space then sign of the first player\n").split())
                self.player1 = Player(name, sign)
                break
            except ValueError:
                # Catch the error when there aren't exactly two inputs
                print("Error: Please enter both a name and a symbol (e.g., 'Alice X'). Try again.")
        while True:
            try:
                name, sign = map(str, input("enter the name then space then sign of the second player\n").split())
                self.player2 = Player(name, sign)
                break
            except ValueError:
                # Catch the error when there aren't exactly two inputs
                print("Error: Please enter both a name and a symbol (e.g., 'Alice X'). Try again.")
        self.current_player = self.player1
    def game(self):
        self.creat_players()
        self.my_board.show_board()
        while True :
            row=None
            column = None
            ret = False
            while not ret:
                    print(f"{self.current_player.player_name} turn")
                    try:
                        # Get input and try to convert it to integers
                        row, column = map(int, input("Enter the row then space then column (e.g., '1 1').\n").split())

                        # Check if the row and column are valid within the board range
                        if not self.check_row_column(row, column):
                            print("Invalid row or column. Please try again.")
                            continue

                        # Check if the cell is already occupied
                        if not self.check_a_play(row, column):
                            print("The cell is already occupied. Please choose another.")
                            continue

                        # If both checks pass, we can proceed with the move
                        ret = True
                    except ValueError:
                        print("Invalid input. Please enter two integers separated by a space.")
                    except IndexError:
                        print("Out of bounds. Please ensure the row and column are within the board dimensions.")

            self.my_board.modify_board(row, column,self.current_player.player_sign)
            self.my_board.show_board()
            self.is_win()
            self.is_draw()
            self.switch_player()

    @staticmethod
    def check_row_column(row, column) -> bool  :
        if row > 3 or row < 1:
            print("invalid input")
            print("try again")
            return False
        elif column > 3 or column < 1:
            print("invalid input")
            print("try again")
            return False
        else:
            return True

    @staticmethod
    def check_main_menu_input(option : str) -> bool:
        if (option != "start") and (option != "quit"):
            print("invalid input")
            print("try again")
            return False
        else:
            return True


    def check_a_play(self,row, column):
        row=row-1
        column=column-1
        if self.my_board.map[row][column] != " ":
            print("can't play here")
            return False
        else:
            return True




























