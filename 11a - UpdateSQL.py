import sqlite3

def main():
    conn = sqlite3.connect("Employees.db")
    cur = conn.cursor()
    
    cur.execute('''Update Employees set Address="9988 2nd st",City="Buena Park" where EmpID = 2''')
    conn.commit()
    conn.close()

main()