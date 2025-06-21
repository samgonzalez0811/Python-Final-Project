import sqlite3

def main():
    conn = sqlite3.connect("Employees.db")
    cur = conn.cursor()
    
    cur.execute('''Delete from Employees where empid = 3''')
    
    conn.commit()
    conn.close()

main()
