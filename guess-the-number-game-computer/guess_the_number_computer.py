import random
def guess(x):
    random_number = random.randint(1, x)
    count = 0
    guess = 0
    while guess != random_number:
        guess = int(input('guess a number between 1 and {x}:'))
        if guess< random_number:
            count += 1
            print(f"{guess} sorry! the number you guessed is lower then the number, guess again:")
            print("========================================")
        elif guess > random_number:
            count += 1
            print(f"{guess} sorry! the number you guessed is higher then the number, guess again:")
            print("========================================")
        
    print(f"congrats ! you guessed the right number {random_number}")
    count += 1
    print("========================================")
    print(f"It Took {count} attempts to you to guess the right number {random_number}")
guess(10)