'''Features to include:
- Check current balance
- Withdraw money (only if enough balance)
- Deposit money
- Exit the program
- Use one list or variable to track the balance
- Write separate functions for each operation
'''
print("SIMPLE BANKING SYSTEM")

balance = 0  

def checkBalance():
    print(f"Your current balance is: {balance} PKR")

def depositMoney():
    global balance
    print("Enter amount to deposit:")
    amount = int(input())
    if amount > 0:
        balance += amount
        print(f"{amount} PKR deposited successfully.")
    else:
        print("Invalid amount. Deposit must be positive.")

def withdrawMoney():
    global balance
    print("Enter amount to withdraw:")
    amount = int(input())
    if amount > balance:
        print("Insufficient balance.")
    elif amount <= 0:
        print("Invalid amount. Withdrawal must be positive or non-zero.")
    else:
        balance -= amount
        print(f"{amount} PKR withdrawn successfully.")

def MainMenu():
    while True:
        print("\nFeatures:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("Enter your choice: (1-4)")
        choice = input()

        if choice == '1':
            checkBalance()
        elif choice == '2':
            depositMoney()
        elif choice == '3':
            withdrawMoney()
        elif choice == '4':
            print("Thank you for using our banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

MainMenu()
