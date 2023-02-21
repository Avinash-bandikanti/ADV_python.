from tkinter import *


# Designing Main Screen So, first of all, you have to design the main screen.
# two buttons Login and Register.
def main_screen():
    mainscreen = Tk()  # create a GUI window
    mainscreen.geometry("500x600")  # set the configuration of GUI window
    mainscreen.title("Train ticket booking")  # set the title of GUI window


# create a Form label
Label(text="Train ticket", bg="white", width="30", height="2", font=("Calibri", 13)).pack()
Label(text="").pack()
# create Login Button
Button(text="Login", height="2", width="30").pack()
Label(text="").pack()
# create a register button
Button(text="Register", height="2", width="30").pack()

Tk().mainloop()  # start the GUI
main_screen()  # call the main_account_screen() function