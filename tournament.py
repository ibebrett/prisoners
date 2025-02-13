import argparse
from itertools import combinations
from collections import defaultdict
from experiment import players, run_game, positive_int

def tournament(num_games: int):
    scores = defaultdict(int)
    counts = {}

    for (p1_name, p2_name) in combinations(players.keys(), 2):
        p1 = players[p1_name]()
        p2 = players[p2_name]()

        results = list(run_game(p1, p2, num_games))

        counts[(p1_name, p2_name)] = (results[-1].player1_total, results[-1].player2_total)

        scores[p1_name] += results[-1].player1_total
        scores[p2_name] += results[-1].player2_total

    return scores, counts

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('num_games', type=positive_int)

    args = parser.parse_args()

    scores, counts = tournament(args.num_games)

    sorted_scores = reversed(sorted(scores.items(), key=lambda x: x[1]))

    print("Scores in order")
    print("---------------")
    for name, score in sorted_scores:
        print(f"{name}: {score}")

    print("Matches")
    print("-------")

    for (p1_name, p2_name), (p1_score, p2_score) in counts.items():
        print(f"{p1_name} vs {p2_name}: {p1_score} to {p2_score}")

