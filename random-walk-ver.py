#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simulating a random walk of the dice game.

see dice-game-simulation for more info
"""

import matplotlib.pyplot as plt
import numpy as np

from module import apply_rules, constants, falling, roll_dice

np.random.seed(123)

def random_walk(throws, prob_of_falling):
    random_walk = [0]

    for _ in range(throws):
        score = random_walk[-1]
        
        dice = roll_dice()
        score = apply_rules(score, dice, prob_of_falling)

        random_walk.append(score)

    return random_walk


if __name__ == '__main__':
    # load constants
    _, THROWS, PROB_OF_FALLING, BETTING_SCORES = constants()

    r = random_walk(THROWS, PROB_OF_FALLING)
        
    plt.plot(r)
    plt.show()
