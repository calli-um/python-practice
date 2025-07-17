import random  # to generate random numbers

print('Number Guessing Game')
generated_number = random.randint(1, 100)
attempts_limit = 3

for attempt in range(1, attempts_limit + 1):
    print(f'Attempt {attempt} of {attempts_limit}')
    print('Guess a number from 1 to 100:')
    
    guessed_number = input()

    try:
        guessed_number = int(guessed_number)
        
        if guessed_number < generated_number:
            print('Oops, try with a greater number.')
        elif guessed_number > generated_number:
            print('Oops, try with a smaller number.')
        else:
            print(f'Yohoo! You guessed the number in {attempt} attempt(s)!')
            break
    except ValueError:
        print('Invalid input. Please enter a number.')
else:
    print(f'Oops! You are out of attempts. The number was {generated_number}.')

print('Game exited. Thank you for playing buds!')
