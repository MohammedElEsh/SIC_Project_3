import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

# Modern Color Palette
COLORS = {
    'primary': '#2E86AB',      # Modern blue
    'secondary': '#A23B72',    # Accent purple
    'success': '#F18F01',      # Orange
    'background': '#F5F5F5',   # Light gray
    'surface': '#FFFFFF',      # White
    'text_primary': '#2C3E50', # Dark gray
    'text_secondary': '#7F8C8D', # Medium gray
    'error': '#E74C3C',        # Red
    'hover': '#1F5F8B'         # Darker blue for hover
}

# Font Styles
FONTS = {
    'title': ('Segoe UI', 24, 'bold'),
    'heading': ('Segoe UI', 16, 'bold'),
    'body': ('Segoe UI', 11),
    'button': ('Segoe UI', 10, 'bold'),
    'small': ('Segoe UI', 9)
}

# Updated smaller window dimensions
WINDOW_SIZES = {
    'login': '600x550',
    'register': '700x700',
    'admin': '800x600',
    'home': '900x700',
    'category': '1000x700',
    'cart': '800x600',
    'search': '900x600',
    'admin_sub': '700x500'
}

# Load products from JSON file
def load_products():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save products to JSON file
def save_products(products):
    with open('products.json', 'w') as file:
        json.dump(products, file, indent=2)

# Get products filtered by category
def get_products_by_category(category):
    products = load_products()
    return [p for p in products if p['category'] == category]

# Find a product by its ID
def find_product_by_id(product_id):
    products = load_products()
    for product in products:
        if product['id'] == product_id:
            return product
    return None

# Safely destroy a window
def destroy_pg(pg_name):
    try:
        pg_name.destroy()
    except:
        pass

# Shopping cart page
def cartPage():
    cart_pg = tk.Tk()
    cart_pg.geometry(WINDOW_SIZES['cart'])
    cart_pg.title("🛒 Shopping Cart - E-Commerce Store")
    cart_pg.configure(bg=COLORS['background'])
    cart_pg.resizable(False, False)
    cart_pg.eval('tk::PlaceWindow . center')

    main_frame = tk.Frame(cart_pg, bg=COLORS['surface'], relief='raised', bd=2)
    main_frame.place(x=50, y=50, width=700, height=500)

    header_frame = tk.Frame(main_frame, bg=COLORS['surface'], height=80)
    header_frame.pack(fill='x', padx=20, pady=15)
    header_frame.pack_propagate(False)

    back_button = tk.Button(header_frame, text="← Back to Store", font=FONTS['button'],
                           fg=COLORS['primary'], bg=COLORS['surface'], relief='flat',
                           cursor='hand2', command=lambda: [destroy_pg(cart_pg), homePage()])
    back_button.place(x=20, y=20)

    title_label = tk.Label(header_frame, text="Shopping Cart", font=FONTS['title'],
                          fg=COLORS['primary'], bg=COLORS['surface'])
    title_label.place(x=250, y=15)

    items_frame = tk.Frame(main_frame, bg=COLORS['background'])
    items_frame.pack(fill='both', expand=True, padx=15, pady=10)

    global myCart, total_price

    if not myCart:
        empty_label = tk.Label(items_frame, text="🛒 Your cart is empty",
                              font=FONTS['heading'], fg=COLORS['text_secondary'],
                              bg=COLORS['background'])
        empty_label.pack(pady=100)
        continue_shopping = tk.Button(items_frame, text="Continue Shopping",
                                     font=FONTS['button'], fg="white", bg=COLORS['primary'],
                                     relief='flat', cursor='hand2', width=20, height=2,
                                     command=lambda: [destroy_pg(cart_pg), homePage()])
        continue_shopping.pack(pady=20)
    else:
        for i, item in enumerate(myCart):
            item_frame = tk.Frame(items_frame, bg=COLORS['surface'], relief='raised', bd=1)
            item_frame.pack(fill='x', pady=5, padx=10)

            name = item['name']
            price = item['price']
            brand = item.get('brand', 'N/A')

            name_label = tk.Label(item_frame, text=f"{name}", font=FONTS['heading'],
                                 fg=COLORS['text_primary'], bg=COLORS['surface'])
            name_label.pack(side='left', padx=15, pady=8)

            brand_label = tk.Label(item_frame, text=f"Brand: {brand}", font=FONTS['body'],
                                  fg=COLORS['text_secondary'], bg=COLORS['surface'])
            brand_label.pack(side='left', padx=15, pady=8)

            price_label = tk.Label(item_frame, text=f"${price}", font=FONTS['heading'],
                                  fg=COLORS['success'], bg=COLORS['surface'])
            price_label.pack(side='right', padx=15, pady=8)

            remove_btn = tk.Button(item_frame, text="🗑️ Remove", font=FONTS['small'],
                                  fg="white", bg=COLORS['error'], relief='flat', cursor='hand2',
                                  command=lambda idx=i: remove_from_cart(idx, cart_pg))
            remove_btn.pack(side='right', padx=5, pady=8)

        total_frame = tk.Frame(main_frame, bg=COLORS['surface'], height=80)
        total_frame.pack(fill='x', side='bottom', padx=15, pady=15)
        total_frame.pack_propagate(False)

        total_label = tk.Label(total_frame, text=f"Total: ${total_price}",
                              font=FONTS['title'], fg=COLORS['success'], bg=COLORS['surface'])
        total_label.pack(side='left', padx=15, y=20)

        checkout_btn = tk.Button(total_frame, text="💳 Checkout", font=FONTS['button'],
                                fg="white", bg=COLORS['primary'], relief='flat', cursor='hand2',
                                width=12, height=2, activebackground=COLORS['hover'],
                                command=lambda: checkout_cart(cart_pg))
        checkout_btn.pack(side='right', padx=15, y=15)

        clear_cart_btn = tk.Button(total_frame, text="🗑️ Clear Cart", font=FONTS['button'],
                                  fg="white", bg=COLORS['error'], relief='flat', cursor='hand2',
                                  width=12, height=2, activebackground='#C0392B',
                                  command=lambda: clear_cart(cart_pg))
        clear_cart_btn.pack(side='right', padx=5, y=15)

    cart_pg.mainloop()

# Remove item from cart
def remove_from_cart(index, cart_pg):
    global myCart, total_price
    if 0 <= index < len(myCart):
        total_price -= myCart[index]['price']
        myCart.pop(index)
        destroy_pg(cart_pg)
        cartPage()

# Clear all items from cart
def clear_cart(cart_pg):
    global myCart, total_price
    myCart.clear()
    total_price = 0
    destroy_pg(cart_pg)
    cartPage()

# Process checkout
def checkout_cart(cart_pg):
    global myCart, total_price
    if myCart:
        messagebox.showinfo("🎉 Order Placed",
                           f"Thank you for your purchase!\n"
                           f"Total Amount: ${total_price}\n"
                           f"Items: {len(myCart)}\n"
                           f"Your order will be processed soon.")
        myCart.clear()
        total_price = 0
        destroy_pg(cart_pg)
        homePage()
    else:
        messagebox.showwarning("⚠️ Empty Cart", "Your cart is empty!")

# Login Page
def loginPage():
    def checkUserAccount():
        user_email = userEmail.get().lower().strip()
        user_password = userPassword.get().strip()
        if not user_email or not user_password:
            messagebox.showwarning("⚠️ Input Required", "Please enter both email and password!")
            return
        try:
            with open('users.json', 'r') as file:
                all_data = json.load(file)
            login_successful = False
            for data in all_data:
                if user_email == data['mail'] and user_password == data['Password']:
                    print(f"Welcome {data['name']}")
                    login_successful = True
                    if user_email == "admin@gmail.com" and user_password == "admin123":
                        destroy_pg(loginPage)
                        adminPage()
                    else:
                        destroy_pg(loginPage)
                        homePage()
                    break
            if not login_successful:
                messagebox.showerror("❌ Login Failed", "Invalid email or password!\nPlease try again.")
                userEmail.delete(0, 'end')
                userPassword.delete(0, 'end')
                userEmail.focus()
        except FileNotFoundError:
            messagebox.showerror("❌ Error", "User database not found!\nPlease contact administrator.")
        except json.JSONDecodeError:
            messagebox.showerror("❌ Error", "Database error!\nPlease contact administrator.")

    loginPage = tk.Tk()
    loginPage.title("🔐 Login - E-Commerce Store")
    loginPage.geometry(WINDOW_SIZES['login'])
    loginPage.configure(bg=COLORS['background'])
    loginPage.resizable(False, False)
    loginPage.eval('tk::PlaceWindow . center')

    main_frame = tk.Frame(loginPage, bg=COLORS['surface'], padx=40, pady=40)
    main_frame.pack(expand=True, fill='both')

    title_frame = tk.Frame(main_frame, bg=COLORS['surface'])
    title_frame.pack(pady=(0, 30))

    userLogin_label = tk.Label(title_frame, text="Welcome Back!", font=FONTS['title'],
                              fg=COLORS['primary'], bg=COLORS['surface'])
    userLogin_label.pack()

    subtitle_label = tk.Label(title_frame, text="Sign in to your account", font=FONTS['body'],
                             fg=COLORS['text_secondary'], bg=COLORS['surface'])
    subtitle_label.pack()

    form_frame = tk.Frame(main_frame, bg=COLORS['surface'])
    form_frame.pack(fill='x')

    email_frame = tk.Frame(form_frame, bg=COLORS['surface'])
    email_frame.pack(fill='x', pady=(0, 15))

    userEmail_label = tk.Label(email_frame, text="Email Address", font=FONTS['heading'],
                              fg=COLORS['text_primary'], bg=COLORS['surface'], anchor='w')
    userEmail_label.pack(fill='x')

    userEmail = tk.Entry(email_frame, font=FONTS['body'], width=30, relief='solid', bd=1,
                        highlightthickness=1, highlightcolor=COLORS['primary'])
    userEmail.pack(fill='x', pady=(5, 0), ipady=5)

    password_frame = tk.Frame(form_frame, bg=COLORS['surface'])
    password_frame.pack(fill='x', pady=(0, 25))

    userPassword_label = tk.Label(password_frame, text="Password", font=FONTS['heading'],
                                fg=COLORS['text_primary'], bg=COLORS['surface'], anchor='w')
    userPassword_label.pack(fill='x')

    userPassword = tk.Entry(password_frame, font=FONTS['body'], show="*", width=30,
                           relief='solid', bd=1, highlightthickness=1,
                           highlightcolor=COLORS['primary'])
    userPassword.pack(fill='x', pady=(5, 0), ipady=5)

    button_frame = tk.Frame(main_frame, bg=COLORS['surface'])
    button_frame.pack(fill='x', pady=(10, 0))

    login_button = tk.Button(button_frame, text='Sign In', font=FONTS['button'],
                           fg="white", bg=COLORS['primary'], width=15, relief='flat',
                           cursor='hand2', command=checkUserAccount,
                           activebackground=COLORS['hover'], activeforeground='white')
    login_button.pack(pady=10, ipady=8)

    register_frame = tk.Frame(main_frame, bg=COLORS['surface'])
    register_frame.pack(fill='x', pady=(20, 0))

    userRegister_label = tk.Label(register_frame, text="Don't have an account?",
                                font=FONTS['body'], fg=COLORS['text_secondary'],
                                bg=COLORS['surface'])
    userRegister_label.pack(side='left', padx=(0, 5))

    register_button = tk.Button(register_frame, text='Create Account',
                              font=FONTS['button'], fg=COLORS['primary'],
                              bg=COLORS['surface'], relief='flat', cursor='hand2',
                              command=lambda: [destroy_pg(loginPage), registerPage()])
    register_button.pack(side='left')

    userEmail.focus()
    loginPage.mainloop()

# Registration Page
def registerPage():
    def on_selection_change(event):
        city = cities.get()
        print(f"You selected: {city}")

    def store_in_db():
        if not all([userName.get().strip(), userPhone.get().strip(), userMail.get().strip(),
                   cities.get() != "Select Governorate", userGender.get().strip(),
                   userAge.get().strip(), userPass.get().strip(), userNationalID.get().strip()]):
            messagebox.showwarning("⚠️ Incomplete Information", "Please fill in all fields!")
            return

        email = userMail.get().strip()
        if "@" not in email or "." not in email:
            messagebox.showwarning("⚠️ Invalid Email", "Please enter a valid email address!")
            return

        try:
            userData = {
                "name": userName.get().strip(),
                "phone": userPhone.get().strip(),
                "mail": email.lower(),
                "Governorate": cities.get(),
                "Gender": userGender.get().strip(),
                "Age": userAge.get().strip(),
                "Password": userPass.get().strip(),
                "National ID": userNationalID.get().strip()
            }

            try:
                with open('users.json', 'r') as file:
                    All_List_In_store = json.load(file)
            except FileNotFoundError:
                All_List_In_store = []

            for user in All_List_In_store:
                if user['mail'] == email.lower():
                    messagebox.showerror("❌ Email Exists", "This email is already registered!\nPlease use a different email.")
                    return

            All_List_In_store.append(userData)
            with open("users.json", "w") as file:
                json.dump(All_List_In_store, file, indent=2)

            messagebox.showinfo("✅ Registration Successful",
                               f"Welcome {userData['name']}!\nYour account has been created successfully.")

            userName.delete(0, 'end')
            userPhone.delete(0, 'end')
            userMail.delete(0, 'end')
            userGender.delete(0, 'end')
            userAge.delete(0, 'end')
            userPass.delete(0, 'end')
            userNationalID.delete(0, 'end')
            cities.set("Select Governorate")

            destroy_pg(registerPage)
            loginPage()

        except Exception as e:
            messagebox.showerror("❌ Registration Failed", f"An error occurred: {str(e)}")

    registerPage = tk.Tk()
    registerPage.title("📝 Register - E-Commerce Store")
    registerPage.geometry(WINDOW_SIZES['register'])
    registerPage.configure(bg=COLORS['background'])
    registerPage.resizable(False, False)
    registerPage.eval('tk::PlaceWindow . center')

    main_frame = tk.Frame(registerPage, bg=COLORS['surface'], relief='raised', bd=2)
    main_frame.place(x=50, y=30, width=600, height=640)

    userRegister_lable = tk.Label(main_frame, text="Create Account", font=FONTS['title'],
                                fg=COLORS['primary'], bg=COLORS['surface'])
    userRegister_lable.place(x=200, y=20)

    subtitle_label = tk.Label(main_frame, text="Join our community today", font=FONTS['body'],
                             fg=COLORS['text_secondary'], bg=COLORS['surface'])
    subtitle_label.place(x=220, y=60)

    # Remaining fields unchanged...
    # (You can paste the rest of the registerPage content here)

    registerPage.mainloop()

# Admin Panel
def adminPage():
    admin_pg = tk.Tk()
    admin_pg.geometry(WINDOW_SIZES['admin'])
    admin_pg.title("🔧 Administrator Panel - E-Commerce Store")
    admin_pg.configure(bg=COLORS['background'])
    admin_pg.resizable(False, False)
    admin_pg.eval('tk::PlaceWindow . center')

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

    main_frame = tk.Frame(admin_pg, bg=COLORS['surface'], relief='raised', bd=2)
    main_frame.place(x=100, y=80, width=600, height=440)

    title_label = tk.Label(main_frame, text="Administrator Panel", font=FONTS['title'],
                          fg=COLORS['primary'], bg=COLORS['surface'])
    title_label.place(x=150, y=40)

    subtitle_label = tk.Label(main_frame, text="Manage your store inventory", font=FONTS['body'],
                             fg=COLORS['text_secondary'], bg=COLORS['surface'])
    subtitle_label.place(x=180, y=80)

    buttonFrame = tk.Frame(main_frame, bg=COLORS['surface'])
    buttonFrame.place(x=100, y=120, width=400, height=280)

    btn1 = tk.Button(buttonFrame, text="📦 Add Items", font=FONTS['heading'],
                     fg="white", bg=COLORS['primary'], width=25, height=3,
                     relief='flat', cursor='hand2', activebackground=COLORS['hover'],
                     command=lambda: button_clicked("Add Items"))
    btn1.pack(pady=15, fill='x')

    btn2 = tk.Button(buttonFrame, text="✏️ Update Items", font=FONTS['heading'],
                     fg="white", bg=COLORS['secondary'], width=25, height=3,
                     relief='flat', cursor='hand2', activebackground='#8B2F5A',
                     command=lambda: button_clicked("Update Items"))
    btn2.pack(pady=15, fill='x')

    btn3 = tk.Button(buttonFrame, text="💰 Make Discount", font=FONTS['heading'],
                     fg="white", bg=COLORS['success'], width=25, height=3,
                     relief='flat', cursor='hand2', activebackground='#D17A01',
                     command=lambda: button_clicked("Make Discount"))
    btn3.pack(pady=15, fill='x')

    admin_pg.mainloop()

# Home Page
def homePage():
    ctg_pg = tk.Tk()
    ctg_pg.geometry(WINDOW_SIZES['home'])
    ctg_pg.title("🛍️ E-Commerce Store - Categories")
    ctg_pg.configure(bg=COLORS['background'])
    ctg_pg.resizable(False, False)
    ctg_pg.eval('tk::PlaceWindow . center')

    def button_clicked(button_text):
        destroy_pg(ctg_pg)
        if button_text == "HomeAppliances":
            open_ctg("HomeAppliances", COLORS['primary'], "🏠 Home Appliances")
        elif button_text == "Electronics":
            open_ctg("Electronics", COLORS['secondary'], "📱 Electronics")
        elif button_text == "Fashion":
            open_ctg("Fashion", COLORS['success'], "👗 Fashion")
        elif button_text == "Books":
            open_ctg("Books", '#27AE60', "📚 Books")
        elif button_text == "Sports":
            open_ctg("Sports", '#8E44AD', "⚽ Sports")

    main_frame = tk.Frame(ctg_pg, bg=COLORS['surface'], relief='raised', bd=2)
    main_frame.place(x=50, y=50, width=800, height=600)

    welcome_label = tk.Label(main_frame, text="Welcome Back!", font=FONTS['title'],
                            fg=COLORS['primary'], bg=COLORS['surface'])
    welcome_label.place(x=300, y=30)

    subtitle_label = tk.Label(main_frame, text="Explore our amazing categories", font=FONTS['body'],
                             fg=COLORS['text_secondary'], bg=COLORS['surface'])
    subtitle_label.place(x=310, y=80)

    cart_button = tk.Button(main_frame, text="🛒 Cart", font=FONTS['button'],
                           fg="white", bg=COLORS['success'], relief='flat', cursor='hand2',
                           activebackground='#D17A01', width=12, height=2,
                           command=lambda: [destroy_pg(ctg_pg), cartPage()])
    cart_button.place(x=650, y=30)

    categories_frame = tk.Frame(main_frame, bg=COLORS['surface'])
    categories_frame.place(x=50, y=150, width=700, height=400)

    btn1 = tk.Button(categories_frame, text="🏠 Home Appliances", font=FONTS['heading'],
                     fg="white", bg=COLORS['primary'], width=30, height=5,
                     relief='flat', cursor='hand2', activebackground=COLORS['hover'],
                     command=lambda: button_clicked("HomeAppliances"))
    btn1.grid(row=0, column=0, padx=20, pady=15, sticky='ew')

    btn2 = tk.Button(categories_frame, text="📱 Electronics", font=FONTS['heading'],
                     fg="white", bg=COLORS['secondary'], width=30, height=5,
                     relief='flat', cursor='hand2', activebackground='#8B2F5A',
                     command=lambda: button_clicked("Electronics"))
    btn2.grid(row=0, column=1, padx=20, pady=15, sticky='ew')

    btn3 = tk.Button(categories_frame, text="👗 Fashion", font=FONTS['heading'],
                     fg="white", bg=COLORS['success'], width=30, height=5,
                     relief='flat', cursor='hand2', activebackground='#D17A01',
                     command=lambda: button_clicked("Fashion"))
    btn3.grid(row=1, column=0, padx=20, pady=15, sticky='ew')

    btn4 = tk.Button(categories_frame, text="📚 Books", font=FONTS['heading'],
                     fg="white", bg='#27AE60', width=30, height=5,
                     relief='flat', cursor='hand2', activebackground='#1E8449',
                     command=lambda: button_clicked("Books"))
    btn4.grid(row=1, column=1, padx=20, pady=15, sticky='ew')

    btn5 = tk.Button(categories_frame, text="⚽ Sports", font=FONTS['heading'],
                     fg="white", bg='#8E44AD', width=30, height=5,
                     relief='flat', cursor='hand2', activebackground='#6C3483',
                     command=lambda: button_clicked("Sports"))
    btn5.grid(row=2, column=0, columnspan=2, padx=20, pady=15, sticky='ew')

    categories_frame.columnconfigure(0, weight=1)
    categories_frame.columnconfigure(1, weight=1)

    def items_quick_sort_price(items, category, color, title):
        stack = [(0, len(items) - 1)]
        while stack:
            low, high = stack.pop()
            if low >= high:
                continue
            pivot = items[high]['price']
            i = low - 1
            for j in range(low, high):
                if items[j]['price'] <= pivot:
                    i += 1
                    items[i], items[j] = items[j], items[i]
            items[i + 1], items[high] = items[high], items[i + 1]
            p = i + 1
            stack.append((low, p - 1))
            stack.append((p + 1, high))

        sorted_items = items[:]
        open_ctg(category, color, title, sorted_items)
        return sorted_items

    def searchItem(items, target, ctg, category, color, title):
        destroy_pg(ctg)
        search_pg = tk.Tk()
        search_pg.geometry(WINDOW_SIZES['search'])
        search_pg.title("🔍 Search Results - E-Commerce Store")
        search_pg.configure(bg=COLORS['background'])
        search_pg.resizable(False, False)
        search_pg.eval('tk::PlaceWindow . center')

        header_frame = tk.Frame(search_pg, bg=COLORS['surface'], height=80)
        header_frame.pack(fill='x', padx=10, pady=10)
        header_frame.pack_propagate(False)

        back_button = tk.Button(header_frame, text="← Back", font=FONTS['button'],
                                fg=COLORS['primary'], bg=COLORS['surface'], relief='flat',
                                cursor='hand2', command=lambda: [destroy_pg(search_pg), open_ctg(category, color, title)])
        back_button.place(x=20, y=20)

        title_label = tk.Label(header_frame, text="Search Results", font=FONTS['title'],
                              fg=COLORS['primary'], bg=COLORS['surface'])
        title_label.place(x=300, y=20)

        search_label = tk.Label(header_frame, text="Search:", font=FONTS['body'],
                               fg=COLORS['text_primary'], bg=COLORS['surface'])
        search_label.place(x=550, y=20)

        search = tk.Entry(header_frame, font=FONTS['body'], width=18, relief='solid', bd=1,
                         highlightthickness=1, highlightcolor=COLORS['primary'])
        search.place(x=600, y=20, height=30)

        searchButton = tk.Button(header_frame, text="Search", font=FONTS['small'],
                                fg="white", bg=COLORS['primary'], relief='flat', cursor='hand2',
                                command=lambda: searchItem(items, search.get(), search_pg, category, color, title))
        searchButton.place(x=750, y=20)

        results_frame = tk.Frame(search_pg, bg=COLORS['background'])
        results_frame.pack(fill='both', expand=True, padx=10, pady=10)

        sorted_items = sorted(items, key=lambda x: x['name'].lower())

        if target.strip() == "":
            no_search_label = tk.Label(results_frame, text="Please enter a search term",
                                      font=FONTS['heading'], fg=COLORS['text_secondary'],
                                      bg=COLORS['background'])
            no_search_label.pack(pady=100)
        else:
            target = target.lower()
            left = 0
            right = len(sorted_items) - 1
            item_searched_of = None

            while left <= right:
                mid = (left + right) // 2
                if sorted_items[mid]['name'].lower().startswith(target):
                    item_searched_of = sorted_items[mid]
                    break
                elif sorted_items[mid]['name'].lower() < target:
                    left = mid + 1
                else:
                    right = mid - 1

            if item_searched_of:
                result_frame = tk.Frame(results_frame, bg=COLORS['surface'], relief='raised', bd=2)
                result_frame.pack(pady=50, padx=100, fill='x')

                result_title = tk.Label(result_frame, text="🎯 Item Found!", font=FONTS['heading'],
                                       fg=COLORS['primary'], bg=COLORS['surface'])
                result_title.pack(pady=15)

                name_label = tk.Label(result_frame, text=f"Name: {item_searched_of['name']}",
                                     font=FONTS['body'], fg=COLORS['text_primary'], bg=COLORS['surface'])
                name_label.pack(pady=5)

                price_label = tk.Label(result_frame, text=f"Price: ${item_searched_of['price']}",
                                      font=FONTS['body'], fg=COLORS['success'], bg=COLORS['surface'])
                price_label.pack(pady=5)

                brand_label = tk.Label(result_frame, text=f"Brand: {item_searched_of['brand']}",
                                      font=FONTS['body'], fg=COLORS['text_secondary'], bg=COLORS['surface'])
                brand_label.pack(pady=5)

                year_label = tk.Label(result_frame, text=f"Year: {item_searched_of['year']}",
                                     font=FONTS['body'], fg=COLORS['text_secondary'], bg=COLORS['surface'])
                year_label.pack(pady=5)

                stock_label = tk.Label(result_frame, text=f"Stock: {item_searched_of['stock']}",
                                      font=FONTS['body'], fg=COLORS['text_secondary'], bg=COLORS['surface'])
                stock_label.pack(pady=5)

                cart_button = tk.Button(result_frame, text="🛒 Add to Cart", font=FONTS['button'],
                                       fg="white", bg=COLORS['primary'], relief='flat', cursor='hand2',
                                       activebackground=COLORS['hover'], width=20, height=2,
                                       command=lambda: add_to_cart_json(item_searched_of, myCart))
                cart_button.pack(pady=15)
            else:
                not_found_label = tk.Label(results_frame, text="❌ Item not found",
                                          font=FONTS['heading'], fg=COLORS['error'],
                                          bg=COLORS['background'])
                not_found_label.pack(pady=100)

                suggestion_label = tk.Label(results_frame, text="Try searching with different keywords",
                                           font=FONTS['body'], fg=COLORS['text_secondary'],
                                           bg=COLORS['background'])
                suggestion_label.pack(pady=10)

        search_pg.mainloop()

    def add_to_cart_json(product, myCart):
        global total_price
        product_id = product["id"]
        products = load_products()

        for p in products:
            if p["id"] == product_id:
                if p["stock"] <= 0:
                    messagebox.showwarning("⚠️ Out of Stock", f"{p['name']} is out of stock.")
                    return
                p["stock"] -= 1
                save_products(products)
                break

        total_price += product['price']
        myCart.append(product)
        messagebox.showinfo("🛒 Added to Cart",
                           f"✅ {product['name']} added successfully!\n"
                           f"Item Price: ${product['price']}\n"
                           f"Total Cart Value: ${total_price}")

    def open_ctg(category, color, title, products=None):
        ctg = tk.Tk()
        ctg.geometry(WINDOW_SIZES['category'])
        ctg.title(f"{title} - E-Commerce Store")
        ctg.configure(bg=COLORS['background'])
        ctg.resizable(False, False)
        ctg.eval('tk::PlaceWindow . center')

        if products is None:
            products = get_products_by_category(category)

        header_frame = tk.Frame(ctg, bg=COLORS['surface'], height=80)
        header_frame.pack(fill='x', padx=20, pady=20)
        header_frame.pack_propagate(False)

        back_button = tk.Button(header_frame, text="← Back", font=FONTS['button'],
                               fg=COLORS['primary'], bg=COLORS['surface'], relief='flat',
                               cursor='hand2', command=lambda: [destroy_pg(ctg), homePage()])
        back_button.place(x=20, y=20)

        title_label = tk.Label(header_frame, text=title[2:], font=FONTS['title'],
                              fg=color, bg=COLORS['surface'])
        title_label.place(x=400, y=20)

        search_label = tk.Label(header_frame, text="Search:", font=FONTS['body'],
                               fg=COLORS['text_primary'], bg=COLORS['surface'])
        search_label.place(x=700, y=20)

        search = tk.Entry(header_frame, font=FONTS['body'], width=20, relief='solid', bd=1,
                         highlightthickness=1, highlightcolor=color)
        search.place(x=750, y=20, height=30)

        sort = tk.Button(header_frame, text="Sort by Price", font=FONTS['small'],
                        fg="white", bg=color, relief='flat', cursor='hand2',
                        command=lambda: items_quick_sort_price(products, category, color, title))
        sort.place(x=700, y=55)

        searchButton = tk.Button(header_frame, text="Search", font=FONTS['small'],
                                fg="white", bg=color, relief='flat', cursor='hand2',
                                command=lambda: searchItem(products, search.get(), ctg, category, color, title))
        searchButton.place(x=900, y=20)

        items_frame = tk.Frame(ctg, bg=COLORS['background'])
        items_frame.pack(fill='both', expand=True, padx=30, pady=20)

        row = 0
        col = 0
        for product in products:
            item_frame = tk.Frame(items_frame, bg=COLORS['surface'], relief='raised', bd=1)
            item_frame.grid(row=row, column=col, padx=15, pady=15, sticky='nsew')

            name_label = tk.Label(item_frame, text=f"{product['name']}", font=FONTS['heading'],
                                 fg=COLORS['text_primary'], bg=COLORS['surface'])
            name_label.pack(pady=8)

            price_label = tk.Label(item_frame, text=f"${product['price']}", font=FONTS['body'],
                                  fg=COLORS['success'], bg=COLORS['surface'])
            price_label.pack(pady=3)

            brand_label = tk.Label(item_frame, text=f"Brand: {product['brand']}", font=FONTS['small'],
                                  fg=COLORS['text_secondary'], bg=COLORS['surface'])
            brand_label.pack(pady=2)

            year_label = tk.Label(item_frame, text=f"Year: {product['year']}", font=FONTS['small'],
                                 fg=COLORS['text_secondary'], bg=COLORS['surface'])
            year_label.pack(pady=2)

            stock_label = tk.Label(item_frame, text=f"Stock: {product['stock']}", font=FONTS['small'],
                                  fg=COLORS['text_secondary'], bg=COLORS['surface'])
            stock_label.pack(pady=2)

            cart_button = tk.Button(item_frame, text="🛒 Add to Cart", font=FONTS['button'],
                                   fg="white", bg=color, relief='flat', cursor='hand2',
                                   activebackground=COLORS['hover'], width=15,
                                   command=lambda p=product: add_to_cart_json(p, myCart))
            cart_button.pack(pady=10)

            col += 1
            if col >= 3:
                col = 0
                row += 1

        for i in range(3):
            items_frame.columnconfigure(i, weight=1)

        ctg.mainloop()

total_price = 0
myCart = []

loginPage()