#Connect seed file to the DB
#Drop any tables if they exist
#Create a transactions table
#Add any initial info needed

import records

db = records.Database("postgres://localhost/atm_db")

db.query("DROP TABLE IF EXISTS transactions;")

create_query = """
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    amount NUMERIC (5),
    type VARCHAR (20)
);
"""

db.query(create_query)

insert_query = "INSERT INTO transactions (amount, type) VALUES (0, 'None');"
db.query(insert_query)
