import random
from participant import Move, Prisoner


class Amilcar1(Prisoner):
    def __init__(self):
        super().__init__()
        self.coop_probability = 0.50
        self.their_history = []
        self.game_count = 0


    @classmethod
    def get_name(self) -> str:
        return "Amilcar1"

    def play(self) -> Move:
        if self.their_history:
            self.coop_rate = sum(1 for move in self.their_history if move == Move.COOPERATE) / len(self.their_history)

            self.coop_probability = 0.2 + self.coop_rate * 0.9
        self.game_count += 1
        if random.random() < self.coop_probability:
            return Move.COOPERATE
        else:
            return Move.DEFECT

    def result(self, your_move: Move, their_move: Move, payout: int,
               their_payout: int) -> None:
        self.their_history.append(their_move)
