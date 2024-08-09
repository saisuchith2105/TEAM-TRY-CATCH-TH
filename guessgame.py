import random
 
def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Guess the number between 1 and 100.")
    while (user_guess := int(input("Your guess: "))) != number_to_guess:
        print("Higher!" if user_guess < number_to_guess else "Lower!")
        attempts += 1
    print(f"Correct! You guessed it in {attempts + 1} attempts.")
 
 
guessing_game()
