import sqlite3

def main():
    conn = sqlite3.connect("Employees.db")
    cur = conn.cursor()
    
    cur.execute('''Select * From Employees''')
    
    row = cur.fetchone()
    
    while row != None:
        print(row)
        row = cur.fetchone()
        
    conn.close()

main()
