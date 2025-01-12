import tkinter as tk
from tkinter import messagebox
import random, string


#Main Window
rt = tk.Tk()
rt.title("Password Generator")
rt.geometry("800x500+230+80")


#Main Title 
title_label = tk.Label(rt, text="PASSWORD GENERATOR", font=("Arial", 30,"bold"), fg='brown').pack(pady=20)


#Password details gathering
length_label = tk.Label(rt, text="Password Length:", font=("Arial",18))
length_label.pack(anchor='w', padx=20)
length_scale = tk.Scale(rt, from_=6, to=15, orient='horizontal')
length_scale.set(8)
length_scale.pack(anchor='w', padx=20)


#Complexity options
uc_var = tk.IntVar()
dgt_var = tk.IntVar()
symb_var = tk.IntVar()

label = tk.Label(rt, text="Choose Complexity of Your Password", font=('Arial',18)).pack(anchor='w', pady=25, padx=20)
uc_checkbox = tk.Checkbutton(rt, text="include Uppercase Letters", font=('Arial',14), variable=uc_var).pack(anchor='w', padx=20)
dgt_checkbox = tk.Checkbutton(rt, text="include Digits", font=('Arial',14), variable=dgt_var).pack(anchor='w', padx=20)
symb_checkbox = tk.Checkbutton(rt, text="Add Special Characters", font=('Arial',14), variable=symb_var).pack(anchor='w', padx=20)


#Space to display Password
pwd_label = tk.Label(rt, text="", font=('Arial', 14), fg="red")
pwd_label.pack(pady=10)


#Button for Getting Password and copy password
btn_frame = tk.Frame(rt).pack()

#Generating Password function
def Generate_pwd():
    length = length_scale.get()
    use_uc = uc_var.get()
    use_digit = dgt_var.get()
    use_symb = symb_var.get()

    if not(use_uc or use_digit or use_symb):
        messagebox.showerror("ERROR..!!", "Please, Choose atleast 1 complexity option")
        return
    
    char = string.ascii_lowercase
    if use_uc:
        char = char + string.ascii_uppercase
    if use_digit:
        char = char + string.digits
    if use_symb:
        char = char + string.punctuation
    
    password =''.join(random.choices(char, k=length))
    pwd_label.config(text=password)

#"Get Password" button
pwd_btn = tk.Button(btn_frame, text="GET PASSWORD", font=("Arial", 12, "bold"), command=Generate_pwd, bg="blue", fg="white")
pwd_btn.pack(side="left",padx=80)

#Copy Function
def copy_option():
    pwd = pwd_label.cget("text")
    if pwd:
        rt.clipboard_clear()
        rt.clipboard_append(pwd)
        rt.update()
        messagebox.showinfo("Password Copied", "Password is copied to Keyboard..!")
    else:
        messagebox.showwarning("No Password", "Generate a Password First...!")

#"Copy" button
cpy_btn = tk.Button(btn_frame, text="COPY", font=("Arial", 12, "bold"), command=copy_option)
cpy_btn.pack(side="left",padx=80)

#clear function
def clear():
    pwd_label.config(text="")
    length_scale.set(8)
    uc_var.set(0)
    dgt_var.set(0)
    symb_var.set(0)

#"clear" button
clear_btn = tk.Button(btn_frame, text="Clear Field", font=("Arial", 12, "bold"), bg="red", fg="white", command=clear)
clear_btn.pack(side="left", padx=80)



#applicaiton running
rt.mainloop()