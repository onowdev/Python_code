import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number between 1 and 100 \n"))
    
    if guess == secret_number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < secret_number:
        print("Too Low! Try again.")
    else:
        print("Too high! try again.")
        