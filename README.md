# Iterated Prisoners Dilemma

[Wiki Article](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma)

## Implementation

See [defector.py](defectory.py) and [coinflipper.py](coinflipper.py) for example implementations.

The goal is to make a new implementation of your own!

Your job is to implement a few methods on a subclass of prisoner.

1. play(...). This is called once per round to generate your move: Defect or Cooperate.

2. result() This is called after you make your move with the results from the round. You can store information from your round to help you determine if you should defect or cooperate later.

The way it works is that your bot will be paired against another bot and will repeatedly play moves. The results of each round will be fed back into your bot with result. You can learn from history but you have to keep track of this
yourself.

When done, add your player to the ones in experiment.py!

## Running an individual game

This command will run a set of games between Defector and CoinFlipper.
Change the names to your bot! Make sure you edit experiments.py and add your player.

```python experiment.py Defector CoinFlipper 100```

## Tournament

Once we have enough players, we will run a tournament where every player plays
every other player. The players with the most points at the end win!

To run a tournament just run

```python tournament 10000```

A sample of current standings:

```
python3 tournament.py 30

Scores in order
---------------
Jacob5: 608
Zack: 509
CoinFlipper: 504
Memory: 500
mustafa1: 494
Jacob1: 490
Defector: 490
Amilcar1: 482
DerekJOne: 468
AIBot: 466
Matches
-------
AIBot vs Amilcar1: 83 to 53
AIBot vs CoinFlipper: 76 to 71
AIBot vs DerekJOne: 66 to 76
AIBot vs Defector: 15 to 90
AIBot vs Jacob1: 52 to 52
AIBot vs Jacob5: 64 to 49
AIBot vs mustafa1: 49 to 74
AIBot vs Memory: 38 to 68
AIBot vs Zack: 23 to 73
Amilcar1 vs CoinFlipper: 68 to 93
Amilcar1 vs DerekJOne: 69 to 64
Amilcar1 vs Defector: 25 to 50
Amilcar1 vs Jacob1: 89 to 89
Amilcar1 vs Jacob5: 92 to 87
Amilcar1 vs mustafa1: 35 to 60
Amilcar1 vs Memory: 26 to 46
Amilcar1 vs Zack: 25 to 50
CoinFlipper vs DerekJOne: 68 to 68
CoinFlipper vs Defector: 14 to 94
CoinFlipper vs Jacob1: 65 to 65
CoinFlipper vs Jacob5: 57 to 67
CoinFlipper vs mustafa1: 56 to 81
CoinFlipper vs Memory: 58 to 78
CoinFlipper vs Zack: 22 to 77
DerekJOne vs Defector: 15 to 90
DerekJOne vs Jacob1: 75 to 75
DerekJOne vs Jacob5: 81 to 71
DerekJOne vs mustafa1: 59 to 79
DerekJOne vs Memory: 15 to 90
DerekJOne vs Zack: 15 to 90
Defector vs Jacob1: 34 to 29
Defector vs Jacob5: 42 to 27
Defector vs mustafa1: 30 to 30
Defector vs Memory: 30 to 30
Defector vs Zack: 30 to 30
Jacob1 vs Jacob5: 90 to 90
Jacob1 vs mustafa1: 29 to 34
Jacob1 vs Memory: 29 to 34
Jacob1 vs Zack: 32 to 37
Jacob5 vs mustafa1: 46 to 76
Jacob5 vs Memory: 84 to 94
Jacob5 vs Zack: 87 to 92
mustafa1 vs Memory: 30 to 30
mustafa1 vs Zack: 30 to 30
Memory vs Zack: 30 to 30
```


### OpenAI Bot

The AIBot will not use OpenAI unless you have the python ```openai``` package installed and your environment variable ```OPENAI_API_KEY``` set. If the openai package is not available, it will fall back to being a cooperator.
