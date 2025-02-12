from participant import Move, Prisoner
#from collections import deque

class Memory(Prisoner):
   
    def __init__(self):
        self.enemy_moves = []

    @classmethod
    def get_name(self) -> str:
        return "Memory"
    
    def play(self) -> Move:
        
        if self.enemy_moves.count(Move.DEFECT) >= len(self.enemy_moves) // 2:
            return Move.DEFECT
        
        return Move.COOPERATE

    def result(self, your_move: Move, their_move: Move, payout: int, their_payout: int) -> None:
        self.enemy_moves.append(their_move)

        ...
        

