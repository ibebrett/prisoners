from participant import Move, Prisoner
from collections import deque

class Jacob(Prisoner):
   
    def __init__(self):
        self.last_five = deque([])

    @classmethod
    def get_name(self) -> str:
        return "Jacob5"
    
    def play(self) -> Move:
        
        if self.last_five.count(Move.DEFECT) >= 3:
            return Move.DEFECT
        
        return Move.COOPERATE

    def result(self, your_move: Move, their_move: Move, payout: int, their_payout: int) -> None:
        self.last_five.appendleft(their_move)

        if len(self.last_five) > 5:
            self.last_five.pop()
        ...
        

