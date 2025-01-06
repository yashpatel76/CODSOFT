import sqlite3

#Creation of DB
def create_table():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS store
    (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        phone TEXT UNIQUE NOT NULL,
        email TEXT,
        address TEXT
    )
''')
    conn.commit()
    conn.close()

#adding data
def insert_contact(name, phone, email, address):
    try:
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO store (name, phone, email, address) VALUES(?, ?, ?, ?)',(name, phone, email, address))
        conn.commit()
        conn.close()
        return "success"
    except sqlite3.IntegrityError:
        return "ERROR...!! Data is not Inserted into Database"

#displaying data 
def view_contact():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM store')
    rows = cursor.fetchall()
    conn.close()
    return rows

#updating data
def update_contact(contact_id, name, phone, email, address):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute(''' 
    UPDATE store
    SET name = ?, phone = ?, email = ?,address = ?
    WHERE id = ?
    ''',(name, phone, email, address, contact_id))
    conn.commit()
    conn.close()

#deleting data
def delete_contact(contact_id):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM store WHERE id = ?",(contact_id,))
    conn.commit()
    conn.close()
    reset_id()

#searching data
def search_contact(search):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    query = "SELECT * FROM store WHERE name LIKE ? OR phone LIKE ? OR email LIKE ? OR address LIKE ?"
    cursor.execute(query,(f"%{search}%", f"%{search}%", f"%{search}%", f"%{search}%"))
    rows = cursor.fetchall()
    conn.close()
    return rows

#Reseting IDs
def reset_id():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute(" CREATE TEMPORARY TABLE temp_table AS SELECT * FROM store")
    cursor.execute("DELETE FROM store")
    cursor.execute("INSERT INTO store (id, name, phone, email, address) SELECT ROW_NUMBER() OVER (ORDER BY id), name, phone, email, address FROM temp_table")
    cursor.execute("DROP TABLE temp_table")
    conn.commit()
    conn.close()


