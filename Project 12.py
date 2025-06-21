#Samuel Gonzalez
#Project 12

#Importing the tkinter library
import tkinter as tk
import sqlite3

EmployeeData = []
RecordNumber = 0

def close():
    root.destroy()

def clear_text():
    try:
        idEntry.delete(0, "end")
        nameEntry1.delete(0, "end")
        nameEntry2.delete(0, "end")
        addyEntry.delete(0, "end")
        cityEntry.delete(0, "end")
        stateEntry.delete(0, "end")
        zipEntry.delete(0, "end")
        phoneEntry.delete(0,"end")
        rateEntry.delete(0, "end")
        hoursEntry.delete(0, "end")
        idEntry.focus_set()
    except:
        pass
    
def save():
    SQL = buildInsertSQL()
    print(SQL)
    executeSQL(SQL)
    loadData()

def loadData():
    global RecordNumber
    RecordNumber = 0
    readDatabase()
    displayDataForm()

def buildInsertSQL():
    SQL = "INSERT INTO Employees (EmpID,FirstName,LastName,Address,City,State,Zip,Phone,Rate,Hours) Values ('" + idEntry.get() + "','" + nameEntry1.get() + "','" + nameEntry2.get() + "','" + addyEntry.get() + "','" + cityEntry.get() + "','" + stateEntry.get() + "','" + zipEntry.get() + "','" + phoneEntry.get() + "','" + rateEntry.get() + "','" + hoursEntry.get() + "')"
    return SQL

def executeSQL(SQL):
    conn = sqlite3.connect("Employees.db")
    cur = conn.cursor()
    
    cur.execute(SQL)
    
    conn.commit()
    conn.close()

def readDatabase():
    global EmployeeData
    EmployeeData = []
    conn = sqlite3.connect("Employees.db")
    cur = conn.cursor()
    
    cur.execute('''Select * From Employees''')
    
    row = cur.fetchone()
    
    while row != None:
        TempList = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]]
        EmployeeData.append(TempList)
        row = cur.fetchone()
        
    conn.close()

def displayDataForm():
    try:
        clear_text()
        idEntry.insert(0,EmployeeData[RecordNumber][0])
        nameEntry1.insert(0,EmployeeData[RecordNumber][1])
        nameEntry2.insert(0,EmployeeData[RecordNumber][2])
        addyEntry.insert(0, EmployeeData[RecordNumber][3])
        cityEntry.insert(0, EmployeeData[RecordNumber][4])
        stateEntry.insert(0,EmployeeData[RecordNumber][5])
        zipEntry.insert(0, EmployeeData[RecordNumber][6])
        phoneEntry.insert(0,EmployeeData[RecordNumber][7])
        rateEntry.insert(0, EmployeeData[RecordNumber][8])
        hoursEntry.insert(0,EmployeeData[RecordNumber][9])
    except:
        pass
    
def moveFirst():
    try:
        global RecordNumber
        RecordNumber = 0
        displayDataForm()
    except:
        pass

def moveLast():
    try:
        global RecordNumber
        RecordNumber = len(EmployeeData) - 1
        displayDataForm()
    except:
        pass

def moveNext():
    try:
        global RecordNumber
        RecordNumber += 1
        if RecordNumber > len(EmployeeData) - 1:
            RecordNumber = len(EmployeeData) - 1
        displayDataForm()
    except:
        pass

def movePrevious():
    try:
        global RecordNumber
        RecordNumber -= 1
        if RecordNumber < 0:
            RecordNumber = 0
        displayDataForm()
    except:
        pass

#Creating a GUI window
root = tk.Tk()
root.configure(background="light grey")
root.title("New Employee Entry")
root.geometry("600x600")

#Creating the labels for each text box
idLabel = tk.Label(root, text="Employee ID", bg="light grey")
nameLabel1 = tk.Label(root, text="First Name", bg="light grey")
nameLabel2 = tk.Label(root, text="Last Name", bg="light grey")
addyLabel = tk.Label(root, text="Address", bg="light grey")
cityLabel = tk.Label(root, text="City", bg="light grey")
stateLabel = tk.Label(root, text="State", bg="light grey")
zipLabel = tk.Label(root, text="Zip", bg="light grey")
phoneLabel = tk.Label(root, text="Phone Number", bg="light grey")
rateLabel = tk.Label(root, text="Hourly Rate", bg="light grey")
hoursLabel = tk.Label(root, text="Normal Hours", bg="light grey")

#Placing the labels
idLabel.place(x=10, y=25)
nameLabel1.place(x=10, y=60)
nameLabel2.place(x=10, y=95)
addyLabel.place(x=10, y=130)
cityLabel.place(x=10, y=165)
stateLabel.place(x=10, y=200)
zipLabel.place(x=10, y=235)
phoneLabel.place(x=10, y=270)
rateLabel.place(x=10, y=305)
hoursLabel.place(x=10, y=340)

#Creating the entry boxes
idEntry = tk.Entry(root)
nameEntry1 = tk.Entry(root)
nameEntry2 = tk.Entry(root)
addyEntry = tk.Entry(root)
cityEntry = tk.Entry(root)
stateEntry = tk.Entry(root)
zipEntry = tk.Entry(root)
phoneEntry = tk.Entry(root)
rateEntry = tk.Entry(root)
hoursEntry = tk.Entry(root)

#Placing the entry boxes
idEntry.place(x=220, y=25)
nameEntry1.place(x=220, y=60)
nameEntry2.place(x=220, y=95)
addyEntry.place(x=220, y=130)
cityEntry.place(x=220, y=165)
stateEntry.place(x=220, y=200)
zipEntry.place(x=220, y=235)
phoneEntry.place(x=220, y=270)
rateEntry.place(x=220, y=305)
hoursEntry.place(x=220, y=340)

#Creating the buttons
btnSave = tk.Button(root, text="Save", command=save)
btnClear = tk.Button(root, text="Clear", command=clear_text)
btnClose = tk.Button(root, text="Close", command=close)
btnLoad = tk.Button(root, text="Load Data", command=loadData)
btnFirst = tk.Button(root, text="First", command=moveFirst)
btnLast = tk.Button(root, text="Last", command=moveLast)
btnNext = tk.Button(root, text="Next", command=moveNext)
btnPrev = tk.Button(root, text="Previous", command=movePrevious)

#Placing the buttons
btnSave.place(x=75, y=425)
btnClear.place(x=220, y=425)
btnClose.place(x=350, y=425)
btnLoad.place(x=470, y=425)
btnFirst.place(x=75, y=475)
btnPrev.place(x=210, y=475)
btnNext.place(x=350, y=475)
btnLast.place(x=470, y=475)

root.mainloop()   #Main loop ensuring the responsiveness of GUI