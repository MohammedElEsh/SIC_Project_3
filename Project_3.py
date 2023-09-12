import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json





def destroy_pg(pg_name):
    pg_name.destroy()


def loginPage():

    def checkUserAccount():
        user_email = userEmail.get().lower().strip()
        user_password = userPassword.get().strip()

        print(user_email)
        print(user_password)

        file = open('Project_3_json.json', 'r')
        all_data = json.load(file)
        file.close()

        for data in all_data:
            if user_email == data['mail'] and user_password == data['Password']:
                print(data['name'])

                if user_email == "admin@gmail.com" and user_password == "admin123":
                    adminPage()
                else:
                    destroy_pg(loginPage)
                    homePage()

            # else:
            #     messagebox.showwarning("Alert!", "Wrong email or password")
            #     userEmail.delete(0, 'end')
            #     userPassword.delete(0, 'end')

    loginPage = tk.Tk()
    loginPage.title("Login Page")
    loginPage.geometry("500x500")

    userLogin_label = tk.Label(
        loginPage, text="Login Here", font="Impact 35 bold", fg="#6162FF")
    userLogin_label.place(x=90, y=100)

    userEmail_label = tk.Label(loginPage, text="Email", font="Arial 15 bold")
    userEmail_label.place(x=90, y=180)

    userEmail = tk.Entry(loginPage, font="Arial 12")
    userEmail.place(x=90, y=210)

    userPassword_label = tk.Label(
        loginPage, text="Password", font="Arial 15 bold")
    userPassword_label.place(x=90, y=280)

    userPassword = tk.Entry(loginPage, font="Arial 12", show="*")
    userPassword.place(x=90, y=310)

    login_button = tk.Button(loginPage, text='Login  >>', font="Arial 12 bold",
                             fg="white", bg="#6162FF", command=checkUserAccount)
    login_button.place(x=90, y=340)

    userRegister_label = tk.Label(
        loginPage, text="Don't have an account!", font="Arial 10 bold", fg="red")
    userRegister_label.place(x=90, y=400)
    register_button = tk.Button(loginPage, text='Register  >>',
                                font="Arial 12 bold", fg="white", bg="#6162FF", command=registerPage)
    register_button.place(x=90, y=430)

    loginPage.mainloop()


def registerPage():

    def on_selection_change(event):
        city = cities.get()
        print(f"You selected: {city}")

    def store_in_db():

        userData = {"name": userName.get(), "phone": userPhone.get(), "mail": userMail.get(),
                    "Governorate": cities.get(), "Gender": userGender.get(),
                    "Age": userAge.get(),
                    "Password": userPass.get(),
                    "National ID": userNationalID.get()}

        # All_List_In_store = loadData()
        file = open('Project_3_json.json', 'r')
        All_List_In_store = json.load(file)

        All_List_In_store.append(userData)
        print("Done!")

        file = open("Project_3_json.json", "w")
        json.dump(All_List_In_store, file, indent=2)
        file.close()

    registerPage = tk.Tk()
    registerPage.title("register page")
    registerPage.geometry("500x700")

    userRegister_lable = tk.Label(
        registerPage, text="Register Here", font="Impact 35 bold", fg="#6162FF")
    userRegister_lable.place(x=90, y=40)

    userName_lable = tk.Label(registerPage, text="Name", font="Arial 10 bold")
    userName_lable.place(x=90, y=120)

    userName = tk.Entry(registerPage, font="arial 12")
    userName.place(x=90, y=140)

    userPhone_lable = tk.Label(
        registerPage, text="Phone number", font="Arial 10 bold")
    userPhone_lable.place(x=90, y=180)

    userPhone = tk.Entry(registerPage, font="arial 12")
    userPhone.place(x=90, y=200)

    userMail_lable = tk.Label(registerPage, text="Email", font="Arial 10 bold")
    userMail_lable.place(x=90, y=240)

    userMail = tk.Entry(registerPage, font="arial 12")
    userMail.place(x=90, y=260)

    userGovernnorate_lable = tk.Label(
        registerPage, text="Governorate", font="Arial 10 bold")
    userGovernnorate_lable.place(x=90, y=300)

    cities = tk.StringVar(registerPage)
    cities.set("cities")

    options = [
        "Alexandria", "Aswan", "Asyut", "Beheira", "Beni Suef", "Cairo", "Dakahlia", "Damietta", "Faiyum",
        "Gharbia", "Giza", "Ismailia", "Kafr El Sheikh", "Luxor", "Matrouh", "Minya", "Monufia", "New Valley",
        "North Sinai", "Port Said", "Qalyubia", "Qena", "Red Sea", "Sharqia", "Sohag", "South Sinai", "Suez"]

    cities_menu = ttk.Combobox(
        registerPage, textvariable=cities, values=options)
    cities_menu.bind("<<ComboboxSelected>>", on_selection_change)
    cities_menu.place(x=90, y=320)

    userGender_lable = tk.Label(
        registerPage, text="Gender", font="Arial 10 bold")
    userGender_lable.place(x=90, y=360)

    userGender = tk.Entry(registerPage, font="arial 12")
    userGender.place(x=90, y=380)

    userAge_lable = tk.Label(registerPage, text="age", font="Arial 10 bold")
    userAge_lable.place(x=90, y=420)

    userAge = tk.Entry(registerPage, font="arial 12")
    userAge.place(x=90, y=440)

    userPass_lable = tk.Label(
        registerPage, text="Password", font="Arial 10 bold")
    userPass_lable.place(x=90, y=480)

    userPass = tk.Entry(registerPage, font="arial 12")
    userPass.place(x=90, y=500)
    userNationalID_lable = tk.Label(
        registerPage, text="National ID", font="Arial 10 bold")
    userNationalID_lable.place(x=90, y=540)

    userNationalID = tk.Entry(registerPage, font="arial 12")
    userNationalID.place(x=90, y=560)

    register_button = tk.Button(registerPage, text='Register  >>',
                                font="head 12 bold", fg="white", bg="#6162FF", command=store_in_db)
    register_button.place(x=90, y=600)

    registerPage.mainloop()


def adminPage():
    admin_pg = tk.Tk()
    admin_pg.geometry("500x500")
    admin_pg.title("Administrator")

    def button_clicked(button_text):

        destroy_pg(admin_pg)

        if button_text == "Add Items":
            open_add_pg()
        elif button_text == "Update Items":
            open_update_pg()
        elif button_text == "Make Discount":
            open_discount_pg()

    def back_to_adminPage(pg_name):
        destroy_pg(pg_name)
        adminPage()



    buttonFrame = tk.Frame(admin_pg)
    buttonFrame.columnconfigure(0, weight=1)

    btn1 = tk.Button(buttonFrame, text="Add Items", width=10,
                     height=10, command=lambda: button_clicked("Add Items"))
    btn1.grid(row=0, sticky=tk.W + tk.E)

    btn2 = tk.Button(buttonFrame, text="Update Items", width=10,
                     height=10, command=lambda: button_clicked("Update Items"))
    btn2.grid(row=1, sticky=tk.W + tk.E)

    btn3 = tk.Button(buttonFrame, text="Make Discount", width=10,
                     height=12, command=lambda: button_clicked("Make Discount"))
    btn3.grid(row=2, sticky=tk.W + tk.E)

    buttonFrame.pack(fill="x")

    def open_add_pg():
        add_pg = tk.Tk()
        add_pg.geometry("500x500")
        add_pg.title("Add Items")

        back_button = tk.Button(add_pg, text="Back", command= lambda: back_to_adminPage(add_pg))
        back_button.place(x= 10, y= 10)


        def on_selection_change(event):
            ctg = ctgs.get()
            print(f"You selected: {ctg}")

        def add_item(ctg):

            name = name_Box.get()
            price = price_Box.get()
            brand = brand_Box.get()
            year = year_Box.get()

            if ctg == "HomeAppliances":
                HomeAppliances.append(Item(ctg, name, price, brand, year))
            elif ctg == "Electronics":
                Electronics.append(Item(ctg, name, price, brand, year))
            elif ctg == "Fashion":
                Fashion.append(Item(ctg, name, price, brand, year))
            elif ctg == "Books":
                Books.append(Item(ctg, name, price, brand, year))
            elif ctg == "Sports":
                Sports.append(Item(ctg, name, price, brand, year))

            print("Item added in", ctg)



        ctgs = tk.StringVar(add_pg)
        ctgs.set("Categories")

        options = ["HomeAppliances", "Electronics",
                   "Fashion", "Books", "Sports"]

        ctgs_menu = ttk.Combobox(add_pg, textvariable=ctgs, values=options)
        ctgs_menu.bind("<<ComboboxSelected>>", on_selection_change)
        ctgs_menu.pack()

        name_label = tk.Label(add_pg, text="Enter item name:")
        name_label.pack(pady=5)

        name_Box = tk.Entry(add_pg)
        name_Box.pack()

        price_label = tk.Label(add_pg, text="Enter item price:")
        price_label.pack(pady=5)

        price_Box = tk.Entry(add_pg)
        price_Box.pack()

        brand_label = tk.Label(add_pg, text="Enter item brand:")
        brand_label.pack(pady=5)

        brand_Box = tk.Entry(add_pg)
        brand_Box.pack()

        year_label = tk.Label(add_pg, text="Enter item year:")
        year_label.pack(pady=5)

        year_Box = tk.Entry(add_pg)
        year_Box.pack()

        add_button = tk.Button(add_pg, text="Add", command= lambda: add_item(ctgs.get()))
        add_button.pack(pady=10)

        add_pg.mainloop()

    def open_update_pg():
        update_pg = tk.Tk()
        update_pg.geometry("500x500")
        update_pg.title("Update Items")

        back_button = tk.Button(update_pg, text="Back", command= lambda: back_to_adminPage(update_pg))
        back_button.place(x= 10, y= 10)

        update_pg.mainloop()

    def open_discount_pg():
        discount_pg = tk.Tk()
        discount_pg.geometry("500x500")
        discount_pg.title("Make Discount")


        back_button = tk.Button(discount_pg, text="Back", command= lambda: back_to_adminPage(discount_pg))
        back_button.place(x= 10, y= 10)
        discount_pg.mainloop()

    admin_pg.mainloop()


def homePage():
    ctg_pg = tk.Tk()
    ctg_pg.geometry("500x750")
    ctg_pg.title("Categories")



    def items_quick_sort_price(list, ctg):
        if len(list) == 1 or len(list) == 0:
            return list
        lift = []
        right = []
        pivot = list[0]['price']
        pivotList = list[0]
        for i in range(1, len(list)):
            if list[i]['price'] <= pivot:
                lift.append(list[i])
            else:
                right.append(list[i])

        sorted_items = items_quick_sort_price(lift) + [pivotList] + items_quick_sort_price(right)
        print('After sorting ---->** ',sorted_items)  
        return sorted_items
    

     

    def searchItem(items, target, ctg):
        ctg.destroy()
        search_pg = tk.Tk()
        search_pg.geometry("500x500")
        search_pg.title("HomeAppliances")

        back_button = tk.Button(search_pg, text="Back", command=lambda: back_to_homePage(search_pg))
        back_button.place(x=10, y=10)
        search = tk.Entry(search_pg, font="Arial 12")
        search.place(x=330, y=30)

        searchButton = tk.Button(search_pg, text="Search",command=lambda: searchItem(items, search.get(), search_pg))
        searchButton.place(x=330, y=50)


        i = 0
        lift = 0
        right = len(items) - 1
        target =target.lower()
        targetlength = len(target)
        while lift <= right:
            i += 1
            mid = (right + lift) // 2
            print((items[mid].name)[0:targetlength])

            if ((items[mid].name)[0:targetlength]).lower() == target:
                item_searched_of = vars(items[mid])
                print('Steps:', i, vars(items[mid]))
                break

            elif ((items[mid].name)[0:targetlength]).lower() < target:
                lift = mid + 1
            else:
                right = mid - 1


        frame = tk.LabelFrame(search_pg, text="Item Details")
        frame.pack(pady=5)

        name_label = tk.Label(frame, text=f"Name: {item_searched_of['name']}")
        name_label.pack(pady=5)

        price_label = tk.Label(frame, text=f"Price: {item_searched_of['price']}")
        price_label.pack(pady=5)

        brand_label = tk.Label(frame, text=f"Brand: {item_searched_of['brand']}")
        brand_label.pack(pady=5)

        year_label = tk.Label(frame, text=f"Model Year: {item_searched_of['year']}")
        year_label.pack(pady=5)

        button = tk.Button(frame, text="Add to Cart",command=lambda: add_to_cart_in_search(item_searched_of, myCart))
        button.pack(pady=10)

        search_pg.mainloop()

    def back_to_homePage(pg_name):
        destroy_pg(pg_name)
        homePage()

    def add_to_cart(item, myCart):

        global total_price
        total_price += item.price

        messagebox.showinfo("Add to Cart", f"You added {item.name} to your cart with ${item.price} total price now is ${total_price}")
        myCart.append(item)

        # print(myCart)
        print(total_price)

    
    def add_to_cart_in_search(item, myCart):

        global total_price
        total_price += item['price']

        messagebox.showinfo("Add to Cart", f"You added {item['name']} to your cart with ${item['price']} total price now is ${total_price}")
        myCart.append(item)

        # print(myCart)
        print(total_price)

    def button_clicked(button_text, ctg_pg):
        destroy_pg(ctg_pg)

        if button_text == "HomeAppliances":
            open_ctg1(HomeAppliances)
        elif button_text == "Electronics":
            open_ctg2(Electronics)
        elif button_text == "Fashion":
            open_ctg3(Fashion)
        elif button_text == "Books":
            open_ctg4(Books)
        elif button_text == "Sports":
            open_ctg5(Sports)



    label = tk.Label(ctg_pg, text="Welcome Back!",font="Arial 12 bold")
    label.pack()

    label = tk.Label(ctg_pg, text="Our Store Has ...",font="Arial 12 bold")
    label.pack()

    buttonFrame = tk.Frame(ctg_pg)
    buttonFrame.columnconfigure(0, weight=1)

    btn1 = tk.Button(buttonFrame, text="HomeAppliances", width=10,height=5,font="Head 14 bold",bg= "#6162FF",fg= "White", command=lambda: button_clicked("HomeAppliances", ctg_pg))
    btn1.grid(row=0, sticky=tk.W + tk.E)

    btn2 = tk.Button(buttonFrame, text="Electronics", width=10,height=6,font="Head 14 bold",bg= "#6162FF",fg= "White", command=lambda: button_clicked("Electronics", ctg_pg))
    btn2.grid(row=1, sticky=tk.W + tk.E)

    btn3 = tk.Button(buttonFrame, text="Fashion", width=10,height=5,font="Head 14 bold",bg= "#6162FF",fg= "White", command=lambda: button_clicked("Fashion", ctg_pg))
    btn3.grid(row=2, sticky=tk.W + tk.E)

    btn4 = tk.Button(buttonFrame, text="Books", width=10,height=6,font="Head 14 bold",bg= "#6162FF",fg= "White", command=lambda: button_clicked("Books", ctg_pg))
    btn4.grid(row=3, sticky=tk.W + tk.E)

    btn5 = tk.Button(buttonFrame, text="Sports", width=10, height=5,font="Head 14 bold",bg= "#6162FF",fg= "White", command=lambda: button_clicked("Sports", ctg_pg))
    btn5.grid(row=4, sticky=tk.W + tk.E)

    buttonFrame.pack(fill="x")

    def open_ctg1(list):
        ctg1 = tk.Tk()
        ctg1.geometry("500x500")
        ctg1.title("HomeAppliances")

        back_button = tk.Button(ctg1, text="Back", command=lambda: back_to_homePage(ctg1))
        back_button.place(x=10, y=10)

        search = tk.Entry(ctg1,font= "Arial 12")
        search.place(x=250,y=30)

 

        sort = tk.Button(ctg1, text="Sort price low to high", command=lambda: items_quick_sort_price(list, ctg1))
        sort.place(x=10, y=40)

        list = [
            Item("HomeAppliances", "Microwave Oven", 199, "Panasonic", 2023),
            Item("HomeAppliances", "Microwave Oven", 199, "Panasonic", 2023),
            Item("HomeAppliances", "Refrigerator", 999, "Samsung", 2022),
            Item("HomeAppliances", "Refrigerator", 999, "Samsung", 2022),
            Item("HomeAppliances", "Washing Machine", 699, "LG", 2021),
            Item("HomeAppliances", "Washing Machine", 699, "LG", 2021),
        ]



        searchButton=tk.Button(ctg1, text="Search",fg="white", bg="#6162FF", command=lambda: searchItem(list,search.get(),ctg1))
        searchButton.place(x=250,y=50)
        # global HomeAppliances

        i = 20
        j = 100
        for item in list:

            frame = tk.LabelFrame(ctg1, text="Item Details",fg="white", bg="#6162FF")
            frame.place(x= i,y= j)
            i+= 150
            if i ==470:
                i= 20
                j+=200

            name_label = tk.Label(frame, text=f"Name: {item.name}")
            name_label.pack(pady=3)

            price_label = tk.Label(frame, text=f"Price: {item.price}")
            price_label.pack(pady=3)

            brand_label = tk.Label(frame, text=f"Brand: {item.brand}")
            brand_label.pack(pady=3)

            year_label = tk.Label(frame, text=f"Model Year: {item.year}")
            year_label.pack(pady=3)

            button = tk.Button(frame, text="Add to Cart",fg="REd", bg="Black",
                               command=lambda: add_to_cart(item, myCart))
            button.pack(pady=3)

        ctg1.mainloop()

    def open_ctg2(list):

        ctg2 = tk.Tk()
        ctg2.geometry("500x500")
        ctg2.title("Electronics")

        back_button = tk.Button(ctg2, text="Back", command=lambda: back_to_homePage(ctg2))
        back_button.place(x=10, y=10)

        search = tk.Entry(ctg2, font="Arial 12")
        search.place(x=250, y=30)


     

        sort = tk.Button(ctg2, text="Sort price low to high",command=lambda: items_quick_sort_price(list, ctg2))
        sort.place(x=10, y=40)



        # global Electronics
        list = [
            Item("Electronics", "Camera", 599, "Nikon", 2023),
            Item("Electronics", "Gaming Console", 399, "Microsoft", 2021),
            Item("Electronics", "Headphones", 99, "Bose", 2023),
            Item("Electronics", "Laptop", 1499, "Dell", 2021),
            Item("Electronics", "Smart TV", 999, "Sony", 2022),
            Item("Electronics", "Smartphone", 699, "Apple", 2022)
        ]

        searchButton = tk.Button(ctg2, text="Search", fg="white", bg="#6162FF",command=lambda: searchItem(list, search.get(), ctg2))
        searchButton.place(x=250, y=50)
        i=20
        j=100
        for item in list:
            frame = tk.LabelFrame(ctg2, text="Item Details",fg="white", bg="#6162FF")
            frame.place(x=i, y=j)
            i += 150
            if i == 470:
                i = 20
                j += 200

            name_label = tk.Label(frame, text=f"Name: {item.name}")
            name_label.pack(pady=5)

            price_label = tk.Label(frame, text=f"Price: {item.price}")
            price_label.pack(pady=5)

            brand_label = tk.Label(frame, text=f"Brand: {item.brand}")
            brand_label.pack(pady=5)

            year_label = tk.Label(frame, text=f"Model Year: {item.year}")
            year_label.pack(pady=5)

            button = tk.Button(frame, text="Add to Cart",fg="REd", bg="Black",
                               command=lambda: add_to_cart(item, myCart))
            button.pack(pady=10)

        ctg2.mainloop()

    def open_ctg3(list):

        ctg3 = tk.Tk()
        ctg3.geometry("500x500")
        ctg3.title("Fashion")

        back_button = tk.Button(
            ctg3, text="Back", command=lambda: back_to_homePage(ctg3))
        back_button.place(x=10, y=10)

        search = tk.Entry(ctg3, font="Arial 12")
        search.place(x=250, y=30)


        sort = tk.Button(ctg3, text="Sort price low to high",command=lambda: items_quick_sort_price(list, ctg3))
        sort.place(x=10, y=40)



        # global Fashion
        list = [
            Item("Fashion", "Dress", 79, "Zara", 2023),
            Item("Fashion", "Handbag", 149, "Michael Kors", 2021),
            Item("Fashion", "Jeans", 59, "Levi's", 2021),
            Item("Fashion", "Sneakers", 99, "Adidas", 2022),
            Item("Fashion", "T-Shirt", 29, "Nike", 2022),
            Item("Fashion", "Watch", 199, "Fossil", 2023)
        ]

        searchButton = tk.Button(ctg3, text="Search", fg="white", bg="#6162FF",
                                 command=lambda: searchItem(list, search.get(), ctg3))
        searchButton.place(x=250, y=50)
        i=20
        j=100
        for item in list:
            frame = tk.LabelFrame(ctg3, text="Item Details",fg="white", bg="#6162FF")
            frame.place(x=i, y=j)
            i += 150
            if i == 470:
                i = 20
                j += 200

            name_label = tk.Label(frame, text=f"Name: {item.name}")
            name_label.pack(pady=5)

            price_label = tk.Label(frame, text=f"Price: {item.price}")
            price_label.pack(pady=5)

            brand_label = tk.Label(frame, text=f"Brand: {item.brand}")
            brand_label.pack(pady=5)

            year_label = tk.Label(frame, text=f"Model Year: {item.year}")
            year_label.pack(pady=5)

            button = tk.Button(frame, text="Add to Cart",fg="REd", bg="Black",
                               command=lambda: add_to_cart(item, myCart))
            button.pack(pady=10)

        ctg3.mainloop()

    def open_ctg4(list):

        ctg4 = tk.Tk()
        ctg4.geometry("700x500")
        ctg4.title("Books")

        back_button = tk.Button(
            ctg4, text="Back", command=lambda: back_to_homePage(ctg4))
        back_button.place(x=10, y=10)

        search = tk.Entry(ctg4, font="Arial 12")
        search.place(x=250, y=30)




        sort = tk.Button(ctg4, text="Sort price low to high",command=lambda: items_quick_sort_price(list, ctg4))
        sort.place(x=10, y=40)





        # global Books
        list = [
            Item("Books", "George Orwell", 8, "1948", 1949),
            Item("Books", "Harry Potter ", 15, "J.K. Rowling", 1997),
            Item("Books", "Pride and Prejudice", 9, "Jane Austen", 1813),
            Item("Books", "The Great Gatsby", 12, "F. Scott Fitzgerald", 1925),
            Item("Books", "To Kill a Mockingbird", 10, "Harper Lee", 1960),
            Item("Books", "The Catcher in the Rye", 11, "J.D. Salinger", 1951)
        ]

        searchButton = tk.Button(ctg4, text="Search", fg="white", bg="#6162FF",
                                 command=lambda: searchItem(list, search.get(), ctg4))
        searchButton.place(x=250, y=50)
        i=20
        j=100
        for item in list:
            frame = tk.LabelFrame(ctg4, text="Item Details",fg="white", bg="#6162FF")
            frame.place(x=i, y=j)
            i += 200
            if i == 620:
                i = 20
                j += 200

            name_label = tk.Label(frame, text=f"Name: {item.name}")
            name_label.pack(pady=5)

            price_label = tk.Label(frame, text=f"Price: {item.price}")
            price_label.pack(pady=5)

            brand_label = tk.Label(frame, text=f"Brand: {item.brand}")
            brand_label.pack(pady=5)

            year_label = tk.Label(frame, text=f"Model Year: {item.year}")
            year_label.pack(pady=5)

            button = tk.Button(frame, text="Add to Cart",fg="REd", bg="Black",
                               command=lambda: add_to_cart(item, myCart))
            button.pack(pady=10)

        ctg4.mainloop()

    def open_ctg5(list):

        ctg5 = tk.Tk()
        ctg5.geometry("500x500")
        ctg5.title("Sports")

        back_button = tk.Button(ctg5, text="Back", command=lambda: back_to_homePage(ctg5))
        back_button.place(x=10, y=10)

        search = tk.Entry(ctg5, font="Arial 12")
        search.place(x=250, y=30)


        sort = tk.Button(ctg5, text="Sort price low to high",command=lambda: items_quick_sort_price(list, ctg5))
        sort.place(x=10, y=40)



        #global Sports
        list = [
            Item("Sports", "Athletic Shorts", 49, "Puma", 2022),
            Item("Sports", "Racket", 29, "Under Armour", 2023),
            Item("Sports", "Running Shoes", 79, "Nike", 2022),
            Item("Sports", "Sports Leggings", 39, "Adidas", 2021),
            Item("Sports", "Sweatbands", 12, "New Balance", 2023),
            Item("Sports", "Training T-Shirt", 35, "Reebok", 2021),
        ]

        searchButton = tk.Button(ctg5, text="Search", fg="white", bg="#6162FF",
                                 command=lambda: searchItem(list, search.get(), ctg5))
        searchButton.place(x=250, y=50)
        i=20
        j=100
        for item in list:
            frame = tk.LabelFrame(ctg5, text="Item Details",fg="white", bg="#6162FF")
            frame.place(x=i, y=j)
            i += 150
            if i == 470:
                i = 20
                j += 200

            name_label = tk.Label(frame, text=f"Name: {item.name}")
            name_label.pack(pady=5)

            price_label = tk.Label(frame, text=f"Price: {item.price}")
            price_label.pack(pady=5)

            brand_label = tk.Label(frame, text=f"Brand: {item.brand}")
            brand_label.pack(pady=5)

            year_label = tk.Label(frame, text=f"Model Year: {item.year}")
            year_label.pack(pady=5)

            button = tk.Button(frame, text="Add to Cart",fg="REd", bg="Black",
                               command=lambda: add_to_cart(item, myCart))
            button.pack(pady=10)

        ctg5.mainloop()






















class Item:
    def __init__(self, category, name, price, brand, year):
        self.category = category
        self.name = name
        self.price = price
        self.brand = brand
        self.year = year


total_price = 0
myCart = []

HomeAppliances = []
Electronics = []
Fashion = []
Books = []
Sports = []


loginPage()