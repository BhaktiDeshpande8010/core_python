import sqlite3 as sq

con = sq.connect("jobportal.db")   # creates DB file
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS employee(
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    profile TEXT,
    status TEXT,
    application TEXT
)
""")