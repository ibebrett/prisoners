import abc
from dataclasses import dataclass
from enum import StrEnum

class Move(StrEnum):
    COOPERATE = "COOPERATE"
    DEFECT = "DEFECT"

PAYOUT_TABLE: dict[tuple[Move, Move], int] = {
    (Move.COOPERATE, Move.COOPERATE): 3,
    (Move.DEFECT, Move.COOPERATE): 5,
    (Move.COOPERATE, Move.DEFECT): 0,
    (Move.DEFECT, Move.DEFECT): 1,
}


@dataclass
class RoundResult:
    player1_move: Move
    player2_move: Move
    player1_payout: int
    player2_payout: int
    player1_total: int
    player2_total: int


class Prisoner(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def get_name() -> str:
        ...

    @abc.abstractmethod
    def play(self) -> Move:
        ...

    @abc.abstractmethod
    def result(self, your_move: Move, their_move: Move, payout: int, their_payout: int) -> None:
        ...

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


class  Defector(Prisoner):
    @classmethod
    def get_name(self) -> str:
        return "Defector"
    
    def play(self) -> Move:
        return Move.DEFECT
        
    def result(self, your_move: Move, their_move: Move, payout: int, their_payout: int) -> None:
        ...