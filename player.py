class Player:
    def __init__(self,name :str,sign:str):
        self.player_name= name
        self.player_sign:str = sign
        self.player_score= 0


    def player_add_score(self):
        self.player_score+=1
