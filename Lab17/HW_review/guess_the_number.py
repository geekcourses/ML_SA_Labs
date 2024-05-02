import random

def generate_random_number(min, max):
    """Generates a random number between min and max.

    Args:
        min (int): The minimum value of the random number.
        max (int): The maximum value of the random number.

    Returns:
        int: A randomly generated number within the specified range.
    """
    return random.randint(min, max)

def user_input(min,max):
    """Prompts the user to guess a number.

    Returns:
        int: The number guessed by the user.
    """

    while True:
        user_num = int(input(f'Enter your guess [{min}-{max}]: '))
        if min<user_num<max:
            break

    return user_num

def check_guess(guess, answer):
    """Checks if the user's guess matches the generated number.

    Args:
        guess (int): The user's guessed number.
        answer (int): The correct number.

    Returns:
        bool: True if the guess is correct, False otherwise.
        str: A message indicating whether the guess was too high, too low, or correct.
    """
    if guess == answer:
        return True,"Just right! Congratulations!"
    elif guess < answer:
        return False, "Too low!"
    else :
        return False,"Too high!"

def play_game(min_number, max_number):
    """Controls the flow of the game, utilizing other functions."""

    print(f"Guess the number between {min_number} and {max_number}.")
    answer = generate_random_number(min_number,max_number)
    print(f'#### answer={answer}')
    # print('#### answer={}'.format(answer))

    tries = 0
    while True:
        guess = user_input(min_number,max_number)
        guess_status,guess_msg  = check_guess(guess, answer) # status=False, msg = "Too low!"
        print(guess_msg)
        tries+=1

        if guess_status==True:
            print(f'You guessed the number in {tries} tries.')
            break






# main program
if __name__ == "__main__":
    play_game(min_number=1, max_number=100)


# EXPECTED OUTPUT:
# Guess the number between 1 and 100.
# Enter your guess: 50
# Too high!
# Enter your guess: 25
# Too low!
# Enter your guess: 37
# Too high!
# Enter your guess: 31
# Too high!
# Enter your guess: 28
# Just right! Congratulations!
# You guessed the number in 5 tries.