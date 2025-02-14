import random
from participant import Move, Prisoner

class Zack(Prisoner):
    def __init__(self):
        self.betrayed = False
        self.moveNum = 0
    @classmethod
    def get_name(self) -> str:
        return "Zack"
    
    def play(self) -> Move:
        if self.moveNum == 0:
            self.moveNum +=1
            return Move.DEFECT
        if not self.betrayed:
            return Move.COOPERATE
        return Move.DEFECT
        
    def result(self, your_move: Move, their_move: Move, payout: int, their_payout: int) -> None:
        if their_move == "DEFECT":
            self.betrayed = True