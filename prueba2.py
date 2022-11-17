import tkinter as tk

from PIL import Image, ImageTk

# Constants
WIDTH = 1000
HEIGHT = 400

home = None


def set_position(screen_name):
    """Center window in the screen

    Args:
        screen_name (string): name of the screen
    """
    screen_width = screen_name.winfo_screenwidth()
    screen_height = screen_name.winfo_screenheight()
    x = (screen_width / 2) - (WIDTH / 2)
    y = (screen_height / 2) - (HEIGHT / 2)
    screen_name.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, x, y))


def create_menu(screen_name):
    """Create the menu

    Args:
        screen_name (string): name of the screen
    """
    menubar = tk.Menu(screen_name)
    menubar.add_command(label="Menu")
    menubar.add_command(label="Coupons")
    menubar.add_command(label="Delivery")
    menubar.add_command(label="Account")
    menubar.add_command(label="My order")
    screen_name.config(menu=menubar)


def main():
    """Main program"""
    home = tk.Tk()  # Main page
    home.title("Home | The Spanish Burger")
    home.configure(background="black")

    # Set position on screen and size
    set_position(home)
    create_menu(home)

    label = tk.Label(
        text="↓ VIEW MORE ↓", foreground="orange", background="black", font="Helvetica 18 bold"
    )
    label.pack(side="bottom")

    home.mainloop()



main()
