import tkinter
from tkinter import *

window = Tk()
window.geometry("1000x500")
window.config(bg = "#FED99B")
window.resizable(False, False)
window.title("Restaarant Menu")

lbl = Label(window, text = "Restaurant Management System", font = ("Times New Roman", 30), bg = "#FED99B", fg = "#000000").pack(pady = 10)



frame = Frame(window, bg = "#6EEB83", width = "300", height = "370")
frame.place(x = 30, y = 110)

fr1 = Frame(window, bg = "#00A5CF",width = "300", height = "370")
fr1.place(x = 350, y = 110)

fr2 = Frame(window, bg = "#CFCFCD", width = "300", height = "370")
fr2.place(x = 670, y = 110)

# Labels for frame1
Label(frame, text = "Menu", font = ("Times New Roman", 30, "bold"), bg = "#6EEB83", fg = "black").place(x = 20, y = 60 )


Label(frame, text = "Pizza----------700", font = ("Times New Roman", 25),bg = "#6EEB83", fg = "black").place(x = 10, y = 100)
Label(frame, text = "Coffee---------200", font = ("Times New Roman",25), bg = "#6EEB83", fg = "black").place(x = 10,y = 140)
Label(frame, text = "Burger---------250", font = ("Times New Roman",25), bg = "#6EEB83", fg = "black").place(x = 10, y = 180)

# Buttons and functions for frame2

lb1_pizza = Label(fr1, text = "Pizza", font = ("Times New Roman",25), bg = "#00A5CF", fg = "Black")
lb1_pizza.place(x = 20, y = 50)

lb1_coffee = Label(fr1, text = "Coffee", font = ("Times New Roman",25), bg = "#00A5CF", fg = "Black")
lb1_coffee.place(x = 20, y = 100)

lb1_burger = Label(fr1, text = "Burger", font = ("Times New Roman",25), bg = "#00A5CF", fg = "Black")
lb1_burger.place(x = 20, y = 150)

# Entry Boxes for frame2

pizza = StringVar()
Coffee = StringVar()
Burger = StringVar()
total_bill = StringVar()

entry_pizza = Entry(fr1, textvariable = pizza, bg = "#00A5CF", font = ("times 25 bold"), width = 10, fg = "Black")
entry_pizza.place(x = 100, y = 50)

entry_coffee = Entry(fr1, textvariable = Coffee, bg = "#00A5CF", font = ("times 25 bold"), width = 10, fg = "Black")
entry_coffee.place(x = 100, y = 100)

entry_burger = Entry(fr1, textvariable = Burger, bg = "#00A5CF", font = ("times 25 bold"), width = 10, fg = "Black")
entry_burger.place(x = 100, y = 150)


def calculate():
    try:
        a1 = int(pizza.get())
    except:
        a1 = 0 
    try:
        a2 = int(Coffee.get())
    except:
        a2 = 0
    try:
        a3 = int(Burger.get())
    except:
        a3 = 0
    a1 = 700*a1
    a2 = 200*a2
    a3 = 250*a3

    lbl_total = Label(fr2, text = "Total Bill:", font = ("times new roman", 25 ,"bold"), fg = "black", bg = "#CFCFCD")
    lbl_total.place(x = 90, y = 100)
    global lbl2_total
    lbl2_total = Label(fr2, text = str(a1+a2+a3), font = ("times new roman", 25, "bold"), fg = "black", bg = "#CFCFCD")
    lbl2_total.place(x = 90, y = 200)




def Reset():
    entry_pizza.delete(0,END)
    entry_coffee.delete(0,END)
    entry_burger.delete(0,END)
    lbl2_total.configure(text = "")
    

btn = Button(fr1, text = "Calculate", font = ("times 25"),bg = "white", fg = "black",command = calculate)
btn.place(x = 120, y = 200)


btn_reset = Button(fr1, text = "Reset", font = ("times 25"),bg = "white", fg = "black",command = Reset)
btn_reset.place(x = 20, y = 200)


Label(fr2, text = "Bill",font = ("times 25"), bg = "#CFCFCD", fg = "Black").place(x = 125 , y = 30)

Label(fr1, text = "Enter the amount of dishes", bg = "#00A5CF", fg = "black", font = ("times 25")).place(x = 18, y = 10)

window.mainloop()  # main loop
