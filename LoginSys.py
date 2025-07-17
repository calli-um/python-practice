print('LOGIN SYSTEM')
username="Sahiba"
password="python123"

while True:
    print('Enter username:')
    name=input()
    name=str(name)
    print('Enter password:')
    pswrd=input()
    pswrd=str(pswrd)

    if name==username and pswrd==password:
        print('Successfully Logged in!')
        break
    else:
        print('Wrong username or password.')
        print('Would you like to try again? (y/n)')
        ans=input().lower()
        if ans=='n':
            break
        elif ans!='y':
            print("invalid choice")
            break
        else:
            print('sure!')

print('Program exited.')
       