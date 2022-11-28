import tkinter as tk
from PIL import Image, ImageTk
from more_itertools import side_effect

# Constants

WIDTH = 1200
HEIGHT = 800

home = None

# List of products: name, price, quantity
menu_items = (["La Nicky Ñam", 9.99, 0], ["pizza", 8.9, 0], ["nachos", 6.4, 0])


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
    bottom_frame = tk.Frame(
        padx=50,
        bg="black"
    )

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
        create_coupons(frame)  # TODO: CREATE COUPONS
    elif new_screen == 'HOME':
        create_home(frame)
    elif new_screen == 'DELIVERY':
        create_home(frame) # TODO: CREATE DELIVERY SCREEN
    elif new_screen == 'ACCOUNT':
        create_home(frame) # TODO: CREATE ACCOUNT SCREEN
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

    frame_photos = tk.Frame(
        master=frame,
        padx=50,
        pady=50,
        background="black"
    )
    frame_photos.pack(side=tk.TOP, padx=50, pady=20)

    albacete = tk.Label(image=img_albacete, master=frame_photos)
    albacete.image = img_albacete
    albacete.pack(side=tk.LEFT)
    nachos = tk.Label(image=img_nachos, master=frame_photos)
    nachos.image = img_nachos
    nachos.pack(padx=50, side=tk.LEFT)
    pizza = tk.Label(image=img_pizza, master=frame_photos)
    pizza.image = img_pizza
    pizza.pack(side=tk.LEFT)

    # Create "ADD TO CART" section
    frame_add_to_cart = tk.Frame(
        master=frame,
        padx=50,
        pady=50,
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
    add_to_cart_button_1.pack(side=tk.LEFT)
    add_to_cart_button_2.pack(side=tk.LEFT, padx=80)
    add_to_cart_button_3.pack(side=tk.LEFT)
    frame_add_to_cart.pack(side=tk.TOP)

    # Create "view more" frame
    label = tk.Label(
        master=frame,
        text="↓ VIEW MORE ↓",
        foreground="white",
        background="black",
        font="Helvetica 18 bold",
        pady=100,
    )
    label.pack(side=tk.BOTTOM)

    frame.pack(padx=60)


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

def create_coupons(frame):
    label_title = tk.Label(
        master=frame,
        text="COUPONS",
        foreground="orange",
        background="black",
        font="Helvetica 25 bold",
        pady=20,
    )
    label_title.pack(side=tk.TOP)

    image = Image.open(r"./media/kevin_bacon.jpg")
    resize_image = image.resize((450, 450))
    img_kevin = ImageTk.PhotoImage(resize_image)

    image = Image.open(r"./media/kiki_burger.jpg")
    resize_image = image.resize((450, 450))
    img_albacete = ImageTk.PhotoImage(resize_image)

    image = Image.open(r"./media/jaen_pizza.jpg")
    resize_image = image.resize((450, 450))
    img_jaen = ImageTk.PhotoImage(resize_image)

    frame_photos = tk.Frame(
        master=frame,
        padx=50,
        pady=20,
        background="black"
    )
    frame_photos.pack(side=tk.TOP, padx=50, pady=20)

    frame_prizes = tk.Frame(
        master=frame,
        background="black"
    )
    label_prize_kevin_bacon = tk.Label(
        master=frame_prizes,
        text="11'99€",
        font="Helvetica 18 bold",
        foreground="orange",
        background="black"
    )
    label_prize_albacete = tk.Label(
        master=frame_prizes,
        text="16'99€",
        font="Helvetica 18 bold",
        foreground="orange",
        background="black"
    )
    label_prize_jaen = tk.Label(
        master=frame_prizes,
        text="18'99€",
        font="Helvetica 18 bold",
        foreground="orange",
        background="black"
    )
    label_prize_kevin_bacon.pack(side=tk.LEFT)
    label_prize_albacete.pack(side=tk.LEFT, padx=425)
    label_prize_jaen.pack(side=tk.LEFT)
    frame_prizes.pack(side=tk.BOTTOM)

    kevin = tk.Label(image=img_kevin, master=frame_photos)
    kevin.image = img_kevin
    kevin.pack(side=tk.LEFT)
    albacete = tk.Label(image=img_albacete, master=frame_photos)
    albacete.image = img_albacete
    albacete.pack(padx=50, side=tk.LEFT)
    jaen = tk.Label(image=img_jaen, master=frame_photos)
    jaen.image = img_jaen
    jaen.pack(side=tk.LEFT)

    frame_text_1 = tk.Frame(
        master=frame,
        background="black"
    )
    label_kevin_bacon = tk.Label(
        master=frame_text_1,
        text="KEVIN BACON\n+\nCRUZCAMPO\n",
        font="Helvetica 18 bold",
        foreground="white",
        background="black"
    )
    label_albacete = tk.Label(
        master=frame_text_1,
        text="ALBACETE\n+\nSANGRÍA\n",
        font="Helvetica 18 bold",
        foreground="white",
        background="black"
    )
    label_jaen = tk.Label(
        master=frame_text_1,
        text="JAÉN PIZZA\n+\nNACHITOS\n",
        font="Helvetica 18 bold",
        foreground="white",
        background="black"
    )
    label_kevin_bacon.pack(side=tk.LEFT)
    label_albacete.pack(side=tk.LEFT, padx=350)
    label_jaen.pack(side=tk.LEFT)
    frame_text_1.pack(side=tk.BOTTOM)




def create_order(frame):
    label = tk.Label(master=frame, text='Your Products', foreground="white").pack()
    total_cost = 0.0
    for product in menu_items:
        label_for = tk.Label(master=frame,
                 text=str(product[2]) + "\tx\t" + product[0] + "\t\t" + str(product[1]) + "€").pack()
        total_cost += product[1]
    label2 = tk.Label(master=frame, text='Total cost: ' + str(total_cost) + "€").pack()



main()
