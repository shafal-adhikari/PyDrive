from tkinter import *
import sqlite3

import bcrypt

root = Tk()

fullname = StringVar()
username = StringVar()
password = StringVar()


root.geometry('500x500+200+100')

def register():
    db = sqlite3.connect('app.db')
    cur = db.cursor()

    # cur.execute("""CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, fullname text NOT NULL,
    # username TEXT NOT NULL, password text NOT NULL)""")
    hashed_password = bcrypt.hashpw(password.get().encode('utf-8'), bcrypt.gensalt())

    cur.execute("""INSERT INTO users(fullname, username, password) values(?,?,?)""",
                (fullname.get(), username.get(), hashed_password))
    db.commit()

Label(root, text="Register", fg="#eee", padx=10, pady=10, font=("Arial", 24)).pack(fill=BOTH)
Label(root, text="Full Name", fg="#ddd", pady=2, font=("Arial", 14)).pack()
Entry(root, textvar=fullname, width=50, borderwidth=5, bg="#eee", fg="#111", relief=FLAT).pack()
Label(root, text="Username", fg="#ddd", pady=2, font=("Arial", 14)).pack()
Entry(root, textvar=username, width=50, borderwidth=5, bg="#eee", fg="#111", relief=FLAT).pack()
Label(root, text="Password", fg="#ddd", pady=2, font=("Arial", 14)).pack()
Entry(root, textvar=password, width=50, show="*", borderwidth=5, bg="#eee", fg="#111", relief=FLAT).pack()

Button(root, text="Register", bg="green", border=0, font=("""Arial
    """, 14), fg="#fff", padx=15, pady=10, activebackground="green", activeforeground="#fff", command=register).pack()
root.mainloop()