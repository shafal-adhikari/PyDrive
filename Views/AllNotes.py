from tkinter import *

def AllNotes(frame, notes, openNote, switchPage, noteFrame):
    for widget in frame.winfo_children():
        widget.destroy()
    i = 1
    for note in notes:
        label = Label(frame, text=str(i)+'. '+note[1], fg="#eee", padx=10, pady=10, font=("Arial", 24))
        label.pack(fill=BOTH)
        label.bind("<Button-1>", lambda x:openNote(note))
        i = i+1
    Button(frame, text="Make a Note", bg="blue", border=0, font=("""Arial
             """, 14), fg="#fff", padx=15, pady=10, activebackground="blue", activeforeground="#fff",
           command=lambda: switchPage(frame, noteFrame)).pack()