#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simulating a dice betting game.

for each time the dice rolled, there's a score added or subtracted
depending on the number that pops out.

Rules:
1. if the number is 1 or 2, then score is subtracted by 1
2. if the number is 3, 4 or 5, then score is added by 1
3. if the number is 6, then roll the dice again and add the number that pops
   to score.
4. there's F percent chance of score falling, that is it returns to 0 (0.1 here)
5. throw the dice for X times throws (100 in this case);
   and bet whether the score is higher or not than Y (60 in this case)
"""

import matplotlib.pyplot as plt
import numpy as np

from module import apply_rules, check_falling, constants, roll_dice

np.random.seed(123)

def play_games(throws, prob_of_falling):
    score = 0

    for _ in range(throws):
        dice = roll_dice()
        score = apply_rules(score, dice, prob_of_falling)

    return score


if __name__ == '__main__':
    # load constants
    K, THROWS, PROB_OF_FALLING, BETTING_SCORES = constants()

    # record for betting @BETTING_SCORES
    data = {
        ">=": 0,
        "<": 0,
    }

    for _ in range(K):
        r = play_games(THROWS, PROB_OF_FALLING)
        
        if r >= BETTING_SCORES:
            data['>='] += 1
        else:
            data['<'] += 1

    print(data)
    plt.bar(data.keys(), data.values(), width=0.3)
    plt.show()
