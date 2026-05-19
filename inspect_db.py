import sqlite3

conn = sqlite3.connect("database/intake.db")

cursor = conn.cursor()

cursor.execute("PRAGMA table_info(audit_logs)")

columns = cursor.fetchall()

for column in columns:
    print(column)