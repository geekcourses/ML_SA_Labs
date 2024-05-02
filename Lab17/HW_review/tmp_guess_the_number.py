import random

# guess the number
# Write a simple Python program, implementing the "Guess the number" game - a simple interactive game where a player attempts to guess a computer-generated random number within a given range.
# Here's how it works:
# Initialization: The computer chooses a random number in given range, typically between 1 and 100.
# Gameplay: The player is prompted to make a guess about what the number might be, and the computer provides feedback if each guess is:
# Too high: The guessed number is greater than the target number.
# Too low: The guessed number is less than the target number.
# Correct: The guessed number matches the target number precisely.
# End Game: The game continues until the player guesses the number correctly. At this point, the game provides a congratulatory message and reveals the total number of attempts the player made to guess the number correctly.


START=1
END=10

def initialization():
    machine_number = random.randint(START, END)
    return machine_number

def game_play():
    # game intro
    print(f'Guess my number (from {START} to {END})')
    # game move
    user_number = int( input('Enter a number: '))

    if user_number<machine_number:
        print('Too low')
    elif user_number>machine_number:
        print('Too high')
    elif user_number==machine_number:
        print('Correct')
        exit()
    else:
        print('Ups, something else happens')

if __name__=='__main__':
    machine_number = initialization()
    print(machine_number)

    game_play()




