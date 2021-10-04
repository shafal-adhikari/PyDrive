from tkinter import *

def Note(frame, note, fetchNotes):
    for widget in frame.winfo_children():
        widget.destroy()
    title = Label(frame, text=note[1], fg="#eee", padx=10, pady=10, font=("Arial", 24))
    title.pack()
    description = Label(frame, text=note[2], fg="#eee", padx=10, pady=10, font=("Arial", 24))
    description.pack()
    Button(frame, text="All Notes", bg="blue", border=0, font=("""Arial
             """, 14), fg="#fff", padx=15, pady=10, activebackground="blue", activeforeground="#fff",
           command=fetchNotes).pack()
