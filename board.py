class Board:
    def __init__(self):
        self.map = [[" "," "," "],[" "," "," "],[" "," "," "]]
    def show_board(self):
        print(f"{self.map[0][0]}|{self.map[0][1]}|{self.map[0][2]}\n------")
        print(f"{self.map[1][0]}|{self.map[1][1]}|{self.map[1][2]}\n------")
        print(f"{self.map[2][0]}|{self.map[2][1]}|{self.map[2][2]}\n")

    def modify_board(self,row,column,sign:str):
        row=row-1
        column=column-1
        self.map[row][column] = sign
    def clear_board(self):
        self.map = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]




