from tkinter import *

gui = Tk()
width = 700
height = 400
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)


def menu_window():
    new_window = Toplevel(gui)
    new_window.geometry("750x250")
    new_window.title("Menu | The Spanish Burger")
    new_window.geometry("%dx%d+%d+%d" % (width, height, x, y))


def menu_coupons():
    new_window = Toplevel(gui)
    new_window.geometry("750x250")
    new_window.title("Coupons | The Spanish Burger")
    new_window.geometry("%dx%d+%d+%d" % (width, height, x, y))


def menu_delivery():
    new_window = Toplevel(gui)
    new_window.geometry("750x250")
    new_window.title("Delivery | The Spanish Burger")
    new_window.geometry("%dx%d+%d+%d" % (width, height, x, y))


def menu_account():
    new_window = Toplevel(gui)
    new_window.geometry("750x250")
    new_window.title("Account | The Spanish Burger")
    new_window.geometry("%dx%d+%d+%d" % (width, height, x, y))


gui.title("Home | The Spanish Burger")


gui.geometry("%dx%d+%d+%d" % (width, height, x, y))

# Creating Menubar
menubar = Menu(gui)

# Creating labels for menu
menubar.add_command(label="Menu", command=menu_window)
menubar.add_command(label="Coupons", command=menu_coupons)
menubar.add_command(label="Delivery", command=menu_delivery)
menubar.add_command(label="Account", command=menu_account)
menubar.add_command(label="My order")

# display Menu
gui.config(menu=menubar)

gui.mainloop()
