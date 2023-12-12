import sqlite3
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("CLASSROOM BOOKING")
root.geometry("2000x900")
my_tree = ttk.Treeview(root)
storeName = "CLASSROOM BOOKING"


def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup


def insert( id, name, classrooms, time, date):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
    inventory(itemId TEXT, itemName TEXT, itemClassrooms TEXT, itemTime TEXT, itemDate TEXT)""")
    
    cursor.execute("INSERT INTO inventory VALUES ('" + str(id) + "','" + str(name) + "','" + str(classrooms) + "','" + str(time) + "','" + str(date) + "')")
    conn.commit()
    

def delete(data):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemId TEXT, itemName TEXT, itemClassrooms TEXT, itemTime TEXT, itemDate TEXT)""")

    cursor.execute("DELETE FROM inventory WHERE itemId = '" + str(data) + "'")
    conn.commit()


def update(id, name, classrooms, time, date,  idName):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemId TEXT, itemName TEXT, itemQuantity TEXT, itemTime TEXT, itemDate TEXT)""")

    cursor.execute("UPDATE inventory SET itemId = '" + str(id) + "', itemName = '" + str(name) + "', itemClassrooms = '" + str(classrooms) + "', itemTime = '" + str(time) +  "', itemDate = '" + str(date) + "' WHERE itemId='"+str(idName)+"'")
    conn.commit()


def read():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemId TEXT, itemName TEXT, itemClassrooms TEXT, itemTime TEXT, itemDate TEXT)""")

    cursor.execute("SELECT * FROM inventory")
    results = cursor.fetchall()
    conn.commit()
    return results


def insert_data():
    itemId = str(entryId.get())
    itemName = str(entryName.get())
    itemClassrooms = str(entryClassrooms.get())
    itemTime = str(entryTime.get())
    itemDate = str(entryDate.get())
    if itemId == "" or itemName == " ":
        print("Error Inserting Id")
    elif itemName == "" or itemName == " ":
        print("Error Inserting Name")
    elif itemClassrooms == "" or itemClassrooms == " ":
        print("Error Inserting Classrooms")
    elif itemTime == "" or itemTime == " ":
        print("Error Inserting Time")
    elif itemDate == "" or itemDate == " ":
        print("Error Inserting Date")    
    else:
        insert(str(itemId), str(itemName), str(itemClassrooms), str(itemTime), str(itemDate))

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=6, columnspan=5, rowspan=6, padx=12, pady=12)


def delete_data():
    selected_item = my_tree.selection()[0]
    deleteData = str(my_tree.item(selected_item)['values'][0]) 
    delete(deleteData)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=6, columnspan=5, rowspan=6, padx=12, pady=12)

def update_data():
    selected_item = my_tree.selection()[0]
    update_name = my_tree.item(selected_item)['values'][0]
    update(entryId.get(), entryName.get(), entryClassrooms.get(), entryTime.get(), entryDate.get(), update_name)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=6, columnspan=5, rowspan=6, padx=12, pady=12)

#grid and label

titleLabel = Label(root, text=storeName, font=('Univers', 30), bd=2, bg= "#473C8B" )
titleLabel.grid(row=0, column=0, columnspan=8, padx=20, pady=20)

idLabel = Label(root, text="ID", font=('Univers', 15))
nameLabel = Label(root, text="Name", font=('Univers', 15))
classroomsLabel = Label(root, text="Classrooms", font=('Univers', 15))
timeLabel = Label(root, text="Time", font=('Univers', 15))
dateLabel = Label(root, text="Date", font=('Univers', 15))
idLabel.grid(row=1, column=0, padx=10, pady=10)
nameLabel.grid(row=2, column=0, padx=10, pady=10)
classroomsLabel.grid(row=3, column=0, padx=10, pady=10)
timeLabel.grid(row=4, column=0, padx=10, pady=10)
dateLabel.grid(row=5, column=0, padx=10, pady=10)

entryId = Entry(root, width=25, bd=5, font=('Univers', 15))
entryName = Entry(root, width=25, bd=5, font=('Univers', 15))
entryClassrooms = Entry(root, width=25, bd=5, font=('Univers', 15))
entryTime = Entry(root, width=25, bd=5, font=('Univers', 15))
entryDate = Entry(root, width=25, bd=5, font=('Univers', 15))
entryId.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
entryName.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
entryClassrooms.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
entryTime.grid(row=4, column=1, columnspan=3, padx=5, pady=5)
entryDate.grid(row=5, column=1, columnspan=3, padx=5, pady=5)


# button 

buttonEnter = Button(
    root, text="Enter", padx=5, pady=5, width=5,
    bd=3, font=('Univers', 15), bg="#836FFF", command=insert_data)
buttonEnter.grid(row=6, column=1, columnspan=1)

buttonUpdate = Button(
    root, text="Update", padx=5, pady=5, width=5,
    bd=3, font=('Univers', 15), bg="#836FFF", command=update_data)
buttonUpdate.grid(row=6, column=2, columnspan=1)

buttonDelete = Button(
    root, text="Delete", padx=5, pady=5, width=5,
    bd=3, font=('Univers', 15), bg="#836FFF", command=delete_data)
buttonDelete.grid(row=6, column=3, columnspan=1)

#style table

style = ttk.Style()
style.configure("Treeview.Heading", font=('Univers', 15))

my_tree['columns'] = ("ID", "Name", "Classrooms", "Time", "Date")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=W, width=200)
my_tree.column("Name", anchor=W, width=200)
my_tree.column("Classrooms", anchor=W, width=120)
my_tree.column("Time", anchor=W, width=120)
my_tree.column("Date", anchor=W, width=120)
my_tree.heading("ID", text="ID", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Classrooms", text="Classrooms", anchor=W)
my_tree.heading("Time", text="Time", anchor=W)
my_tree.heading("Date", text="Date", anchor=W)

for data in my_tree.get_children():
    my_tree.delete(data)

for result in reverse(read()):
    my_tree.insert(parent='', index='end', iid=0, text="", values=(result), tag="orow")

my_tree.tag_configure('orow', background='#EEEEEE', font=('Univers', 15))
my_tree.grid(row=1, column=6, columnspan=5, rowspan=6, padx=12, pady=12)

root.mainloop()