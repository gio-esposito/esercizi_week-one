import random

print("Welcome to the Number Guess Game")
print("I am thinking of a number between 1 and 100")

secret_value = random.randint(1, 100)
difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ")
guessed = False

def compare():
    global secret_value
    global guessed
    guess_value = int(input("Make a guess: "))
    if guess_value == secret_value:
        print("You won")
        guessed = True
    elif guess_value < secret_value:
        print("To low.")
    elif guess_value > secret_value:
        print("To high.")

if difficulty == 'easy':
    i = 0
    contatore = 10
    while i in range(10) and guessed == False:
        compare()
        contatore -= 1
        i += 1
        if contatore > 0 and guessed == False:
            print(f"You have {contatore} tentatives left")
        elif contatore == 0 and guessed == False:
            print("You lose")
elif difficulty == 'hard':
    j = 0
    contatore = 3
    while j in range(3) and guessed == False:
        compare()
        contatore -= 1
        j += 1
        if contatore > 0 and guessed == False:
            print(f"You have {contatore} tentatives left")
        elif contatore == 0 and guessed == False:
            print("You lose")
