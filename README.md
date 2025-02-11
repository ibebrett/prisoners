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