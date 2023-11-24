import random

def roll():
    roll1 = random.randrange(1, 30)
    roll2 = random.randrange(1, 30)
    roll3 = random.randrange(1, 30)
    roll4 = random.randrange(1, 30)
    roll5 = random.randrange(1, 30)

    # Uncomment the line below if you want to display the lotto numbers.
    print(f"\nLotto #'s: {roll1},{roll2},{roll3},{roll4},{roll5}")
    
    print("\nOdds of winning are 0.00000000412%")
    print("\nGuess 5 numbers between 1-30")
    final_roll = [roll1, roll2, roll3, roll4, roll5]
    guess = input("Type in 5 different numbers (separated by commas): ")

    # Convert the user's guess to a list of integers
    user_numbers = [int(num) for num in guess.split(',')]

    # Check if any of the guessed numbers match the lotto numbers
    correct_numbers = set(user_numbers) & set(final_roll)
    
    if set(user_numbers) == set(final_roll):
        print("\nYOU WON THE LOTTERY")
        print(f"\nThe Lotto #'s are: {roll1},{roll2},{roll3},{roll4},{roll5}")
        
        total_possible_combinations = 30 ** 5
        odds = 1 / total_possible_combinations
        print(f"Odds of guessing all 5 numbers correctly: {odds:.10%}")

    elif len(correct_numbers) == 5:
        print("\nYOU WON THE LOTTERY (all numbers correct, even in the incorrect order)")
        print(f"\nThe Lotto #'s are: {roll1},{roll2},{roll3},{roll4},{roll5}")
    else:
        print("You did not win, try again")
        print(f"\nThe Lotto #'s were: {roll1},{roll2},{roll3},{roll4},{roll5}")
        roll()

roll()
