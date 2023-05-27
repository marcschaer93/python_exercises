target = 25
guess = None


while guess != target:
    guess = input('Enter...')
    if guess == "q":
        break
    guess = int(guess)

print('Game Over')

    