from participant import Move, Prisoner
from collections import deque

class Jacob1(Prisoner):
   
    def __init__(self):
        self.last_move = Move.COOPERATE

    @classmethod
    def get_name(self) -> str:
        return "Jacob1"
    
    def play(self) -> Move:
        return self.last_move

    def result(self, your_mdove: Move, their_move: Move, payout: int, their_payout: int) -> None:
        self.last_move = their_move

        

