import tkinter as tk
import tkinter as tk
from tkinter import simpledialog

class BlackDialog(simpledialog.Dialog):
    def body(self, master):
        self.configure(bg='black')
        tk.Label(master, text="City:", fg='white', bg='black').grid(row=0)
        self.entry = tk.Entry(master, bg='black', fg='white')
        self.entry.grid(row=0, column=1)
        return self.entry  # Focus on the entry field

    def apply(self):
        self.result = self.entry.get()

# Create the black-themed dialog box


