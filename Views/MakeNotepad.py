from tkinter import *
import tkinter
from tkinter.scrolledtext import ScrolledText
def notepadView(frame, title,description, message, makeNote, fetchNotes):
    Label(frame, text="Make a Note", fg="#eee", padx=10, pady=10, font=("Arial", 24)).pack(fill=BOTH)
    Label(frame, text="Title", fg="#ddd", pady=2, font=("Arial", 14)).pack()
    Entry(frame, textvar=title, width=50, borderwidth=5, bg="#eee", fg="#111", relief=FLAT).pack()
    Label(frame, text="Description", fg="#ddd", pady=2, font=("Arial", 14)).pack()
    descriptionBox = ScrolledText(frame, width=50, height=20,borderwidth=5, bg="#eee", fg="#111", relief=FLAT)
    descriptionBox.pack()
    Label(frame, textvar=message, fg="#fff", pady=2, font=("Arial", 16)).pack()
    Button(frame, text="Make a Note", bg="green", border=0, font=("""Arial
             """, 14), fg="#fff", padx=15, pady=10, activebackground="green", activeforeground="#fff",
           command=lambda: makeNote(descriptionBox)).pack()

    Button(frame, text="All Notes", bg="blue", border=0, font=("""Arial
             """, 14), fg="#fff", padx=15, pady=10, activebackground="blue", activeforeground="#fff",
           command=fetchNotes).pack()
