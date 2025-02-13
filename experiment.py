import typing

import argparse
from participant import (
    CoinFlipper,
    Defector,
    Prisoner,
    PAYOUT_TABLE,
    RoundResult
)

from coinflipper import CoinFlipper
from defector import Defector
from jacob1 import Jacob1
from jacob5 import Jacob
from memory import Memory
from mustafa1 import Mustafa1

players_list = [
   CoinFlipper,
   Defector,
   Jacob1,
   Jacob,
   Mustafa1,
   Memory
]

players = { p.get_name(): p for p in players_list }


def run_game(p1: Prisoner, p2: Prisoner, num_games: int) -> typing.Iterable[RoundResult]:
    player1_total = 0
    player2_total = 0
    for _ in range(num_games):
        play1 = p1.play()
        play2 = p2.play()

        payout1 = PAYOUT_TABLE[(play1, play2)]
        payout2 = PAYOUT_TABLE[(play2, play1)]

        player1_total += payout1
        player2_total += payout2

        p1.result(play1, play2, payout1, payout2)
        p2.result(play2, play1, payout2, payout1)

        yield RoundResult(
            player1_move=play1,
            player2_move=play2,
            player1_payout=payout1,
            player2_payout=payout2,
            player1_total=player1_total,
            player2_total=player2_total
        )

def positive_int(value: str) -> int:
    try:
        value = int(value)
        if value <= 0:
            raise argparse.ArgumentTypeError("{} is not a positive integer".format(value))
    except ValueError:
        raise Exception("{} is not an integer".format(value))
    return value

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('player1', choices=players.keys())
    parser.add_argument('player2', choices=players.keys())
    parser.add_argument('num_games', type=positive_int)
    parser.add_argument('--only-results')

    args = parser.parse_args()

    player1 = players[args.player1]()
    player2 = players[args.player2]()
    
    name1 = players[args.player1].get_name()
    name2 = players[args.player2].get_name()
    
    print(f"{player1.get_name()} vs {player2.get_name()}")
    results = []
    for i, round in enumerate(run_game(player1, player2, args.num_games)):
        round: RoundResult
        print(f"Round: {i}")
        print(f"{name1}: {round.player1_move}")
        print(f"{name2}: {round.player2_move}")
        print(f"Points: {name1}: {round.player1_payout}, {name2}: {round.player2_payout})")
        print(f"Total: {name1}: {round.player1_total}, {name2}: {round.player2_total})")

        results.append(round)

    result = ""
    if results[-1].player1_total == results[-1].player2_total:
        result = "Tie"
    elif results[-1].player1_total > results[-1].player2_total:
        result = f"{name1} wins"
    else:
        result = f"{name2} wins"

    print(f"Result: {result}")
