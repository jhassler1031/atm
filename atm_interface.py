#Connect to the DB
#Create functions to interact with DB
#Create UI

import records

db = records.Database("postgres://localhost/atm_db")

# Interaction functions ==============================

def deposit(db, amount):
    pass

def withdrawel(db, amount):
    pass

def show_all(db):
    pass


# UI functions ========================================

def menu():
    print("1) Check Balance")
    print("2) Make a Deposit")
    print("3) Make a Withdrawl")
    print("4) Show All Transactions")
    print("Press <enter> to Exit")
    choice = input("> ")
    return choice

def ui_deposit(db, balance):
    print("How much would you like to deposit?")
    amount = input("> ")
    amount = int(amount)
    print(f"You have deposited ${amount} into your account.")
    #interact with DB

def ui_withdrawel(db, balance):
    while True:
        print("How much would you like to withdrawl? ")
        amount = input("> ")
        amount = int(amount)

        if amount < balance:
            print(f"You have withdrawn ${amount}.")
            #interact with db
            break
        else:
            print("Insufficient Funds")


def get_balance(db, balance):
    print(f"Your Balance is: {balance}")

def ui_show_transactions(db, balance):
    print("Showing All Transactions")
    #interact with DB

def ui_exit(db, balance):
    print("Goodbye")
    exit()

menu_options = {
"1": get_balance,
"2": ui_deposit,
"3": ui_withdrawel,
"4": ui_show_transactions,
"": ui_exit
}

# Main Program ========================================

balance = 1000

print("----------ATM----------")

while True:
    my_choice = menu()

    menu_options[my_choice](db, balance)
