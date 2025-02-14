from participant import Move, Prisoner

class Derek1(Prisoner):
   
    def __init__(self):
        self.last_move = Move.COOPERATE

    @classmethod
    def get_name(self) -> str:
        return "DerekJOne"
    
    def play(self) -> Move:
        move = Move.DEFECT
        if self.last_move == Move.DEFECT:
            move = Move.COOPERATE

        self.last_move = move
        return self.last_move


    def result(self, your_mdove: Move, their_move: Move, payout: int, their_payout: int) -> None:
        pass

        

