from participant import Move, Prisoner


class Defector(Prisoner):
    @classmethod
    def get_name(self) -> str:
        return "Defector"
    
    def play(self) -> Move:
        return Move.DEFECT
        
    def result(self, your_move: Move, their_move: Move, payout: int, their_payout: int) -> None:
        ...

