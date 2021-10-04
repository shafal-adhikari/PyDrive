from tkinter import *
import sqlite3
import bcrypt
from Views.registerView import registerView
from Views.loginView import loginView
from Views.MakeNotepad import notepadView
from Views.AllNotes import AllNotes
from Views.Note import Note
import tkinter as tk
root = Tk()

list = [1,2,3]

fullname = StringVar()
username = StringVar()
password = StringVar()
message= StringVar()


title = StringVar()
description = StringVar()

registerFrame = Frame(root)
registerFrame.pack()

notepadFrame = Frame(root)
allNotesFrame = Frame(root)

# allNotesFrame.pack()
loginFrame = Frame(root)
# loginFrame.pack(row=0,column=0)
noteFrame = Frame(root)
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
def makeNote(description):
    db = sqlite3.connect('app.db')
    cur = db.cursor()
    # cur.execute("""CREATE TABLE notes(id INTEGER PRIMARY KEY AUTOINCREMENT, title text NOT NULL,
    #  description MEDIUMTEXT NOT NULL, userId INTEGER NOT NULL)""")
    cur.execute("""INSERT INTO notes(title, description, userId) values(?,?, ?)""",
                (title.get(), description.get('1.0', tk.END), userId))
    db.commit()

def openNote(note):
    switchPage(allNotesFrame, noteFrame)
    Note(noteFrame, note, fetchNotes)


def fetchNotes():
    switchPage(loginFrame, allNotesFrame)
    switchPage(notepadFrame, allNotesFrame)
    switchPage(noteFrame, allNotesFrame)
    db = sqlite3.connect('app.db')
    cur = db.cursor()
    result = cur.execute('Select * from notes where userId=?', (userId,))
    AllNotes(allNotesFrame, result.fetchall(), openNote, switchPage, notepadFrame)

def login():
    global passwordResult
    db = sqlite3.connect('app.db')
    if(username.get()=='' or password.get() == ''):
        message.set('Please fill in all the fields')
        return
    cur = db.cursor()
    result = cur.execute("Select * from users where username=?", (username.get(),))
    for row in result:
        global userId
        print('row', row)
        passwordResult= row[3]
        check = bcrypt.checkpw(password.get().encode('utf-8'), passwordResult)
        if (check):
            print('Successfully logged in')
            userId = row[0]
            fetchNotes()
            return
        else:
            print('Invalid credentials')
            return
    else:
        print('Invalid credentials')

notepadView(notepadFrame, title, description, message, makeNote,fetchNotes)
registerView(registerFrame, fullname, username, password, register, switchPage, loginFrame, message)
loginView(loginFrame, username, password, login, switchPage, registerFrame, message)

root.mainloop()