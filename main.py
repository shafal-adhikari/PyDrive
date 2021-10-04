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
message= StringVar()

registerFrame = Frame(root)
registerFrame.pack()
global userId
loginFrame = Frame(root)
# loginFrame.pack(row=0,column=0)

root.geometry('500x500+200+100')

def switchPage(currentFrame, nextFrame):
    currentFrame.pack_forget()
    nextFrame.pack()
    fullname.set('')
    username.set('')
    password.set('')
    message.set('')

def register():
    db = sqlite3.connect('app.db')
    cur = db.cursor()
    if(username.get()=='' or password.get() == '' or fullname.get()==''):
        message.set('Please fill in all the fields')
        return
    # cur.execute("""CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, fullname text NOT NULL,
    # username TEXT NOT NULL, password text NOT NULL)""")
    hashed_password = bcrypt.hashpw(password.get().encode('utf-8'), bcrypt.gensalt())

    cur.execute("""INSERT INTO users(fullname, username, password) values(?,?,?)""",
                (fullname.get(), username.get(), hashed_password))
    db.commit()

def login():
    global passwordResult
    db = sqlite3.connect('app.db')
    if(username.get()=='' or password.get() == ''):
        message.set('Please fill in all the fields')
        return
    cur = db.cursor()
    result = cur.execute("Select * from users where username=?", (username.get(),))
    for row in result:
        print('row', row)
        passwordResult= row[3]
        check = bcrypt.checkpw(password.get().encode('utf-8'), passwordResult)
        if (check):
            print('Successfully logged in')
            userId = row[0]
        else:
            print('Invalid credentials')
            return
    else:
        print('Invalid credentials')





registerView(registerFrame, fullname, username, password, register, switchPage, loginFrame, message)
loginView(loginFrame, username, password, login, switchPage, registerFrame, message)

root.mainloop()