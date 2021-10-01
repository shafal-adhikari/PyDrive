from tkinter import *

def registerView(frame, fullname, username, password, command, switchFrame, loginFrame):
    Label(frame, text="Register", fg="#eee", padx=10, pady=10, font=("Arial", 24)).pack(fill=BOTH)
    Label(frame, text="Full Name", fg="#ddd", pady=2, font=("Arial", 14)).pack()
    Entry(frame, textvar=fullname, width=50, borderwidth=5, bg="#eee", fg="#111", relief=FLAT).pack()
    Label(frame, text="Username", fg="#ddd", pady=2, font=("Arial", 14)).pack()
    Entry(frame, textvar=username, width=50, borderwidth=5, bg="#eee", fg="#111", relief=FLAT).pack()
    Label(frame, text="Password", fg="#ddd", pady=2, font=("Arial", 14)).pack()
    Entry(frame, textvar=password, width=50, show="*", borderwidth=5, bg="#eee", fg="#111", relief=FLAT).pack()

    Button(frame, text="Register", bg="green", border=0, font=("""Arial
        """, 14), fg="#fff", padx=15, pady=10, activebackground="green", activeforeground="#fff", command=command).pack()

    Button(frame, text="Login", bg="green", border=0, font=("""Arial
            """, 14), fg="#fff", padx=15, pady=10, activebackground="green", activeforeground="#fff",
           command=lambda: switchFrame(frame, loginFrame)).pack()

