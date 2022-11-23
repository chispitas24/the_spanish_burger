import tkinter as tk
from PIL import Image, ImageTk
from more_itertools import side_effect

# Constants

WIDTH = 1200
HEIGHT = 800

home = None

# List of products: name, price, quantity
menu_items = (["burger", 5.2, 0], ["pizza", 8.9, 0], ["nachos", 6.4, 0])


def set_position(screen_name):
    """Center window in the screen

    Args:
        screen_name (Tk): name of the screen
    """
    screen_width = screen_name.winfo_screenwidth()
    screen_height = screen_name.winfo_screenheight()
    x = (screen_width / 2) - (WIDTH / 2)
    y = (screen_height / 2) - (HEIGHT / 2)
    screen_name.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, 100, 100))


def create_button(text, frame_name, frame_delete):
    """Create a button

    Args:
        text (string): text of the button
        frame_name (Frame): name of the frame
        frame_delete (Frame): bottom frame to delete
    """
    button = tk.Button(
        master=frame_name,
        text=text,
        highlightthickness=0,
        bd=0,
        font="Helvetica 20 bold",
        bg="white",
        padx=50,
        command=lambda: change_screen(text, frame_delete)
    )
    button.pack(side=tk.LEFT)


def create_button_image(image, screen, frame_name, frame_delete):
    """Create a button

    Args:
        image (Photo image): name of the image
        screen (String): name of the screen that creates
        frame_name (Frame): name of the frame
        frame_delete (Frame): bottom frame to delete
    """
    button = tk.Button(
        master=frame_name,
        image=image,
        highlightthickness=0,
        bd=0,
        font="Helvetica 30 bold",
        bg="white",
        padx=50,
        command=lambda: change_screen(screen, frame_delete)
    )
    button.pack(side=tk.LEFT)


def main():
    """Main program"""
    win = tk.Tk()  # Main page
    win.title("Home | The Spanish Burger")
    win.config(background='black')

    # Set position on screen and size
    set_position(win)

    # Bottom frame, for page content
    bottom_frame = tk.Frame(padx=50, bg="black")

    # Create top navigation bar
    top_bar_frame = tk.Frame(bg="white", pady=20)

    create_button("MENU", top_bar_frame, bottom_frame)
    create_button("COUPONS", top_bar_frame, bottom_frame)
    photo = tk.PhotoImage(file=r"./media/logo_general.png")
    pic_1 = photo.subsample(1, 2)
    create_button_image(pic_1, "HOME", top_bar_frame, bottom_frame)
    create_button("DELIVERY", top_bar_frame, bottom_frame)
    create_button("MY ACCOUNT", top_bar_frame, bottom_frame)
    photo = tk.PhotoImage(file=r"./media/carrito.png")
    pic_2 = photo.subsample(8, 8)
    create_button_image(pic_2, "CART", top_bar_frame, bottom_frame)
    top_bar_frame.pack(pady=30)

    create_home(bottom_frame)

    win.mainloop()


def change_screen(new_screen, frame):
    for widget in frame.winfo_children():
        widget.destroy()
    if new_screen == 'MENU':
        for menu_item in menu_items:
            create_product(menu_item, frame)
    elif new_screen == 'COUPONS':
        create_home(frame)
    elif new_screen == 'HOME':
        create_home(frame)
    elif new_screen == 'DELIVERY':
        create_home(frame)
    elif new_screen == 'ACCOUNT':
        create_home(frame)
    elif new_screen == 'CART':
        create_order(frame)
    else:
        create_home(frame)


def create_home(frame):
    image = Image.open(r"./media/albacete.jpg")
    resize_image = image.resize((450, 450))
    img_albacete = ImageTk.PhotoImage(resize_image)

    image = Image.open(r"./media/nachos.png")
    resize_image = image.resize((450, 450))
    img_nachos = ImageTk.PhotoImage(resize_image)

    image = Image.open(r"./media/pizza.png")
    resize_image = image.resize((450, 450))
    img_pizza = ImageTk.PhotoImage(resize_image)

    albacete = tk.Label(image=img_albacete, master=frame)
    albacete.image = img_albacete
    albacete.pack(padx=50, side=tk.LEFT)
    nachos = tk.Label(image=img_nachos, master=frame)
    nachos.image = img_nachos
    nachos.pack(padx=50, side=tk.LEFT)
    pizza = tk.Label(image=img_pizza, master=frame)
    pizza.image = img_pizza
    pizza.pack(padx=50, side=tk.LEFT)

    # Create "view more" frame
    label = tk.Label(
        text="↓ VIEW MORE ↓",
        foreground="white",
        background="black",
        font="Helvetica 18 bold",
        pady=100,
    )
    label.pack(side=tk.BOTTOM)

    # Create "ADD TO CART" section
    frame_add_to_cart = tk.Frame(
        bg="black",
    )

    add_to_cart_button_1 = tk.Button(
        master=frame_add_to_cart,
        text="ADD TO CART",
        font="Helvetica 18 bold",
        width=34,
        background="black",
        foreground="orange",
    )
    add_to_cart_button_2 = tk.Button(
        master=frame_add_to_cart,
        text="ADD TO CART",
        font="Helvetica 18 bold",
        width=34,
        background="black",
        foreground="orange",
    )
    add_to_cart_button_3 = tk.Button(
        master=frame_add_to_cart,
        text="ADD TO CART",
        font="Helvetica 18 bold",
        width=34,
        background="black",
        foreground="orange",
    )
    frame_add_to_cart.pack(side=tk.BOTTOM)
    add_to_cart_button_1.pack(side=tk.LEFT)
    add_to_cart_button_2.pack(side=tk.LEFT, padx=80)
    add_to_cart_button_3.pack(side=tk.LEFT)
    frame.pack(padx=60, pady=30)

def create_product(product, frame_name):
    button = tk.Button(
        master=frame_name,
        text="+ " + product[0] + "\t\t\t" + str(product[1]) + "€",
        highlightthickness=0,
        bd=0,
        font="Helvetica 18",
        padx=50,
        command=lambda: buy_product(product)
    )
    button.pack(side=tk.BOTTOM)


def buy_product(product):
    product[2] += 1


def create_order(frame):
    tk.Label(master=frame, text='Your Products')
    total_cost = 0.0
    for product in menu_items:
        tk.Label(master=frame,
                 text=product[2] + "\tx\t" + product[0] + "\t\t" + product[1]+"€")
        total_cost += product[1]
    tk.Label(master=frame, text='Total cost: '+str(total_cost)+"€")


main()
