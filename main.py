import random

#You will get 5 chances to guess the secret number between 1 - 10

secret_number = random.randint(1, 9)
guess_count = 0
guess_limit = 5

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1

    if guess == secret_number:
        print('You won! YO!!!! 👍')
        break
else:
    print('You lose XD 🤣')
    print("The number was")
    print(secret_number)