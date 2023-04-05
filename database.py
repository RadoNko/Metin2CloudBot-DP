import sqlite3

# create a connection to the database
conn = sqlite3.connect('polling_requests.db')

# create a table to store the polling requests
conn.execute('''
CREATE TABLE IF NOT EXISTS requests (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   state TEXT NOT NULL,
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
''')

# commit the changes
conn.commit()

# close the connection
conn.close()
