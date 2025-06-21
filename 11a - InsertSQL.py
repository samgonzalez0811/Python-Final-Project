import sqlite3

def main():
    conn = sqlite3.connect("Employees.db")
    cur = conn.cursor()
    
    cur.execute('''INSERT INTO Employees (EmpID,FirstName,LastName,Address,City,State,Zip)
                        values (1, "Bill","Smith","123 main st","fullerton","CA","92833")''')
    cur.execute('''INSERT INTO Employees (EmpID,FirstName,LastName,Address,City,State,Zip)
                        values (2, "Wendy","Addams","321 First st","Anaheim","CA","92804")''')
    cur.execute('''INSERT INTO Employees (EmpID,FirstName,LastName,Address,City,State,Zip)
                        values (3, "Jim","Jones","887 main st","Garden Grove","CA","92666")''')
    conn.commit()
    conn.close()

main()