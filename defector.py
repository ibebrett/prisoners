class CoinFlipper(Prisoner):
    @classmethod
    def get_name(self) -> str:
        return "CoinFlipper"
    
    def play(self) -> Move:
        if random.random() < 0.5:
            return Move.COOPERATE
        else:
            return Move.DEFECT
        
    def result(self, your_move: Move, their_move: Move, payout: int, their_payout: int) -> None:
        ...

