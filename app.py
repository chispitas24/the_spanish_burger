import tkinter as tk
from tkinter import *

gui = tk.Tk()

# Global variables
WIDHT = 700
HEIGHT = 400
global screen_width
global screen_height
global x
global y


def menu_window():
    new_window = Toplevel(gui)
    new_window.geometry("750x250")
    new_window.title("Menu | The Spanish Burger")
    new_window.geometry("%dx%d+%d+%d" % (WIDHT, HEIGHT, x, y))


def menu_coupons():
    new_window = Toplevel(gui)
    new_window.geometry("750x250")
    new_window.title("Coupons | The Spanish Burger")
    new_window.geometry("%dx%d+%d+%d" % (WIDHT, HEIGHT, x, y))


def menu_delivery():
    new_window = Toplevel(gui)
    new_window.geometry("750x250")
    new_window.title("Delivery | The Spanish Burger")
    new_window.geometry("%dx%d+%d+%d" % (WIDHT, HEIGHT, x, y))


def menu_account():
    new_window = Toplevel(gui)
    new_window.geometry("750x250")
    new_window.title("Account | The Spanish Burger")
    new_window.geometry("%dx%d+%d+%d" % (WIDHT, HEIGHT, x, y))


def main():

    gui.title("Home | The Spanish Burger")

    screen_width = gui.winfo_screenwidth()
    screen_height = gui.winfo_screenheight()
    x = (screen_width / 2) - (WIDHT / 2)
    y = (screen_width / 2) - (HEIGHT / 2)
    gui.geometry("%dx%d+%d+%d" % (WIDHT, HEIGHT, x, y))
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

    # Create label
    label = tk.Label(gui, text="See more products", foreground="orange")
    label.pack()
    gui.mainloop()


main()
