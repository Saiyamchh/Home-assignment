import tkinter as tk
from tkinter import *

def validate_distance_input(P):
    if P == "" or P.isdigit() and int(P) >= 0:
        return True
    else:
        return False

def validate_date_input(P):
    # You can add more date validation logic here if needed.
    return True

def calculate_bill():
    customer_name = var1.get()
    date_of_rental = var2.get()
    distance = var3.get()
    
    if not customer_name:
        var4.set("Please enter your name.")
    elif not date_of_rental:
        var4.set("Please enter the date of rental.")
    elif not validate_date_input(date_of_rental):
        var4.set("Invalid date format.")
    elif distance <= 0:
        var4.set("Please enter a valid distance.")
    else:
        x = distance
        bill = 0
        if rbVariable1.get() == 1:
            if x >= 1 and x <= 10:
                charge = x * 6
            elif x > 10 and x <= 30:
                charge = 60 + (x - 10) * 5
            else:
                charge = 60 + 100 + (x - 30) * 4
            bill += charge
            if rbVariable2.get() == 1:
                bill += 50
            else:
                bill += 30

        if rbVariable1.get() == 2:
            if x >= 1 and x <= 10:
                charge = x * 7
            elif x > 10 and x <= 30:
                charge = 70 + (x - 10) * 6
            else:
                charge = 70 + 120 + (x - 30) * 5
            bill += charge
            if rbVariable2.get() == 1:
                bill += 80
            else:
                bill += 60

        if rbVariable1.get() == 3:
            if x >= 1 and x <= 10:
                charge = x * 8.5
            elif x > 10 and x <= 30:
                charge = 85 + (x - 10) * 7
            else:
                charge = 85 + 140 + (x - 30) * 6
            bill += charge
            if rbVariable2.get() == 1:
                bill += 150
            else:
                bill += 100
            if rbVariable3.get() == 1:
                bill += 80

        if rbVariable1.get() == 4:
            if x >= 1 and x <= 10:
                charge = x * 10
            elif x > 10 and x <= 30:
                charge = 100 + (x - 10) * 8
            else:
                charge = 100 + 160 + (x - 30) * 7
            bill += charge
            if rbVariable2.get() == 1:
                bill += 250
            else:
                bill += 150
            if rbVariable3.get() == 1:
                bill += 100

        output_text = f"Your name is: {customer_name}\nDate of Rental is: {date_of_rental}\nYour bill is: {bill}"
        var4.set(output_text)

def disable_outstation():
    if rbVariable1.get() in [1, 2]:
        rbVariable3.set(2)  # Set the default to 'Local' if Nano or Mini is selected
        rbGroupThree.config(state=DISABLED)
    else:
        rbGroupThree.config(state=NORMAL)

root = Tk()
var1 = StringVar()
var2 = StringVar()
var3 = IntVar()
var4 = StringVar()
rbVariable1 = tk.IntVar()
rbVariable2 = tk.IntVar()
rbVariable3 = tk.IntVar()

root.geometry('887x589')
root.configure(background='light blue')
root.title('CarRental')

Label(root, text='WheelWonders', bg='light blue', font=('arial', 20, 'normal')).place(x=349, y=45)

Label(root, text='Customer Name', bg='light blue', font=('arial', 20, 'normal')).place(x=106, y=137)
one = Entry(root, textvariable=var1)
one.place(x=400, y=138)

Label(root, text='Date of Rental', bg='light blue', font=('arial', 20, 'normal')).place(x=112, y=208)
two = Entry(root, textvariable=var2, validate="key", validatecommand=(root.register(validate_date_input), "%P"))
two.place(x=400, y=213)

Label(root, text='Distance', bg='light blue', font=('arial', 20, 'normal')).place(x=114, y=283)
three = Entry(root, textvariable=var3, validate="key", validatecommand=(root.register(validate_distance_input), "%P"))
three.place(x=397, y=292)

frame = Frame(root, width=0, height=0, bg='#FFEFDB')
frame.place(x=163, y=362)
ARBEES = [
    ('Nano', 1),
    ('Mini', 2),
    ('Premier', 3),
    ('XL', 4),
]
for text, mode in ARBEES:
    rbGroupOne = Radiobutton(frame, text=text, variable=rbVariable1, value=mode, bg='light blue', font=('arial', 20, 'normal'), command=disable_outstation)
    rbGroupOne.pack(side='left', anchor='w')

frame = Frame(root, width=0, height=0, bg='black')
frame.place(x=241, y=460)
ARBEES = [
    ('AC', 1),
    ('Non AC', 2),
]
for text, mode in ARBEES:
    rbGroupTwo = Radiobutton(frame, text=text, variable=rbVariable2, value=mode, bg='light blue', font=('arial', 20, 'normal'))
    rbGroupTwo.pack(side='left', anchor='w')

frame = Frame(root, width=0, height=0, bg='#FF1493')
frame.place(x=219, y=411)
ARBEES = [
    ('Outstation', 1),
    ('Local', 2),
]
for text, mode in ARBEES:
    rbGroupThree = Radiobutton(frame, text=text, variable=rbVariable3, value=mode, bg='light blue', font=('arial', 20, 'normal'))
    rbGroupThree.pack(side='left', anchor='w')

Button(root, text='Generate Bill', bg='light blue', font=('arial', 15, 'normal'), command=calculate_bill).place(x=66, y=527)

last = Entry(root, width=80, textvariable=var4)
last.place(x=333, y=539)

root.mainloop()
