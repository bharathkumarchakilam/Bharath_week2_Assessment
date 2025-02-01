#class for managing the bank operations
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    
    #function for depost the money
    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
            
    #function for withdraw the money
    def withdraw(self,amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawn: ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds. Withdrawal denied.")
        else:
            print("Withdrawal amount must be positive.")
    
    #function for getting the balance
    def get_balance(self):
        return self.balance

#main function
def main():
    
    initial_balance=float(input("Enter initial balance: "))
    account=BankAccount(initial_balance)

    while True:
        action=input("Enter 'd' to deposit, 'w' to withdraw, 'q' to quit: ")
        if action == 'd':
            amount=float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif action == 'w':
            amount=float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif action == 'q':
            print("Exiting. Final balance:", account.get_balance())
            break
        else:
            print("Invalid input. Please try again.")

#run the program            
main()
