import sys

class Map:
    def __init__(self):
        self.map = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.input = "x"

    def show_map(self):
        print(f"{self.map[0][0]}|{self.map[0][1]}|{self.map[0][2]}\n------")
        print(f"{self.map[1][0]}|{self.map[1][1]}|{self.map[1][2]}\n------")
        print(f"{self.map[2][0]}|{self.map[2][1]}|{self.map[2][2]}\n")
    def modify_map(self,row,column):
        row=row-1
        column=column-1
        if self.input == "x":
            the_input= "x"
            self.map[row][column] = the_input
            self.input = "o"
        elif self.input == "o":
            the_input= "o"
            self.map[row][column] = the_input
            self.input = "x"
    def is_win(self):
        """column winner"""
        if self.map[0][0] == self.map[1][0] == self.map[2][0] != " ":
            print(f"winner is {self.map[0][0]}")
            self.main_menu()
        if self.map[0][1] == self.map[1][1] == self.map[2][1] != " ":
            print(f"winner is {self.map[0][0]}")
            self.main_menu()
        if self.map[0][2] == self.map[1][2] == self.map[2][2] != " ":
            print(f"winner is {self.map[0][0]}")
            self.main_menu()

        """row winner"""

        if self.map[0][0] == self.map[0][1] == self.map[0][2] != " ":
            print(f"winner is {self.map[0][0]}")
            self.main_menu()
        if self.map[1][0] == self.map[1][1] == self.map[1][2] != " ":
            print(f"winner is {self.map[1][1]}")
            self.main_menu()
        if self.map[2][0] == self.map[2][1] == self.map[2][2] != " ":
            print(f"winner is {self.map[2][2]}")
            self.main_menu()

        """diagonal winner"""
        if self.map[0][0] == self.map[1][1] == self.map[2][2] != " ":
            print(f"winner is {self.map[0][0]}")
            self.main_menu()
        if self.map[0][2] == self.map[1][1] == self.map[2][0] != " ":
            print(f"winner is {self.map[2][0]}")
            self.main_menu()

    """could be in separate class"""
    def main_menu(self):
        print("welcome to x_o game")
        ret = False
        option =None
        while ret == False:
            option = str(input("1) enter start to start playing \n2) enter quit to leave\n"))
            ret = self.check_main_menu_input(option)
        if option == str("start"):
            self.game()
        elif option == str("quit"):
            sys.exit(0)

    def game(self):
        while 1 :
            self.show_map()
            row=None
            column = None
            ret = False
            while ret == False:
                try:
                    row, column = map(int, input("enter the row then space then column\n").split())
                except ValueError:
                    print("Error: Please enter exactly two values.")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
                ret = self.check_row_column(row,column)
                self.show_map()
            if not ret:
                continue
            self.modify_map(row, column)
            self.show_map()
            self.is_win()

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