import random



def roll():
	roll1 = random.randrange(1, 30)
	roll2 = random.randrange(1, 30)
	roll3 = random.randrange(1, 30)
	roll4 = random.randrange(1, 30)
	roll5 = random.randrange(1, 30)






	print(f"\nLotto #'s: {roll1},{roll2},{roll3},{roll4},{roll5}")
	print("\nOdds of winning are 0.00000000412%")
	print("\nGuess 5 numbers between 1-30")
	final_roll = (f"{roll1},{roll2},{roll3},{roll4},{roll5}")
	guess = input("Type in 5 different numbers (seperated by commas): ")

	if guess == final_roll:
		print("\nYOU WON THE LOTTERY")

	else:
		print("You dont not win, the numbers were")
		print(f"{roll1},{roll2},{roll3},{roll4},{roll5}")




roll()
	



	
