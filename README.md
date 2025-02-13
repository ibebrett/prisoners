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
Jacob5: 102479
CoinFlipper: 90384
Jacob1: 82298
Memory: 81824
Defector: 69988
mustafa1: 64983
Matches
-------
CoinFlipper vs Defector: 5007 to 29972
CoinFlipper vs Jacob1: 22301 to 22301
CoinFlipper vs Jacob5: 22337 to 22487
CoinFlipper vs mustafa1: 16773 to 24968
CoinFlipper vs Memory: 23966 to 21816
Defector vs Jacob1: 10004 to 9999
Defector vs Jacob5: 10012 to 9997
Defector vs mustafa1: 10000 to 10000
Defector vs Memory: 10000 to 10000
Jacob1 vs Jacob5: 30000 to 30000
Jacob1 vs mustafa1: 9999 to 10004
Jacob1 vs Memory: 9999 to 10004
Jacob5 vs mustafa1: 10001 to 10011
Jacob5 vs Memory: 29994 to 30004
mustafa1 vs Memory: 10000 to 10000
```
