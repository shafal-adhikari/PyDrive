from tkinter import *
import sqlite3
import bcrypt
from Views.registerView import registerView
from Views.loginView import loginView
root = Tk()

list = [1,2,3]

fullname = StringVar()
username = StringVar()
password = StringVar()

registerFrame = Frame(root)
registerFrame.pack()

loginFrame = Frame(root)
# loginFrame.pack(row=0,column=0)

root.geometry('500x500+200+100')

def switchPage(currentFrame, nextFrame):
    currentFrame.pack_forget()
    nextFrame.pack()

def register():
    db = sqlite3.connect('app.db')
    cur = db.cursor()

    # cur.execute("""CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, fullname text NOT NULL,
    # username TEXT NOT NULL, password text NOT NULL)""")
    hashed_password = bcrypt.hashpw(password.get().encode('utf-8'), bcrypt.gensalt())

    cur.execute("""INSERT INTO users(fullname, username, password) values(?,?,?)""",
                (fullname.get(), username.get(), hashed_password))
    db.commit()


registerView(registerFrame, fullname, username, password, register, switchPage, loginFrame)
loginView(loginFrame, username, password, register)

root.mainloop()