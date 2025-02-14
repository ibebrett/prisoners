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
python3 tournament.py 10000

Scores in order
---------------
Jacob5: 162430
Jacob1: 122508
Amilcar1: 120238
Zack: 118012
Memory: 116060
CoinFlipper: 110512
mustafa1: 98472
Defector: 98012
Matches
-------
Amilcar1 vs CoinFlipper: 20276 to 27876
Amilcar1 vs Defector: 7986 to 18056
Amilcar1 vs Jacob1: 30000 to 30000
Amilcar1 vs Jacob5: 30000 to 30000
Amilcar1 vs mustafa1: 16069 to 23429
Amilcar1 vs Memory: 7877 to 18492
Amilcar1 vs Zack: 8030 to 17880
CoinFlipper vs Defector: 5015 to 29940
CoinFlipper vs Jacob1: 22514 to 22509
CoinFlipper vs Jacob5: 22806 to 22441
CoinFlipper vs mustafa1: 16713 to 25028
CoinFlipper vs Memory: 10610 to 27560
CoinFlipper vs Zack: 4978 to 30123
Defector vs Jacob1: 10004 to 9999
Defector vs Jacob5: 10012 to 9997
Defector vs mustafa1: 10000 to 10000
Defector vs Memory: 10000 to 10000
Defector vs Zack: 10000 to 10000
Jacob1 vs Jacob5: 30000 to 30000
Jacob1 vs mustafa1: 9999 to 10004
Jacob1 vs Memory: 9999 to 10004
Jacob1 vs Zack: 10002 to 10007
Jacob5 vs mustafa1: 10001 to 10011
Jacob5 vs Memory: 29994 to 30004
Jacob5 vs Zack: 29997 to 30002
mustafa1 vs Memory: 10000 to 10000
mustafa1 vs Zack: 10000 to 10000
Memory vs Zack: 10000 to 10000

```
