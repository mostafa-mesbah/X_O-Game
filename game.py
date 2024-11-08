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

    def is_win(self):
        """column winner"""
        if self.my_board.map[0][0] == self.my_board.map[1][0] == self.my_board.map[2][0] != " ":
            self.current_player.player1_add_score()
            print(f"winner is {self.current_player.player_name} with score = {self.current_player.player_score}")
            self.main_menu()
        elif self.my_board.map[0][1] == self.my_board.map[1][1] == self.my_board.map[2][1] != " ":
            self.current_player.player1_add_score()
            print(f"winner is {self.current_player.player_name} with score = {self.current_player.player_score}")
            self.main_menu()
        elif self.my_board.map[0][2] == self.my_board.map[1][2] == self.my_board.map[2][2] != " ":
            self.current_player.player1_add_score()
            print(f"winner is {self.current_player.player_name} with score = {self.current_player.player_score}")
            self.main_menu()

        """row winner"""

        if self.my_board.map[0][0] == self.my_board.map[0][1] == self.my_board.map[0][2] != " ":
            self.current_player.player1_add_score()
            print(f"winner is {self.current_player.player_name} with score = {self.current_player.player_score}")
            self.main_menu()
        elif self.my_board.map[1][0] == self.my_board.map[1][1] == self.my_board.map[1][2] != " ":
            self.current_player.player1_add_score()
            print(f"winner is {self.current_player.player_name} with score = {self.current_player.player_score}")
            self.main_menu()
        elif self.my_board.map[2][0] == self.my_board.map[2][1] == self.my_board.map[2][2] != " ":
            self.current_player.player1_add_score()
            print(f"winner is {self.current_player.player_name} with score = {self.current_player.player_score}")
            self.main_menu()

        """diagonal winner"""
        if self.my_board.map[0][0] == self.my_board.map[1][1] == self.my_board.map[2][2] != " ":
            self.current_player.player1_add_score()
            print(f"winner is {self.current_player.player_name} with score = {self.current_player.player_score}")
            self.main_menu()
        elif self.my_board.map[0][2] == self.my_board.map[1][1] == self.my_board.map[2][0] != " ":
            self.current_player.player1_add_score()
            print(f"winner is {self.current_player.player_name} with score = {self.current_player.player_score}")
            self.main_menu()

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

    def game(self):
        name, sign = map(str, input("enter the name then space then sign of the first player\n").split())
        self.player1 = Player(name,sign)
        name, sign = map(str, input("enter the name then space then sign of the second player\n").split())
        self.player2 = Player(name,sign)
        self.current_player = self.player1
        while 1 :
            self.my_board.show_board()
            row=None
            column = None
            ret = False
            while not ret:
                try:
                    row, column = map(int, input("enter the row then space then column\n").split())
                except ValueError:
                    print("Error: Please enter exactly two values.")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
                ret = self.check_row_column(row,column)
                self.my_board.show_board()
            if not ret:
                continue
            self.my_board.modify_board(row, column,self.current_player.player_sign)
            self.my_board.show_board()
            self.is_win()
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






























