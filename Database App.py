import tkinter as tk
import sqlite3

root = tk.Tk()
root.title('Database App')
root.geometry('400x600')

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

'''
# Create table
c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )
""")
'''

# Create function to delete records
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute('DELETE FROM addresses WHERE oid=' + str(delete_box.get()))


    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

# Create function to save edited records
def save():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid""",

        {
        'first':f_name.get(),
        'last':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zipcode':zipcode.get(),

        'oid':record_id
        })

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    # Close window
    editor.destroy()

# Create function to delete records
def update():
    global editor
    editor = tk.Tk()
    editor.title('Editor')
    editor.geometry('450x300')

    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    record_id = delete_box.get()

    # Query the database
    c.execute('SELECT * FROM addresses WHERE oid=' + str(record_id))
    records = c.fetchall()

    # Create global variables for text box names
    global f_name
    global l_name
    global address
    global city
    global state
    global zipcode

    # Create text boxes
    f_name = tk.Entry(editor, width=30)
    f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name = tk.Entry(editor, width=30)
    l_name.grid(row=1, column=1)
    address = tk.Entry(editor, width=30)
    address.grid(row=2, column=1)
    city = tk.Entry(editor, width=30)
    city.grid(row=3, column=1)
    state = tk.Entry(editor, width=30)
    state.grid(row=4, column=1)
    zipcode = tk.Entry(editor, width=30)
    zipcode.grid(row=5, column=1)

    # Create text box labels
    f_name_label = tk.Label(editor, text='First Name')
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = tk.Label(editor, text='Last Name')
    l_name_label.grid(row=1, column=0)
    address_label = tk.Label(editor, text='Address')
    address_label.grid(row=2, column=0)
    city_label = tk.Label(editor, text='City')
    city_label.grid(row=3, column=0)
    state_label = tk.Label(editor, text='State')
    state_label.grid(row=4, column=0)
    zipcode_label = tk.Label(editor, text='Zip Code')
    zipcode_label.grid(row=5, column=0)


    # Loop through results
    for record in records:
        f_name.insert(0, record[0])
        l_name.insert(0, record[1])
        address.insert(0, record[2])
        city.insert(0, record[3])
        state.insert(0, record[4])
        zipcode.insert(0, record[5])

    # Create a save button
    save_btn = tk.Button(editor, text='Save Record', command=save)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Create submit function for database
def submit():

    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute('INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)',
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
            }
    )
    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


    # Clear text boxes
    f_name.delete(0, 'end')
    l_name.delete(0, 'end')
    address.delete(0, 'end')
    city.delete(0, 'end')
    state.delete(0, 'end')
    zipcode.delete(0, 'end')

# Create query function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Query the database
    c.execute('SELECT *, oid FROM addresses')
    records = c.fetchall()

    # Loop through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + '\n'

    query_label = tk.Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

#c.execute('DELETE FROM addresses')

# Create text boxes
f_name = tk.Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = tk.Entry(root, width=30)
l_name.grid(row=1, column=1)
address = tk.Entry(root, width=30)
address.grid(row=2, column=1)
city = tk.Entry(root, width=30)
city.grid(row=3, column=1)
state = tk.Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = tk.Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = tk.Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create text box labels
f_name_label = tk.Label(root, text='First Name')
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = tk.Label(root, text='Last Name')
l_name_label.grid(row=1, column=0)
address_label = tk.Label(root, text='Address')
address_label.grid(row=2, column=0)
city_label = tk.Label(root, text='City')
city_label.grid(row=3, column=0)
state_label = tk.Label(root, text='State')
state_label.grid(row=4, column=0)
zipcode_label = tk.Label(root, text='Zip Code')
zipcode_label.grid(row=5, column=0)

delete_label = tk.Label(root, text='Delete ID')
delete_label.grid(row=9, column=0, pady=5)


# Create a submit button
submit_btn = tk.Button(root, text='Add Record To Database', command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a query button
query_btn = tk.Button(root, text='Show Records', command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=132)

# Create a delete button
delete_btn = tk.Button(root, text='Delete Record', command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=130)

# Create an update button
update_btn = tk.Button(root, text='Edit Records', command=update)
update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()
