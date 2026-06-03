import sqlite3

# Create database

conn = sqlite3.connect(
    "../bluestock_mf.db"
)

cursor = conn.cursor()

# Read schema

with open(
    "../sql/schema.sql",
    "r"
) as file:

    schema = file.read()

# Execute all CREATE TABLE statements

cursor.executescript(schema)

conn.commit()

conn.close()

print("Database created successfully!")