import random
from participant import Move, Prisoner


class Amilcar1(Prisoner):
    def __init__(self):
        super().__init__()
        self.cooperation = 0.1
        self.their_history = []

    @classmethod
    def get_name(self) -> str:
        return "Amilcar1"

    def play(self) -> Move:
        if random.random() < 0.1:
            return Move.COOPERATE
        else:
            return Move.DEFECT

    def result(self, your_move: Move, their_move: Move, payout: int,
               their_payout: int) -> None:
        ...
