import tkinter as tk

from PIL import Image, ImageTk

# Constants
WIDTH = 2000
HEIGHT = 1800

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


def create_menu():
    """Create the menu
    """
    menu_frame = tk.Frame(bg="white", pady=20)

    menu_button = tk.Button(
        master=menu_frame,
        text="MENU",
        highlightthickness=0,
        bd=0,
        font="Helvetica 30 bold",
        bg="white",
        padx=50
    )
    menu_button.pack(side=tk.LEFT)

    coupons_button = tk.Button(
        master=menu_frame,
        text="COUPONS",
        highlightthickness=0,
        bd=0,
        font="Helvetica 30 bold",
        bg="white",
        padx=50

    )
    coupons_button.pack(side=tk.LEFT)

    # Imagen con el logo
    photo = tk.PhotoImage(file=r"./media/logo_general.png")
    photoimage_1 = photo.subsample(1, 2)

    mainmenu_button = tk.Button(
        master=menu_frame,
        image=photoimage_1,
        highlightthickness=0,
        bd=0,
        font="Helvetica 30 bold",
        bg="white",
        padx=50
    )
    mainmenu_button.pack(side=tk.LEFT)

    delivery_button = tk.Button(
        master=menu_frame,
        text="DELIVERY",
        highlightthickness=0,
        bd=0,
        font="Helvetica 30 bold",
        bg="white",
        padx=50
    )
    delivery_button.pack(side=tk.LEFT)

    account_button = tk.Button(
        master=menu_frame,
        text="MY ACCOUNT",
        highlightthickness=0,
        bd=0,
        font="Helvetica 30 bold",
        bg="white",
        padx=50
    )
    account_button.pack(side=tk.LEFT)

    photo = tk.PhotoImage(file=r"./media/carrito.png")
    photoimage_2 = photo.subsample(8, 8)
    order_button = tk.Button(
        master=menu_frame,
        image=photoimage_2,
        highlightthickness=0,
        bd=0,
        font="Helvetica 30 bold",
        bg="white",
        padx=50
    )
    order_button.pack(side=tk.LEFT)

    menu_frame.pack()


def main():
    """Main program"""
    home = tk.Tk()  # Main page
    home.title("Home | The Spanish Burger")
    home.configure(background="black")

    # Set position on screen and size
    set_position(home)
    create_menu()
    label = tk.Label(
        text="↓ VIEW MORE ↓", foreground="orange", background="black", font="Helvetica 18 bold"
    )
    label.pack(side="bottom")

    home.mainloop()

"""
    menu_frame = tk.Frame(bg="white", pady=20)

    menu_button = tk.Button(
        master=menu_frame,
        text="MENU",
        highlightthickness=0,
        bd=0,
        font="Helvetica 30 bold",
        bg="white",
        padx=50
    )
    menu_button.pack(side=tk.LEFT)

    coupons_button = tk.Button(
        master=menu_frame,
        text="COUPONS",
        highlightthickness=0,
        bd=0,
        font="Helvetica 30 bold",
        bg="white",
        padx=50

    )
    coupons_button.pack(side=tk.LEFT)

    # Imagen con el logo
    photo = tk.PhotoImage(file = r"./media/logo_general.png")
    photoimage_1 = photo.subsample(1, 2)

    mainmenu_button = tk.Button(
        master=menu_frame,
        image=photoimage_1,
        highlightthickness=0,
        bd=0,
        font="Helvetica 30 bold",
        bg="white",
        padx=50
    )
    mainmenu_button.pack(side=tk.LEFT)

    delivery_button = tk.Button(
        master=menu_frame,
        text="DELIVERY",
        highlightthickness=0,
        bd=0,
        font="Helvetica 30 bold",
        bg="white",
        padx=50
    )
    delivery_button.pack(side=tk.LEFT)

    account_button = tk.Button(
        master=menu_frame,
        text="MY ACCOUNT",
        highlightthickness=0,
        bd=0,
        font="Helvetica 30 bold",
        bg="white",
        padx=50
    )
    account_button.pack(side=tk.LEFT)

    photo = tk.PhotoImage(file=r"./media/carrito.png")
    photoimage_2 = photo.subsample(8, 8)
    order_button = tk.Button(
        master=menu_frame,
        image=photoimage_2,
        highlightthickness=0,
        bd=0,
        font="Helvetica 30 bold",
        bg="white",
        padx=50
    )
    order_button.pack(side=tk.LEFT)

    menu_frame.pack()
"""
main()
