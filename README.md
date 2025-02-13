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
``
Scores in order
---------------
Jacob5: 13250
CoinFlipper: 12842
Jacob1: 11249
Amilcar1: 11094
Memory: 9623
Defector: 8784
mustafa1: 8712
Matches
-------
Amilcar1 vs CoinFlipper: 1988 to 2773
Amilcar1 vs Defector: 815 to 1740
Amilcar1 vs Jacob1: 3000 to 3000
Amilcar1 vs Jacob5: 3000 to 3000
Amilcar1 vs mustafa1: 1496 to 2226
Amilcar1 vs Memory: 795 to 1820
CoinFlipper vs Defector: 493 to 3028
CoinFlipper vs Jacob1: 2252 to 2252
CoinFlipper vs Jacob5: 2313 to 2258
CoinFlipper vs mustafa1: 1621 to 2471
CoinFlipper vs Memory: 3390 to 1795
Defector vs Jacob1: 1004 to 999
Defector vs Jacob5: 1012 to 997
Defector vs mustafa1: 1000 to 1000
Defector vs Memory: 1000 to 1000
Jacob1 vs Jacob5: 3000 to 3000
Jacob1 vs mustafa1: 999 to 1004
Jacob1 vs Memory: 999 to 1004
Jacob5 vs mustafa1: 1001 to 1011
Jacob5 vs Memory: 2994 to 3004
mustafa1 vs Memory: 1000 to 1000
```