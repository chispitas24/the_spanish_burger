import tkinter as tk

from PIL import Image, ImageTk

# Constants
WIDTH = 2000
HEIGHT = 1800

home = None


def set_position(screen_name):
    """Center window in the screen

    Args:
        screen_name (Tk): name of the screen
    """
    screen_width = screen_name.winfo_screenwidth()
    screen_height = screen_name.winfo_screenheight()
    x = (screen_width / 2) - (WIDTH / 2)
    y = (screen_height / 2) - (HEIGHT / 2)
    screen_name.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, x, y))


def create_button(text, frame_name):
    """Create a button

    Args:
        text (string): text of the button
        frame_name (Frame): name of the frame
    """
    button = tk.Button(
        master=frame_name,
        text=text,
        highlightthickness=0,
        bd=0,
        font="Helvetica 30 bold",
        bg="white",
        padx=50
    )
    button.pack(side=tk.LEFT)


def create_button_image(image_name, frame_name):
    """Create a button

    Args:
        image_name (Photo image): name of the image
        frame_name (Frame): name of the frame
    """
    button = tk.Button(
        master=frame_name,
        image=image_name,
        highlightthickness=0,
        bd=0,
        font="Helvetica 30 bold",
        bg="white",
        padx=50
    )
    button.pack(side=tk.LEFT)


def create_menu():
    """Create the menu
    """
    menu_frame = tk.Frame(bg="white", pady=20)

    create_button("MENU", menu_frame)
    create_button("COUPONS", menu_frame)

    # Imagen con el logo
    photo = tk.PhotoImage(file=r"./media/logo_general.png")
    pic = photo.subsample(1, 2)
    create_button_image(pic, menu_frame)

    create_button("DELIVERY", menu_frame)
    create_button("MY ACCOUNT", menu_frame)

    photo = tk.PhotoImage(file=r"./media/carrito.png")
    pic = photo.subsample(8, 8)
    create_button_image(pic, menu_frame)

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


main()
