from participant import Move, Prisoner


class Defector(Prisoner):
    def __init__(self):
        self.lastOpMove = 0
    
    @classmethod
    def get_name(self) -> str:
        return "Defector"
    
    def play(self) -> Move:
        return self.lastOpMove
        
    def result(self, your_move: Move, their_move: Move, payout: int, their_payout: int) -> None:
        self.lastOpMove = their_move

