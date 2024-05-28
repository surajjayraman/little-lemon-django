import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('my_database.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# Fetch and print data
c.execute('SELECT * FROM stocks')
print(c.fetchall())

# Close the connection
conn.close()