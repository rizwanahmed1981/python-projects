import random

def guess_number(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), correct (C):  ")
        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess + 1

    print(f"wow computer guessed the right number, {guess}")



guess_number(10)