import numpy as np


# CONSTANTS
def constants():
    return (
        100,  # K, simulate K times
        100,  # THROWS
        0.1,  # PROB_OF_FALLING
        60,  # BETTING_SCORES
    )


def roll_dice():
    return np.random.randint(1, 7)


def falling(probability_of_falling):
    if (np.random.rand() * 100) < probability_of_falling:
        return True

    return False

def check_falling(score, prob_of_falling):
    is_falling = falling(prob_of_falling)

    if is_falling:
        score = 0
        is_falling = False
    
    return score

def apply_rules(score, dice, prob_of_falling):
    if dice <= 2:
        score = max(0, score - 1)
    elif dice <= 5:
        score += 1
    else:
        rollagain = roll_dice()
        score += rollagain

    score = check_falling(score, prob_of_falling)

    return score
