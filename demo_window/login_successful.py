from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Bus Ticket Booking System")

# create label widgets
label_name = Label(root, text="Name:")
label_phone = Label(root, text="Phone:")
label_email = Label(root, text="Email:")
label_seat = Label(root, text="Seat Number:")

# create entry widgets
entry_name = Entry(root)
entry_phone = Entry(root)
entry_email = Entry(root)
entry_seat = Entry(root)

# create function to book the seat
def book_seat():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    seat_number = entry_seat.get()

    # save the booking details in a file or database
    # send booking confirmation to passenger's phone number using SMS gateway API

    # display a message box with the booking confirmation
    message = f"Booking confirmed for {name}.\nSeat Number: {seat_number}"
    messagebox.showinfo("Booking Confirmation", message)

# create button widget
button_book = Button(root, text="Book", command=book_seat)

# add the widgets to the window
label_name.grid(row=0, column=0)
entry_name.grid(row=0, column=1)
label_phone.grid(row=1, column=0)
entry_phone.grid(row=1, column=1)
label_email.grid(row=2, column=0)
entry_email.grid(row=2, column=1)
label_seat.grid(row=3, column=0)
entry_seat.grid(row=3, column=1)
button_book.grid(row=4, column=1)

root.mainloop()