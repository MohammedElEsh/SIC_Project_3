import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
from config import COLORS, FONTS, WINDOW_SIZES
from data_manager import ProductManager, UserManager, CartManager
from utils import destroy_page, quick_sort_price

class Page(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cart_manager = CartManager()
        self.product_manager = ProductManager()
        self.user_manager = UserManager()

class LoginPage(Page):
    def __init__(self):
        super().__init__()
        self.geometry(WINDOW_SIZES['login'])
        self.title("🔐 Login - E-Commerce Store")
        self.configure(bg=COLORS['background'])
        self.resizable(False, False)
        self.eval('tk::PlaceWindow . center')
        self.create_widgets()

    def create_widgets(self):
        main_frame = tk.Frame(self, bg=COLORS['surface'], padx=40, pady=40)
        main_frame.pack(expand=True, fill='both')

        title_frame = tk.Frame(main_frame, bg=COLORS['surface'])
        title_frame.pack(pady=(0, 30))

        tk.Label(title_frame, text="Welcome Back!", font=FONTS['title'],
                 fg=COLORS['primary'], bg=COLORS['surface']).pack()
        tk.Label(title_frame, text="Sign in to your account", font=FONTS['body'],
                 fg=COLORS['text_secondary'], bg=COLORS['surface']).pack()

        form_frame = tk.Frame(main_frame, bg=COLORS['surface'])
        form_frame.pack(fill='x')

        email_frame = tk.Frame(form_frame, bg=COLORS['surface'])
        email_frame.pack(fill='x', pady=(0, 15))
        tk.Label(email_frame, text="Email Address", font=FONTS['heading'],
                 fg=COLORS['text_primary'], bg=COLORS['surface'], anchor='w').pack(fill='x')
        self.user_email = tk.Entry(email_frame, font=FONTS['body'], width=30, relief='solid', bd=1,
                                  highlightthickness=1, highlightcolor=COLORS['primary'])
        self.user_email.pack(fill='x', pady=(5, 0), ipady=5)

        password_frame = tk.Frame(form_frame, bg=COLORS['surface'])
        password_frame.pack(fill='x', pady=(0, 25))
        tk.Label(password_frame, text="Password", font=FONTS['heading'],
                 fg=COLORS['text_primary'], bg=COLORS['surface'], anchor='w').pack(fill='x')
        self.user_password = tk.Entry(password_frame, font=FONTS['body'], show="*", width=30,
                                     relief='solid', bd=1, highlightthickness=1,
                                     highlightcolor=COLORS['primary'])
        self.user_password.pack(fill='x', pady=(5, 0), ipady=5)

        button_frame = tk.Frame(main_frame, bg=COLORS['surface'])
        button_frame.pack(fill='x', pady=(10, 0))
        tk.Button(button_frame, text='Sign In', font=FONTS['button'],
                 fg="white", bg=COLORS['primary'], width=15, relief='flat',
                 cursor='hand2', command=self.check_user_account,
                 activebackground=COLORS['hover'], activeforeground='white').pack(pady=10, ipady=8)

        register_frame = tk.Frame(main_frame, bg=COLORS['surface'])
        register_frame.pack(fill='x', pady=(20, 0))
        tk.Label(register_frame, text="Don't have an account?",
                 font=FONTS['body'], fg=COLORS['text_secondary'],
                 bg=COLORS['surface']).pack(side='left', padx=(0, 5))
        tk.Button(register_frame, text='Create Account',
                 font=FONTS['button'], fg=COLORS['primary'],
                 bg=COLORS['surface'], relief='flat', cursor='hand2',
                 command=lambda: [destroy_page(self), RegisterPage()]).pack(side='left')

        self.user_email.focus()

    def check_user_account(self):
        email = self.user_email.get().lower().strip()
        password = self.user_password.get().strip()
        if not email or not password:
            messagebox.showwarning("⚠️ Input Required", "Please enter both email and password!")
            return

        user = self.user_manager.validate_login(email, password)
        if user:
            print(f"Welcome {user['name']}")
            if email == "admin@gmail.com" and password == "admin123":
                destroy_page(self)
                AdminPage()
            else:
                destroy_page(self)
                HomePage(cart_manager=self.cart_manager)
        else:
            messagebox.showerror("❌ Login Failed", "Invalid email or password!\nPlease try again.")
            self.user_email.delete(0, 'end')
            self.user_password.delete(0, 'end')
            self.user_email.focus()

class RegisterPage(Page):
    def __init__(self):
        super().__init__()
        self.geometry(WINDOW_SIZES['register'])
        self.title("📝 Register - E-Commerce Store")
        self.configure(bg=COLORS['background'])
        self.resizable(False, False)
        self.eval('tk::PlaceWindow . center')
        self.create_widgets()

    def create_widgets(self):
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

                destroy_page(self)
                LoginPage()

            except Exception as e:
                messagebox.showerror("❌ Registration Failed", f"An error occurred: {str(e)}")

        main_frame = tk.Frame(self, bg=COLORS['surface'], relief='raised', bd=2)
        main_frame.place(x=50, y=30, width=600, height=640)

        tk.Label(main_frame, text="Create Account", font=FONTS['title'],
                 fg=COLORS['primary'], bg=COLORS['surface']).place(x=200, y=20)
        tk.Label(main_frame, text="Join our community today", font=FONTS['body'],
                 fg=COLORS['text_secondary'], bg=COLORS['surface']).place(x=220, y=60)

        # Name
        tk.Label(main_frame, text="Name", font=FONTS['body'],
                 fg=COLORS['text_primary'], bg=COLORS['surface']).place(x=50, y=100)
        userName = tk.Entry(main_frame, font=FONTS['body'], width=30, relief='solid', bd=1)
        userName.place(x=200, y=100, height=30)

        # Phone
        tk.Label(main_frame, text="Phone", font=FONTS['body'],
                 fg=COLORS['text_primary'], bg=COLORS['surface']).place(x=50, y=160)
        userPhone = tk.Entry(main_frame, font=FONTS['body'], width=30, relief='solid', bd=1)
        userPhone.place(x=200, y=160, height=30)

        # Email
        tk.Label(main_frame, text="Email", font=FONTS['body'],
                 fg=COLORS['text_primary'], bg=COLORS['surface']).place(x=50, y=220)
        userMail = tk.Entry(main_frame, font=FONTS['body'], width=30, relief='solid', bd=1)
        userMail.place(x=200, y=220, height=30)

        # Gender
        tk.Label(main_frame, text="Gender", font=FONTS['body'],
                 fg=COLORS['text_primary'], bg=COLORS['surface']).place(x=50, y=280)
        userGender = tk.Entry(main_frame, font=FONTS['body'], width=30, relief='solid', bd=1)
        userGender.place(x=200, y=280, height=30)

        # Age
        tk.Label(main_frame, text="Age", font=FONTS['body'],
                 fg=COLORS['text_primary'], bg=COLORS['surface']).place(x=50, y=340)
        userAge = tk.Entry(main_frame, font=FONTS['body'], width=30, relief='solid', bd=1)
        userAge.place(x=200, y=340, height=30)

        # Password
        tk.Label(main_frame, text="Password", font=FONTS['body'],
                 fg=COLORS['text_primary'], bg=COLORS['surface']).place(x=50, y=400)
        userPass = tk.Entry(main_frame, font=FONTS['body'], width=30, relief='solid', bd=1, show="*")
        userPass.place(x=200, y=400, height=30)

        # National ID
        tk.Label(main_frame, text="National ID", font=FONTS['body'],
                 fg=COLORS['text_primary'], bg=COLORS['surface']).place(x=50, y=460)
        userNationalID = tk.Entry(main_frame, font=FONTS['body'], width=30, relief='solid', bd=1)
        userNationalID.place(x=200, y=460, height=30)

        # Governorate
        tk.Label(main_frame, text="Governorate", font=FONTS['body'],
                 fg=COLORS['text_primary'], bg=COLORS['surface']).place(x=50, y=520)
        cities = ttk.Combobox(main_frame, values=[
            "Select Governorate",
            "Alexandria", "Aswan", "Asyut", "Beheira", "Beni Suef", "Cairo",
            "Dakahlia", "Damietta", "Faiyum", "Gharbia", "Giza", "Ismailia",
            "Kafr El Sheikh", "Luxor", "Matruh", "Minya", "Monufia", "New Valley",
            "North Sinai", "Port Said", "Qalyubia", "Qena", "Red Sea", "Sharqia",
            "Sohag", "South Sinai", "Suez"
        ], font=FONTS['body'], state='readonly')
        cities.place(x=200, y=520, width=200, height=30)
        cities.current(0)
        cities.bind("<<ComboboxSelected>>", on_selection_change)

        # Register Button
        tk.Button(main_frame, text="Register", font=FONTS['button'],
                 fg="white", bg=COLORS['primary'], relief='flat', cursor='hand2',
                 command=store_in_db).place(x=200, y=580, width=200, height=40)

class HomePage(Page):
    def __init__(self, cart_manager):
        super().__init__()
        self.cart_manager = cart_manager
        self.geometry(WINDOW_SIZES['home'])
        self.title("🛍️ E-Commerce Store - Categories")
        self.configure(bg=COLORS['background'])
        self.resizable(False, False)
        self.eval('tk::PlaceWindow . center')
        self.create_widgets()

    def create_widgets(self):
        main_frame = tk.Frame(self, bg=COLORS['surface'], relief='raised', bd=2)
        main_frame.place(x=50, y=50, width=800, height=600)

        tk.Label(main_frame, text="Welcome Back!", font=FONTS['title'],
                 fg=COLORS['primary'], bg=COLORS['surface']).place(x=300, y=30)
        tk.Label(main_frame, text="Explore our amazing categories", font=FONTS['body'],
                 fg=COLORS['text_secondary'], bg=COLORS['surface']).place(x=310, y=80)

        tk.Button(main_frame, text="🛒 Cart", font=FONTS['button'],
                 fg="white", bg=COLORS['success'], relief='flat', cursor='hand2',
                 activebackground='#D17A01', width=12, height=2,
                 command=lambda: [destroy_page(self), CartPage(self.cart_manager)]).place(x=650, y=30)

        tk.Button(main_frame, text="🔓 Logout", font=FONTS['button'],
                 fg="white", bg=COLORS['error'], relief='flat', cursor='hand2',
                 activebackground='#C0392B', width=12, height=2,
                 command=self.logout).place(x=50, y=30)

        categories_frame = tk.Frame(main_frame, bg=COLORS['surface'])
        categories_frame.place(x=50, y=150, width=700, height=400)

        categories = [
            ("HomeAppliances", COLORS['primary'], "🏠 Home Appliances", 0, 0, '#1F5F8B'),
            ("Electronics", COLORS['secondary'], "📱 Electronics", 0, 1, '#8B2F5A'),
            ("Fashion", COLORS['success'], "👗 Fashion", 1, 0, '#D17A01'),
            ("Books", '#27AE60', "📚 Books", 1, 1, '#1E8449'),
            ("Sports", '#8E44AD', "⚽ Sports", 2, 0, '#6C3483')
        ]
        for cat, color, text, row, col, active_color in categories:
            btn = tk.Button(categories_frame, text=text, font=FONTS['heading'],
                           fg="white", bg=color, width=30, height=5,
                           relief='flat', cursor='hand2',
                           activebackground=active_color,
                           command=lambda c=cat, clr=color, t=text: self.open_category(c, clr, t))
            btn.grid(row=row, column=col, padx=20, pady=15, sticky='ew')
            if cat == "Sports":
                btn.grid(columnspan=2)

        categories_frame.columnconfigure(0, weight=1)
        categories_frame.columnconfigure(1, weight=1)

    def logout(self):
    # Show confirmation dialog
        confirmed = messagebox.askyesno("Logout Confirmation", "Are you sure you want to logout?")
        
        if confirmed:
            self.cart_manager.clear_cart()
            messagebox.showinfo("Success", "You have been logged out successfully!")
            destroy_page(self)
            LoginPage()

    def open_category(self, category, color, title):
        destroy_page(self)
        CategoryPage(category, color, title, self.cart_manager)

class CartPage(Page):
    def __init__(self, cart_manager):
        super().__init__()
        self.cart_manager = cart_manager
        self.geometry(WINDOW_SIZES['cart'])
        self.title("🛒 Shopping Cart - E-Commerce Store")
        self.configure(bg=COLORS['background'])
        self.resizable(False, False)
        self.eval('tk::PlaceWindow . center')
        self.create_widgets()

    def create_widgets(self):
        main_frame = tk.Frame(self, bg=COLORS['surface'], relief='raised', bd=2)
        main_frame.place(x=50, y=50, width=700, height=500)

        header_frame = tk.Frame(main_frame, bg=COLORS['surface'], height=80)
        header_frame.pack(fill='x', padx=20, pady=15)
        header_frame.pack_propagate(False)

        tk.Button(header_frame, text="← Back to Store", font=FONTS['button'],
                 fg=COLORS['primary'], bg=COLORS['surface'], relief='flat',
                 cursor='hand2', command=lambda: [destroy_page(self), HomePage(self.cart_manager)]).place(x=20, y=20)

        tk.Label(header_frame, text="Shopping Cart", font=FONTS['title'],
                 fg=COLORS['primary'], bg=COLORS['surface']).place(x=250, y=15)

        items_frame = tk.Frame(main_frame, bg=COLORS['background'])
        items_frame.pack(fill='both', expand=True, padx=15, pady=10)

        if not self.cart_manager.cart:
            tk.Label(items_frame, text="🛒 Your cart is empty",
                     font=FONTS['heading'], fg=COLORS['text_secondary'],
                     bg=COLORS['background']).pack(pady=100)
            tk.Button(items_frame, text="Continue Shopping",
                     font=FONTS['button'], fg="white", bg=COLORS['primary'],
                     relief='flat', cursor='hand2', width=20, height=2,
                     command=lambda: [destroy_page(self), HomePage(self.cart_manager)]).pack(pady=20)
        else:
            for i, item in enumerate(self.cart_manager.cart):
                item_frame = tk.Frame(items_frame, bg=COLORS['surface'], relief='raised', bd=1)
                item_frame.pack(fill='x', pady=5, padx=10)

                tk.Label(item_frame, text=f"{item['name']}", font=FONTS['heading'],
                         fg=COLORS['text_primary'], bg=COLORS['surface']).pack(side='left', padx=15, pady=8)
                tk.Label(item_frame, text=f"Brand: {item.get('brand', 'N/A')}", font=FONTS['body'],
                         fg=COLORS['text_secondary'], bg=COLORS['surface']).pack(side='left', padx=15, pady=8)
                tk.Label(item_frame, text=f"${item['price']}", font=FONTS['heading'],
                         fg=COLORS['success'], bg=COLORS['surface']).pack(side='right', padx=15, pady=8)
                tk.Button(item_frame, text="🗑️ Remove", font=FONTS['small'],
                         fg="white", bg=COLORS['error'], relief='flat', cursor='hand2',
                         command=lambda idx=i: self.remove_item(idx)).pack(side='right', padx=5, pady=8)

            total_frame = tk.Frame(main_frame, bg=COLORS['surface'], height=80)
            total_frame.pack(fill='x', side='bottom', padx=15, pady=15)
            total_frame.pack_propagate(False)

            tk.Label(total_frame, text=f"Total: ${self.cart_manager.total_price}",
                     font=FONTS['title'], fg=COLORS['success'], bg=COLORS['surface']).pack(side='left', padx=15)
            tk.Button(total_frame, text="💳 Checkout", font=FONTS['button'],
                     fg="white", bg=COLORS['primary'], relief='flat', cursor='hand2',
                     width=12, height=2, activebackground=COLORS['hover'],
                     command=self.checkout).pack(side='right', padx=15)
            tk.Button(total_frame, text="🗑️ Clear Cart", font=FONTS['button'],
                     fg="white", bg=COLORS['error'], relief='flat', cursor='hand2',
                     width=12, height=2, activebackground='#C0392B',
                     command=self.clear_cart).pack(side='right', padx=5)

    def remove_item(self, index):
        self.cart_manager.remove_from_cart(index)
        destroy_page(self)
        CartPage(self.cart_manager)

    def clear_cart(self):
        self.cart_manager.clear_cart()
        destroy_page(self)
        CartPage(self.cart_manager)

    def checkout(self):
        self.cart_manager.checkout()
        destroy_page(self)
        HomePage(self.cart_manager)

class CategoryPage(Page):
    def __init__(self, category, color, title, cart_manager, sorted_products=None):
        super().__init__()
        self.category = category
        self.color = color
        self.title_text = title
        self.cart_manager = cart_manager
        self.sorted_products = sorted_products
        self.geometry(WINDOW_SIZES['category'])
        self.title(f"{title} - E-Commerce Store")
        self.configure(bg=COLORS['background'])
        self.resizable(False, False)
        self.eval('tk::PlaceWindow . center')
        self.create_widgets()

    def create_widgets(self):
        products = self.sorted_products if self.sorted_products is not None else self.product_manager.get_products_by_category(self.category)

        header_frame = tk.Frame(self, bg=COLORS['surface'], height=80)
        header_frame.pack(fill='x', padx=20, pady=20)
        header_frame.pack_propagate(False)

        tk.Button(header_frame, text="← Back", font=FONTS['button'],
                 fg=COLORS['primary'], bg=COLORS['surface'], relief='flat',
                 cursor='hand2', command=lambda: [destroy_page(self), HomePage(self.cart_manager)]).place(x=20, y=20)
        tk.Label(header_frame, text=self.title_text[2:], font=FONTS['title'],
                 fg=self.color, bg=COLORS['surface']).place(x=400, y=20)
        tk.Label(header_frame, text="Search:", font=FONTS['body'],
                 fg=COLORS['text_primary'], bg=COLORS['surface']).place(x=700, y=20)
        search = tk.Entry(header_frame, font=FONTS['body'], width=20, relief='solid', bd=1,
                         highlightthickness=1, highlightcolor=self.color)
        search.place(x=750, y=20, height=30)
        tk.Button(header_frame, text="Sort by Price", font=FONTS['small'],
                 fg="white", bg=self.color, relief='flat', cursor='hand2',
                 command=lambda: self.sort_by_price(products)).place(x=700, y=55)
        tk.Button(header_frame, text="Search", font=FONTS['small'],
                 fg="white", bg=self.color, relief='flat', cursor='hand2',
                 command=lambda: self.search_item(products, search.get())).place(x=900, y=55)

        items_frame = tk.Frame(self, bg=COLORS['background'])
        items_frame.pack(fill='both', expand=True, padx=30, pady=20)

        if not products:
            tk.Label(items_frame, text=f"No products found in {self.title_text[2:]}",
                     font=FONTS['heading'], fg=COLORS['text_secondary'],
                     bg=COLORS['background']).pack(pady=100)
            tk.Button(items_frame, text="Back to Categories",
                     font=FONTS['button'], fg="white", bg=COLORS['primary'],
                     relief='flat', cursor='hand2', width=20, height=2,
                     command=lambda: [destroy_page(self), HomePage(self.cart_manager)]).pack(pady=20)
        else:
            row, col = 0, 0
            for product in products:
                item_frame = tk.Frame(items_frame, bg=COLORS['surface'], relief='raised', bd=1)
                item_frame.grid(row=row, column=col, padx=15, pady=15, sticky='nsew')

                tk.Label(item_frame, text=f"{product['name']}", font=FONTS['heading'],
                         fg=COLORS['text_primary'], bg=COLORS['surface']).pack(pady=8)
                tk.Label(item_frame, text=f"${product['price']}", font=FONTS['body'],
                         fg=COLORS['success'], bg=COLORS['surface']).pack(pady=3)
                tk.Label(item_frame, text=f"Brand: {product.get('brand', 'N/A')}", font=FONTS['small'],
                         fg=COLORS['text_secondary'], bg=COLORS['surface']).pack(pady=2)
                tk.Label(item_frame, text=f"Year: {product.get('year', 'N/A')}", font=FONTS['small'],
                         fg=COLORS['text_secondary'], bg=COLORS['surface']).pack(pady=2)
                tk.Label(item_frame, text=f"Stock: {product.get('stock', 'N/A')}", font=FONTS['small'],
                         fg=COLORS['text_secondary'], bg=COLORS['surface']).pack(pady=2)
                tk.Button(item_frame, text="🛒 Add to Cart", font=FONTS['button'],
                         fg="white", bg=self.color, relief='flat', cursor='hand2',
                         activebackground=COLORS['hover'], width=15,
                         command=lambda p=product: self.add_to_cart(p)).pack(pady=10)

                col += 1
                if col >= 3:
                    col = 0
                    row += 1

            for i in range(3):
                items_frame.columnconfigure(i, weight=1)

    def add_to_cart(self, product):
        self.cart_manager.add_to_cart(product)

    def sort_by_price(self, products):
        sorted_products = quick_sort_price(products.copy())
        destroy_page(self)
        CategoryPage(self.category, self.color, self.title_text, self.cart_manager, sorted_products=sorted_products)

    def search_item(self, products, target):
        destroy_page(self)
        SearchPage(products, target, self.category, self.color, self.title_text, self.cart_manager)

class SearchPage(Page):
    def __init__(self, items, target, category, color, title, cart_manager):
        super().__init__()
        self.items = items
        self.target = target
        self.category = category
        self.color = color
        self.title_text = title
        self.cart_manager = cart_manager
        self.geometry(WINDOW_SIZES['category'])
        self.title("🔍 Search Results - E-Commerce Store")
        self.configure(bg=COLORS['background'])
        self.resizable(False, False)
        self.eval('tk::PlaceWindow . center')
        self.create_widgets()

    def create_widgets(self):
        header_frame = tk.Frame(self, bg=COLORS['surface'], height=80)
        header_frame.pack(fill='x', padx=20, pady=20)
        header_frame.pack_propagate(False)

        tk.Button(header_frame, text="← Back", font=FONTS['button'],
                 fg=COLORS['primary'], bg=COLORS['surface'], relief='flat',
                 cursor='hand2', command=lambda: [destroy_page(self), CategoryPage(self.category, self.color, self.title_text, self.cart_manager)]).place(x=20, y=20)
        tk.Label(header_frame, text="Search Results", font=FONTS['title'],
                 fg=self.color, bg=COLORS['surface']).place(x=400, y=20)
        tk.Label(header_frame, text="Search:", font=FONTS['body'],
                 fg=COLORS['text_primary'], bg=COLORS['surface']).place(x=700, y=20)
        search = tk.Entry(header_frame, font=FONTS['body'], width=20, relief='solid', bd=1,
                         highlightthickness=1, highlightcolor=self.color)
        search.place(x=750, y=20, height=30)
        tk.Button(header_frame, text="Search", font=FONTS['small'],
                 fg="white", bg=self.color, relief='flat', cursor='hand2',
                 activebackground=COLORS['hover'],
                 command=lambda: self.search_item(self.items, search.get())).place(x=900, y=20)

        results_container = tk.Frame(self, bg=COLORS['background'])
        results_container.pack(fill='both', expand=True, padx=30, pady=20)

        canvas = tk.Canvas(results_container, bg=COLORS['background'], highlightthickness=0)
        scrollbar = tk.Scrollbar(results_container, orient='vertical', command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=COLORS['background'])

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        def _on_mousewheel(event):
            canvas.yview_scroll(-1 * (event.delta // 120), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        if not self.target.strip():
            tk.Label(scrollable_frame, text="Please enter a search term",
                     font=FONTS['heading'], fg=COLORS['text_secondary'],
                     bg=COLORS['background']).pack(pady=100)
            tk.Button(scrollable_frame, text="Back to Category",
                     font=FONTS['button'], fg="white", bg=self.color,
                     relief='flat', cursor='hand2', width=20, height=2,
                     activebackground=COLORS['hover'],
                     command=lambda: [destroy_page(self), CategoryPage(self.category, self.color, self.title_text, self.cart_manager)]).pack(pady=20)
        else:
            target = self.target.lower()
            matching_items = [item for item in self.items if target in item['name'].lower()]

            if matching_items:
                row, col = 0, 0
                for item in matching_items:
                    result_frame = tk.Frame(scrollable_frame, bg=COLORS['surface'], relief='raised', bd=1)
                    result_frame.grid(row=row, column=col, padx=15, pady=15, sticky='nsew')

                    tk.Label(result_frame, text=f"{item['name']}", font=FONTS['heading'],
                             fg=COLORS['text_primary'], bg=COLORS['surface']).pack(pady=8)
                    tk.Label(result_frame, text=f"Price: ${item['price']}", font=FONTS['body'],
                             fg=COLORS['success'], bg=COLORS['surface']).pack(pady=3)
                    tk.Label(result_frame, text=f"Brand: {item.get('brand', 'N/A')}", font=FONTS['small'],
                             fg=COLORS['text_secondary'], bg=COLORS['surface']).pack(pady=2)
                    tk.Label(result_frame, text=f"Year: {item.get('year', 'N/A')}", font=FONTS['small'],
                             fg=COLORS['text_secondary'], bg=COLORS['surface']).pack(pady=2)
                    tk.Label(result_frame, text=f"Stock: {item.get('stock', 'N/A')}", font=FONTS['small'],
                             fg=COLORS['text_secondary'], bg=COLORS['surface']).pack(pady=2)
                    tk.Button(result_frame, text="🛒 Add to Cart", font=FONTS['button'],
                             fg="white", bg=self.color, relief='flat', cursor='hand2',
                             activebackground=COLORS['hover'], width=15,
                             command=lambda p=item: self.cart_manager.add_to_cart(p)).pack(pady=10)

                    col += 1
                    if col >= 3:
                        col = 0
                        row += 1

                for i in range(3):
                    scrollable_frame.columnconfigure(i, weight=1)
            else:
                tk.Label(scrollable_frame, text="❌ No items found",
                         font=FONTS['heading'], fg=COLORS['error'],
                         bg=COLORS['background']).pack(pady=100)
                tk.Label(scrollable_frame, text="Try searching with different keywords",
                         font=FONTS['body'], fg=COLORS['text_secondary'],
                         bg=COLORS['background']).pack(pady=10)
                tk.Button(scrollable_frame, text="Back to Category",
                         font=FONTS['button'], fg="white", bg=self.color,
                         relief='flat', cursor='hand2', width=20, height=2,
                         activebackground=COLORS['hover'],
                         command=lambda: [destroy_page(self), CategoryPage(self.category, self.color, self.title_text, self.cart_manager)]).pack(pady=20)

    def search_item(self, items, target):
        destroy_page(self)
        SearchPage(items, target, self.category, self.color, self.title_text, self.cart_manager)

class AdminPage(Page):
    def __init__(self):
        super().__init__()
        self.geometry(WINDOW_SIZES['admin'])
        self.title("🔧 Administrator Panel - E-Commerce Store")
        self.configure(bg=COLORS['background'])
        self.resizable(False, False)
        self.eval('tk::PlaceWindow . center')
        self.create_widgets()

    def create_widgets(self):
        main_frame = tk.Frame(self, bg=COLORS['surface'], relief='raised', bd=2)
        main_frame.place(x=100, y=80, width=600, height=440)

        tk.Label(main_frame, text="Administrator Panel", font=FONTS['title'],
                 fg=COLORS['primary'], bg=COLORS['surface']).place(x=150, y=40)
        tk.Label(main_frame, text="Manage your store inventory", font=FONTS['body'],
                 fg=COLORS['text_secondary'], bg=COLORS['surface']).place(x=180, y=80)

        button_frame = tk.Frame(main_frame, bg=COLORS['surface'])
        button_frame.place(x=100, y=120, width=400, height=280)

        tk.Button(button_frame, text="📦 Add Items", font=FONTS['heading'],
                 fg="white", bg=COLORS['primary'], width=25, height=3,
                 relief='flat', cursor='hand2', activebackground=COLORS['hover'],
                 command=lambda: self.button_clicked("Add Items")).pack(pady=15, fill='x')
        tk.Button(button_frame, text="✏️ Update Items", font=FONTS['heading'],
                 fg="white", bg=COLORS['secondary'], width=25, height=3,
                 relief='flat', cursor='hand2', activebackground='#8B2F5A',
                 command=lambda: self.button_clicked("Update Items")).pack(pady=15, fill='x')
        tk.Button(button_frame, text="💰 Make Discount", font=FONTS['heading'],
                 fg="white", bg=COLORS['success'], width=25, height=3,
                 relief='flat', cursor='hand2', activebackground='#D17A01',
                 command=lambda: self.button_clicked("Make Discount")).pack(pady=15, fill='x')

    def button_clicked(self, action):
        destroy_page(self)
        AdminPage()