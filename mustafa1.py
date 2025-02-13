import random
from participant import Prisoner, Move

class Mustafa1(Prisoner):
    def __init__(self):
        self.history = []
        self.currentDefected = 0
        self.currentCooperated = 0
        self.opDefected = 0
        self.opCooperated = 0
    
    @classmethod
    def get_name(self) -> str:
        return "mustafa1"
    
    def play(self) -> Move:
        
        if len(self.history) == 0:
            return Move.DEFECT
        if len(self.history) == 1:
            return Move.DEFECT
        
        if self.history[-1][1] == Move.DEFECT and self.history[-2][1] == Move.DEFECT:
            return Move.DEFECT
        
        if self.history[-1][1] == Move.DEFECT:
            return Move.DEFECT
        
        return self.decideMove()
    
    def decideMove(self) -> Move:
        return random.choices([Move.DEFECT, Move.COOPERATE], weights=[1, 2])[0]

    
    def printHistory(self):
        for i in self.history:
            print(i)
    
    def result(self, your_move: Move, their_move: Move, payout: int, their_payout: int) -> None:
        self.history.append((your_move, their_move, payout, their_payout))
        if your_move == Move.DEFECT:
            self.currentDefected += 1
        else:
            self.currentCooperated += 1
            
        if their_move == Move.DEFECT:
            self.opDefected += 1
        else:
            self.opCooperated += 1
            
        
        