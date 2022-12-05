import tkinter as tk
from PIL import Image, ImageTk
from more_itertools import side_effect

# Constants

WIDTH = 1200
HEIGHT = 800

home = None

# List of products: name, price, quantity
menu_items = (["La Nicky Ñam", 9.99, 0], ["La Smoke", 12.99, 0], ["Edamami", 10.99, 0],
              ["Kevin Bacon", 11.50, 0], ["Kendall Bacon", 11.99, 0], ["La smash", 14.99, 0],
              ["Pigma", 10.99, 0], ["M-30", 9.50, 0], ["Albacete", 15.99, 0],
              ["Nachitos", 5.99, 0], ["Chicken tenders", 8.99, 0], ["Papalatas", 6.99, 0],
              ["Onion rings", 4.99, 0], ["Chilly pizza", 9.99, 0], ["Murcia pizza", 12.99, 0],
              ["Jaén Pizza", 15.99, 0], ["Water", 1.50, 0], ["Cruzcampo", 2.80, 0],
              ["Estrella", 2.80, 0], ["Coca-cola", 2.50, 0], ["Nestea", 2.50, 0],
              ["Sangría", 4, 0], ["Wine", 3.50, 0])


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
    create_button("ACCOUNT", top_bar_frame, bottom_frame)
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
        create_menu(frame)
    elif new_screen == 'COUPONS':
        create_coupons(frame)
    elif new_screen == 'HOME':
        create_home(frame)
    elif new_screen == 'DELIVERY':
        create_delivery(frame)  # TODO: CREATE DELIVERY SCREEN
    elif new_screen == 'ACCOUNT':
        create_account(frame)  # TODO: CREATE ACCOUNT SCREEN
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
        width=30,
        background="black",
        foreground="orange",
    )
    add_to_cart_button_2 = tk.Button(
        master=frame_add_to_cart,
        text="ADD TO CART",
        font="Helvetica 18 bold",
        width=30,
        background="black",
        foreground="orange",
    )
    add_to_cart_button_3 = tk.Button(
        master=frame_add_to_cart,
        text="ADD TO CART",
        font="Helvetica 18 bold",
        width=30,
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


def create_menu(frame):
    left_frame1 = tk.Frame(master=frame, background="black")
    middle_frame1 = tk.Frame(master=frame, background="black")
    right_frame1 = tk.Frame(master=frame, background="black")
    left_frame2 = tk.Frame(master=frame, background="black")
    middle_frame2 = tk.Frame(master=frame, background="black")
    right_frame2 = tk.Frame(master=frame, background="black")

    image = Image.open(r"./media/burgers.png")
    resize_image = image.resize((70, 70))
    img_logo = ImageTk.PhotoImage(resize_image)
    img_label = tk.Label(image=img_logo, master=left_frame1)
    img_label.image = img_logo
    img_label.pack()

    tk.Label(master=left_frame2,
             text="BURGERS",
             foreground="orange",
             background="black",
             font="Helvetica 25 bold",
             pady=20, ).pack(anchor="w")

    for menu_item in menu_items[0:9]:
        create_product(menu_item, left_frame1, left_frame2)

    image = Image.open(r"./media/nachos.png")
    resize_image = image.resize((70, 70))
    img_logo = ImageTk.PhotoImage(resize_image)
    img_label = tk.Label(image=img_logo, master=middle_frame1)
    img_label.image = img_logo
    img_label.pack()

    tk.Label(master=middle_frame2,
             text="STARTERS",
             foreground="orange",
             background="black",
             font="Helvetica 25 bold",
             pady=20, ).pack(anchor="w")

    for menu_item in menu_items[10:13]:
        create_product(menu_item, middle_frame1, middle_frame2)

    image = Image.open(r"./media/pizza.png")
    resize_image = image.resize((70, 70))
    img_logo = ImageTk.PhotoImage(resize_image)
    img_label = tk.Label(image=img_logo, master=middle_frame1)
    img_label.image = img_logo
    img_label.pack()

    tk.Label(master=middle_frame2,
             text="PIZZAS",
             foreground="orange",
             background="black",
             font="Helvetica 25 bold",
             pady=20, ).pack(anchor="w")

    for menu_item in menu_items[14:16]:
        create_product(menu_item, middle_frame1, middle_frame2)

    tk.Label(master=right_frame2,
             text="DRINKS",
             foreground="orange",
             background="black",
             font="Helvetica 25 bold",
             pady=20, ).pack(anchor="w")

    tk.Label(master=right_frame2,
             text="xd",
             foreground="black",
             background="black",
             font="Helvetica 25 bold",
             pady=20, ).pack()

    for menu_item in menu_items[16:23]:
        create_product(menu_item, right_frame1, right_frame2)

    left_frame1.pack(anchor="n", side=tk.LEFT)
    left_frame2.pack(anchor="n", side=tk.LEFT)
    middle_frame1.pack(anchor="n", side=tk.LEFT)
    middle_frame2.pack(anchor="n", side=tk.LEFT)
    right_frame1.pack(anchor="n", side=tk.LEFT)
    right_frame2.pack(anchor="n", side=tk.LEFT)


def create_product(product, frame_name1, frame_name2):
    button1 = tk.Button(
        master=frame_name1,
        text="+ " + product[0],
        highlightthickness=0,
        bd=0,
        font="Helvetica 18 bold",
        foreground="white",
        background="black",
        padx=50,
        command=lambda: buy_product(product)
    )
    button2 = tk.Button(
        master=frame_name2,
        text=str(product[1]) + "€",
        highlightthickness=0,
        bd=0,
        font="Helvetica 18 bold",
        foreground="orange",
        background="black",
        padx=50,
        command=lambda: buy_product(product)
    )

    button1.pack(anchor="w")
    button2.pack(anchor="w")


def buy_product(product):
    product[2] += 1


def create_coupons(frame):
    """Create coupons screen
     Args:
        frame (Frame): frame where the objects will be placed
    """
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

    kevin = tk.Label(
        image=img_kevin,
        master=frame_photos
    )
    kevin.image = img_kevin
    kevin.pack(side=tk.LEFT)
    albacete = tk.Label(
        image=img_albacete,
        master=frame_photos
    )
    albacete.image = img_albacete
    albacete.pack(padx=50, side=tk.LEFT)
    jaen = tk.Label(
        image=img_jaen,
        master=frame_photos
    )
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


def create_delivery(frame):
    label_title = tk.Label(
        master=frame,
        text="DELIVERY",
        foreground="orange",
        background="black",
        font="Helvetica 25 bold",
        pady=20
    )
    label_title.pack(side=tk.TOP)

    frame_find_us = tk.Frame(
        master=frame,
        background="black"
    )
    label_find_us = tk.Label(
        master=frame_find_us,
        text="FIND US",
        foreground="white",
        background="black",
        font="Helvetica 20 bold",
        pady=20
    )
    label_find_us.pack()

    image = Image.open(r"./media/murcia.png")
    resize_image = image.resize((550, 450))
    img_map = ImageTk.PhotoImage(resize_image)

    map = tk.Label(
        image=img_map,
        master=frame_find_us
    )
    map.image = img_map
    map.pack()

    frame_contact = tk.Frame(
        master=frame_find_us,
        background="black"
    )

    label_address = tk.Label(
        master=frame_contact,
        text="Street Los Dolores, 2000",
        foreground="white",
        background="black",
        font="Helvetica 20 bold",
        pady=20
    )
    label_address.pack(side=tk.TOP)

    image = Image.open(r"./media/phone.png")
    resize_image = image.resize((50, 50))
    img_phone = ImageTk.PhotoImage(resize_image)

    phone = tk.Label(
        image=img_phone,
        master=frame_contact,
        background="black"
    )
    phone.image = img_phone
    phone.pack(side=tk.LEFT)

    label_phone_number = tk.Label(
        master=frame_contact,
        text="(+34) 969 89 10 79",
        foreground="white",
        background="black",
        font="Helvetica 20 bold",
        pady=20
    )
    label_phone_number.pack()
    frame_contact.pack()
    frame_find_us.pack(side=tk.LEFT)

    label_rewards = tk.Frame(
        master=frame,
        background="black"
    )

    label_location = tk.Label(
        master=label_rewards,
        text="Up to 30 Km\nFree for orders higher than 20€\nEarn Spanish Coins and interchange them\nfor rewards of your favourites games",
        font="Helvetica 20 bold",
        foreground="white",
        background="black"
    )
    label_location.pack(side=tk.TOP)

    frame_image = tk.Frame(
        master=label_rewards,
        background="black"
    )

    image = Image.open(r"./media/logo_lol.png")
    resize_image = image.resize((200, 200))
    img_lol = ImageTk.PhotoImage(resize_image)

    lol = tk.Label(
        image=img_lol,
        master=frame_image
    )
    lol.image = img_lol
    lol.pack(side=tk.LEFT)

    image = Image.open(r"./media/logo_cod.png")
    resize_image = image.resize((340, 250))
    img_cod = ImageTk.PhotoImage(resize_image)

    cod = tk.Label(
        image=img_cod,
        master=frame_image
    )
    cod.image = img_cod
    cod.pack(side=tk.RIGHT)
    frame_image.pack(ipadx=60, pady=40)
    label_rewards.pack(side=tk.RIGHT, padx=200, ipady=60, ipadx=40)


def create_account(frame):
    label_title = tk.Label(
        master=frame,
        text="MY ACCOUNT",
        font="Helvetica 25 bold",
        foreground="orange",
        background="black",
        pady=20,
    )
    label_title.pack(side=tk.TOP)

    image = Image.open(r"./media/naruto.jpg")
    resize_image = image.resize((175, 250))
    img_naruto = ImageTk.PhotoImage(resize_image)

    naruto = tk.Label(
        image=img_naruto,
        master=frame
    )
    naruto.image = img_naruto
    naruto.pack(side=tk.LEFT)

    frame_personal_information = tk.Frame(
        master=frame,
        background="black"
    )

    # NAME
    frame_name = tk.Frame(
        master=frame_personal_information,
        background="black"
    )
    label_name_1 = tk.Label(
        master=frame_name,
        text="NAME: ",
        foreground="orange",
        background="black",
        font="Helvetica 18 bold",
        pady=20
    )
    label_name_1.pack(side=tk.LEFT)
    label_name_2 = tk.Label(
        master=frame_name,
        text="Pedro",
        foreground="white",
        background="black",
        font="Helvetica 18 bold",
        pady=20
    )
    label_name_2.pack(side=tk.RIGHT)
    frame_name.pack(side=tk.TOP)

    # SURNAME
    frame_surname = tk.Frame(
        master=frame_personal_information,
        background="black"
    )
    label_surname_1 = tk.Label(
        master=frame_surname,
        text="SURNAME: ",
        foreground="orange",
        background="black",
        font="Helvetica 18 bold",
        pady=20
    )
    label_surname_1.pack(side=tk.LEFT)
    label_surname_2 = tk.Label(
        master=frame_surname,
        text="Sánchez Castejón",
        foreground="white",
        background="black",
        font="Helvetica 18 bold",
        pady=20
    )
    label_surname_2.pack(side=tk.RIGHT)
    frame_surname.pack(side=tk.TOP)

    # ADDRESS
    frame_address = tk.Frame(
        master=frame_personal_information,
        background="black"
    )
    label_address_1 = tk.Label(
        master=frame_address,
        text="ADDRESS: ",
        foreground="orange",
        background="black",
        font="Helvetica 18 bold",
        pady=20
    )
    label_address_1.pack(side=tk.LEFT)
    label_address_2 = tk.Label(
        master=frame_address,
        text="Moncloa Street 49",
        foreground="white",
        background="black",
        font="Helvetica 18 bold",
        pady=20
    )
    label_address_2.pack(side=tk.RIGHT)
    frame_address.pack(side=tk.TOP)

    # BIRTHDATE
    frame_birthdate = tk.Frame(
        master=frame_personal_information,
        background="black"
    )
    label_birthdate_1 = tk.Label(
        master=frame_birthdate,
        text="BIRTHDATE: ",
        foreground="orange",
        background="black",
        font="Helvetica 18 bold",
        pady=20
    )
    label_birthdate_1.pack(side=tk.LEFT)
    label_birthdate_2 = tk.Label(
        master=frame_birthdate,
        text="28/02/1972",
        foreground="white",
        background="black",
        font="Helvetica 18 bold",
        pady=20
    )
    label_birthdate_2.pack(side=tk.RIGHT)
    frame_birthdate.pack(side=tk.TOP)

    # EMAIL
    frame_email = tk.Frame(
        master=frame_personal_information,
        background="black"
    )
    label_email_1 = tk.Label(
        master=frame_email,
        text="EMAIL: ",
        foreground="orange",
        background="black",
        font="Helvetica 18 bold",
        pady=20
    )
    label_email_1.pack(side=tk.LEFT)
    label_email_2 = tk.Label(
        master=frame_email,
        text="psc1972@gmail.com",
        foreground="white",
        background="black",
        font="Helvetica 18 bold",
        pady=20
    )
    label_email_2.pack(side=tk.RIGHT)
    frame_email.pack(side=tk.TOP)

    # PHONE
    frame_phone = tk.Frame(
        master=frame_personal_information,
        background="black"
    )
    label_phone_1 = tk.Label(
        master=frame_phone,
        text="PHONE: ",
        foreground="orange",
        background="black",
        font="Helvetica 18 bold",
        pady=20
    )
    label_phone_1.pack(side=tk.LEFT)
    label_phone_2 = tk.Label(
        master=frame_phone,
        text="(+34) 696 47 90 50",
        foreground="white",
        background="black",
        font="Helvetica 18 bold",
        pady=20
    )
    label_phone_2.pack(side=tk.RIGHT)
    frame_phone.pack(side=tk.TOP)

    # CREDIT CARD
    frame_credit_card = tk.Frame(
        master=frame_personal_information,
        background="black"
    )
    label_credit_cards_1 = tk.Label(
        master=frame_credit_card,
        text="CREDIT CARDS: ",
        foreground="orange",
        background="black",
        font="Helvetica 18 bold",
        pady=20
    )
    label_credit_cards_1.pack(side=tk.LEFT)
    label_credit_cards_2 = tk.Label(
        master=frame_credit_card,
        text="Mastercard    **** **** **** 2979\nVisa               **** **** **** 9792",
        foreground="white",
        background="black",
        font="Helvetica 18 bold",
        pady=20
    )
    label_credit_cards_2.pack(side=tk.RIGHT)
    frame_credit_card.pack(side=tk.TOP)
    frame_personal_information.pack(padx=20, side=tk.LEFT)

    frame_right_side = tk.Frame(
        master=frame,
        background="black"
    )

    label_spanish_coins = tk.Label(
        master=frame_right_side,
        text="SPANISH COINS",
        foreground="orange",
        background="black",
        font="Helvetica 30 bold",
    )
    label_spanish_coins.pack(side=tk.TOP)

    frame_coin = tk.Frame(
        master=frame_right_side,
        background="black"
    )
    label_year_coin = tk.Label(
        master=frame_coin,
        text="1492",
        font="Helvetica 35 bold",
        foreground="white",
        background="black",
    )
    label_year_coin.pack(side=tk.LEFT)
    image = Image.open(r"./media/euro.png")
    resize_image = image.resize((50, 50))
    img_coin = ImageTk.PhotoImage(resize_image)

    coin = tk.Label(
        image=img_coin,
        master=frame_coin
    )
    coin.image = img_coin
    coin.pack(side=tk.RIGHT)
    frame_coin.pack(side=tk.TOP, ipadx=40)

    frame_contact_us = tk.Frame(
        master=frame_right_side,
        background="black"
    )
    label_contact_us = tk.Label(
        master=frame_contact_us,
        text="CONTACT US",
        foreground="orange",
        background="black",
        font="Helvetica 30 bold",
    )
    label_contact_us.pack(side=tk.TOP)


    frame_phone_contact = tk.Frame(
        master=frame_contact_us,
        background="black"
    )
    image = Image.open(r"./media/phone.png")
    resize_image = image.resize((50, 50))
    img_phone = ImageTk.PhotoImage(resize_image)

    phone = tk.Label(
        image=img_phone,
        master=frame_phone_contact
    )
    phone.image = img_phone
    phone.pack(side=tk.LEFT)

    label_phone = tk.Label(
        master=frame_phone_contact,
        text="(+34) 696 89 72 55",
        font="Helvetica 20 bold",
        background="black",
        foreground="white"
    )
    label_phone.pack(side=tk.RIGHT)

    frame_phone_contact.pack(side=tk.TOP, ipadx=10, ipady=10)

    frame_gmail_contact = tk.Frame(
        master=frame_contact_us,
        background="black"
    )
    image = Image.open(r"./media/gmail.png")
    resize_image = image.resize((50, 50))
    img_gmail = ImageTk.PhotoImage(resize_image)

    gmail = tk.Label(
        image=img_gmail,
        master=frame_gmail_contact
    )
    gmail.image = img_gmail
    gmail.pack(side=tk.LEFT)

    label_gmail = tk.Label(
        master=frame_gmail_contact,
        text="info@spburger.com",
        font="Helvetica 20 bold",
        background="black",
        foreground="white"
    )
    label_gmail.pack(side=tk.RIGHT)

    frame_gmail_contact.pack(side=tk.BOTTOM, ipadx=10, ipady=10)
    frame_contact_us.pack(side=tk.BOTTOM, pady=30)

    frame_right_side.pack(side=tk.LEFT)


def create_order(frame):
    label = tk.Label(
        master=frame,
        text='Your Products',
        foreground="orange",
        background="black",
        font="Helvetica 25 bold",
    )
    label.pack(pady=30)
    total_cost = 0.0
    for product in menu_items:
        label_for = tk.Label(
            master=frame,
            text=str(product[2]) + "\tx\t" + product[0] + "\t\t" + str(product[1]) + "€",
            foreground="white",
            background="black",
            font="Helvetica 15 bold",
        )
        label_for.pack()
        if product[2] != 0:
            total_cost += product[1] * product[2]
    label2 = tk.Label(
        master=frame,
        text='Total cost: ' + str(total_cost) + "€",
        foreground="orange",
        background="black",
        font="Helvetica 25 bold",

    )
    label2.pack(pady=30)


main()
