import tkinter as tk
from tkinter import *
from tkinter import messagebox
window=tk.Tk()
window.title("login")
entry=Entry(window)
entry.pack()
def demo():
    messagebox.showinfo("hcl","hello")
def read_entry():
    val=entry.get()
    messagebox.showinfo("hcl data",val)
btn=Button(window,text="Login",command=read_entry)
btn.pack()
window.mainloop()