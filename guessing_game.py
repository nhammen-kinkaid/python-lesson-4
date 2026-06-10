import random

play_again = True

while play_again:
    secret_number = random.randrange(1,3)
    player_guess = 0

    # player_guess=int(input("Guess the secret number: "))

    while player_guess != secret_number:
        player_guess=int(input("Guess the secret number: "))
        if player_guess > secret_number:
            print("That was too high!")
        if player_guess < secret_number:
            print("That was too low!")

    if player_guess == secret_number:
        print("You were right!")

    response = input("Do you want to play again? ")
    if response == "yes":
        play_again = True
    else:
        play_again = False
