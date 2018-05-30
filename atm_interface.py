#Connect to the DB
#Create functions to interact with DB
#Create UI

import records

db = records.Database("postgres://localhost/atm_db")

# Interaction functions ==============================

def deposit(db, amount):
    sql = "INSERT INTO transactions (amount, type) VALUES (:amount, :type);"
    db.query(sql, amount=amount, type="Deposit")

def withdrawel(db, amount):
    sql = sql = "INSERT INTO transactions (amount, type) VALUES (:amount, :type);"
    db.query(sql, amount=amount, type="Withdrawel")

def show_all(db):
    sql = "SELECT * FROM transactions;"
    return db.query(sql)

def display_transaction(db, action):
    print(f"Transaction ID: {action.id} Amount: ${action.amount} Type: {action.type}")


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
    deposit(db, amount)
    balance += amount
    print(f"You have deposited ${amount} into your account.")
    return balance

def ui_withdrawel(db, balance):
    while True:
        print("How much would you like to withdraw? ")
        amount = input("> ")
        amount = int(amount)

        if amount < balance:
            withdrawel(db, amount)
            balance -= amount
            print(f"You have withdrawn ${amount}.")
            break
        else:
            print("Insufficient Funds")
    return balance

def get_balance(db, balance):
    print(f"Your Balance is: {balance}")
    return balance

def ui_show_transactions(db, balance):
    print("Showing All Transactions")
    transactions = show_all(db)
    for action in transactions:
        display_transaction(db, action)
    return balance 

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

    balance = menu_options[my_choice](db, balance)
