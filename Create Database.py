import sqlite3

def main():
    conn = sqlite3.connect("Employees.db")
    cur = conn.cursor()
    
    cur.execute('''CREATE TABLE Employees (EMPID INTEGER PRIMARY KEY NOT NULL,
                                FirstName TEXT,
                                LastName TEXT,
                                Address TEXT,
                                City TEXT,
                                State TEXT,
                                ZIP TEXT,
                                Phone TEXT,
                                Rate TEXT,
                                Hours TEXT)''')
    conn.commit()
    conn.close()

main()