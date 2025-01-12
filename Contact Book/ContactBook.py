import tkinter as tk
from tkinter import ttk, messagebox
from storedb import create_table, insert_contact, update_contact, delete_contact, search_contact, view_contact

def main():
    create_table()

    #adding details
    def on_add():
        name, phone, email, address = name_var.get(), phone_var.get(), email_var.get(), address_var.get()
        if name and phone:
            result = insert_contact(name, phone, email, address)
            if result == "success":
                messagebox.showinfo("SUCCESS..!","Contact addedd successfully..!")
            else:
                messagebox.showerror("ERROR..!", "Phone number is already exists..!")
            refresh_contact()
            clear()
        else:
            messagebox.showwarning("ERROR..!","Name and Phone are required..!")

    #updating details   
    def on_update():
        selected = tree.focus()
        if selected:
            contact_id = tree.item(selected)['values'][0]
            #getting current field values
            curr_name = name_var.get().strip()
            curr_phone = phone_var.get().strip()
            curr_email = email_var.get().strip()
            curr_address = address_var.get().strip()
            
            contacts = view_contact()
            existing_contact = next((row for row in contacts if row[0] == contact_id), None)

            if existing_contact:
                name = curr_name if curr_name else existing_contact[1]
                phone = curr_phone if curr_phone else existing_contact[2]
                email = curr_email if curr_email else existing_contact[3]
                address = curr_address if curr_address else existing_contact[4]

                update_contact(contact_id, name, phone, email, address)
                messagebox.showinfo("SUCCESS..!","Contact updated successfully..!")
                refresh_contact()
                clear()
            else:
                messagebox.showerror("ERROR..!","Unable to find the selected contact in the database.")
        else:
            messagebox.showwarning("ERROR..!","No contact selected..!")


    #Delete function
    def on_delete():
        selected =tree.focus()
        if selected:
            contact_id = tree.item(selected)['values'][0]
            if messagebox.askyesno("Confirmation","Are you sure, you want to delete selected contact?"):
                delete_contact(contact_id)
                messagebox.showinfo("Success..!","Contact deleted successfully..!")
                refresh_contact()
        else:
            messagebox.showwarning("ERROR..!","No Contact selected..!")

    #searching data
    def on_search():
        search_term = search_var.get().strip()
        if search_term:
            rows = search_contact(search_term)
            if rows:
                refresh_tree(rows)
            else:
                messagebox.showinfo("No Results..!",f"No data found for '{search_term}. Displaying all contacts")
                refresh_contact()
        else:
            messagebox.showwarning("Empty Search","Please enter a search word.")
            refresh_contact()
        clear()

    #refresh data
    def refresh_contact():
        rows = view_contact()
        refresh_tree(rows)

    #clearing all fields
    def clear():
        name_var.set("")
        phone_var.set("")
        email_var.set("")
        address_var.set("")
        search_var.set("")


#--------------------------------------------------
    
    #User View
    root = tk.Tk()
    root.title("Store Contact Book")
    root.geometry("1000x600+150+40")

    tk.Label(root, text="Contact Book", font=("Arial", 30,"bold"), fg='brown').pack(pady=20)

    #Variables
    name_var, phone_var, email_var, address_var, search_var = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()

    #Form
    Form_frame = tk.Frame(root)
    Form_frame.pack(pady=10)

    #Store Name (Row=0)
    tk.Label(Form_frame, text="Store Name :", font=('Arial',12)).grid(row=0,  column=0, padx=5, pady=5)
    tk.Entry(Form_frame, textvariable=name_var).grid(row=0, column=1, padx=5, pady=5)

    #Phone Number (Row=0)
    tk.Label(Form_frame, text="Phone Number :", font=('Arial',12)).grid(row=0, column=2, padx=5, pady=5)
    tk.Entry(Form_frame, textvariable=phone_var).grid(row=0, column=3, padx=5, pady=5)

    #Email (Row=1)
    tk.Label(Form_frame, text="Email :", font=('Arial',12)).grid(row=0, column=4, padx=5, pady=5)
    tk.Entry(Form_frame, textvariable=email_var).grid(row=0, column=5, padx=5, pady=5)

    #Address (Row=1)
    tk.Label(Form_frame, text="Address :", font=('Arial',12)).grid(row=0, column=6, padx=5, pady=5)
    tk.Entry(Form_frame, textvariable=address_var).grid(row=0, column=7, padx=5, pady=5)

    #buttons
    #Add button (Row=2)
    tk.Button(Form_frame, text="Add New Contact", command=on_add, font=("Arial", 10, "bold"), bg="blue", fg="white").grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    #update button (Row=2)
    tk.Button(Form_frame, text="Update Contact", command=on_update, font=("Arial", 10, "bold")).grid(row=3, column=2, columnspan=2, padx=10, pady=10)

    #Delete Button (Row=2)
    tk.Button(Form_frame, text="Delete Contact", command=on_delete, font=("Arial", 10, "bold"), bg="red", fg="white").grid(row=3, column=4, columnspan=2, padx=10, pady=10)

    #Refresh Button (Row=3)
    tk.Button(Form_frame, text="Show All Data", command=refresh_contact, font=("Arial", 10, "bold")).grid(row=3, column=6, columnspan=2, padx=10, pady=10)

    #search bar
    search_frame = tk.Frame(root)
    search_frame.pack(pady=10)

    tk.Entry(search_frame, textvariable=search_var).grid(row=0, column=0, padx=5, pady=5)

    tk.Button(search_frame, text="Search", command=on_search, font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5, pady=5)


    #treeview

    frame = tk.Frame(root, bd=2, relief="solid")
    frame.pack(pady=10, fill="both", expand=True)

    style = ttk.Style()
    style.configure("Treeview", rowheight=30, bordercolor='black' , relief="solid",borderwidth=1, highlightthickness=1)
    style.map("Treeview", background=[('selected', '#cdeafe')], foreground=[('selected', 'red')])
    style.layout("Treview", [('Treeview.treearea',{'sticky':'nswe'})])
    
    tree = ttk.Treeview(frame, style='Treeview', columns=("ID", "Name", "Phone", "Email", "Address"), show="headings")
    tree.heading("ID", text="ID")
    tree.column("ID", width=50, anchor="center")
    tree.heading("Name", text="Store Name")
    tree.column("Name", width=150, anchor="center")
    tree.heading("Phone", text="Phone Number")
    tree.column("Phone", width=150, anchor="center")
    tree.heading("Email", text="Email")
    tree.column("Email", width=200, anchor="center")
    tree.heading("Address", text="Address")
    tree.column("Address", width=200, anchor="center")
    
    tree.tag_configure("even", background="#f0f0f0")
    tree.tag_configure("odd", background="#ffffff")

    #refreshing tree view   
    def refresh_tree(rows):
        for row in tree.get_children():
            tree.delete(row)

        for index, row in enumerate(rows):
            tag = "even" if index % 2 == 0 else "odd"
            tree.insert("","end", values=row, tags=(tag,))


    tree.pack(pady=10, fill="both", expand=True)
    #New Frame
    # footer_frame = tk.Frame(root)
    # footer_frame.pack(pady=10)

    

    refresh_contact()
    root.mainloop()

if __name__ == "__main__":
    main()