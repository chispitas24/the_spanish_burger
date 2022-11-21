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


def main():
    """Main program"""
    win = tk.Tk()  # Main page
    win.title("Home | The Spanish Burger")
    image = PhotoImage(file = "./media/wa")
    win.configure(background="black")

    # Set position on screen and size
    set_position(win)

    # Create menu
    menu_frame = tk.Frame(bg="white", pady=20)
    create_button("HOME", menu_frame)
    create_button("COUPONS", menu_frame)
    photo = tk.PhotoImage(file=r"./media/logo_general.png")
    pic_1 = photo.subsample(1, 2)
    create_button_image(pic_1, menu_frame)
    create_button("DELIVERY", menu_frame)
    create_button("MY ACCOUNT", menu_frame)
    photo = tk.PhotoImage(file=r"./media/carrito.png")
    pic_2 = photo.subsample(8, 8)
    create_button_image(pic_2, menu_frame)
    menu_frame.pack(pady=30)

    image = Image.open(r"./media/albacete.jpg")
    resize_image = image.resize((450, 450))
    img_albacete = ImageTk.PhotoImage(resize_image)

    image = Image.open(r"./media/nachos.png")
    resize_image = image.resize((450, 450))
    img_nachos = ImageTk.PhotoImage(resize_image)

    image = Image.open(r"./media/pizza.png")
    resize_image = image.resize((450, 450))
    img_pizza = ImageTk.PhotoImage(resize_image)

    photo_frame = tk.Frame(padx=50, bg="black")
    albacete = tk.Label(image=img_albacete, master=photo_frame)
    albacete.image = img_albacete
    albacete.pack(padx=50, side=tk.LEFT)
    nachos = tk.Label(image=img_nachos, master=photo_frame)
    nachos.image = img_nachos
    nachos.pack(padx=50, side=tk.LEFT)
    pizza = tk.Label(image=img_pizza, master=photo_frame)
    pizza.image = img_pizza
    pizza.pack(padx=50, side=tk.LEFT)
    photo_frame.pack(padx=50, pady=30)





    # Create main frame
    label = tk.Label(
        text="↓ VIEW MORE ↓", foreground="orange", background="black", font="Helvetica 18 bold"
    )
    label.pack(side="bottom")

    win.mainloop()


main()
