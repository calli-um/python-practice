print('Even Odd Checker')
choice = 'y'

while choice == 'y':
    print('Enter a number:')
    num = input()
    try:
        num = int(num)
        if num % 2 == 0:
            print(f'{num} is an even number.')
        else:
            print(f'{num} is an odd number.')
    except:
        print('Input must be a valid number.')
    else:
        print('Do you want to check another number? y/n')
        ans = input()
        ans = ans.lower()
        if ans == 'n':
            print('Number checked successfully.')
            choice = 'n'
        elif ans == 'y':
            choice = 'y'
    finally:
        print('Thank you!')
