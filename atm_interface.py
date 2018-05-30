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
    print("Press <enter> to Exit")
    choice = input("> ")
    return choice

def ui_deposit(db):
    pass

def ui_withdrawel(db):
    pass

def get_balance(db):
    pass

def ui_show_transactions(db):
    pass

def ui_exit(db):
    print("Goodbye")
    exit()

menu_options = {
"1": get_balance,
"2": ui_deposit,
"3": ui_withdrawel,
"": ui_exit
}

# Main Program ========================================

print("----------ATM----------")

while True:
    my_choice = menu()

    menu_options[my_choice](db)
