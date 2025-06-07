import json
from tkinter import messagebox

class ProductManager:
    def __init__(self, file_path='products.json'):
        self.file_path = file_path

    def load_products(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_products(self, products):
        with open(self.file_path, 'w') as file:
            json.dump(products, file, indent=2)

    def get_products_by_category(self, category):
        products = self.load_products()
        return [p for p in products if p['category'] == category]

    def find_product_by_id(self, product_id):
        products = self.load_products()
        for product in products:
            if product['id'] == product_id:
                return product
        return None

class UserManager:
    def __init__(self, file_path='users.json'):
        self.file_path = file_path

    def load_users(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_user(self, user_data):
        users = self.load_users()
        users.append(user_data)
        with open(self.file_path, 'w') as file:
            json.dump(users, file, indent=2)

    def email_exists(self, email):
        users = self.load_users()
        return any(user['mail'] == email.lower() for user in users)

    def validate_login(self, email, password):
        users = self.load_users()
        for user in users:
            if user['mail'] == email.lower() and user['Password'] == password:
                return user
        return None

class CartManager:
    def __init__(self):
        self.cart = []
        self.total_price = 0
        self.product_manager = ProductManager()

    def add_to_cart(self, product):
        product_id = product["id"]
        products = self.product_manager.load_products()

        for p in products:
            if p["id"] == product_id:
                if p["stock"] <= 0:
                    messagebox.showwarning("⚠️ Out of Stock", f"{p['name']} is out of stock.")
                    return
                p["stock"] -= 1
                self.product_manager.save_products(products)
                break

        self.total_price += product['price']
        self.cart.append(product)
        messagebox.showinfo("🛒 Added to Cart",
                           f"✅ {product['name']} added successfully!\n"
                           f"Item Price: ${product['price']}\n"
                           f"Total Cart Value: ${self.total_price}")

    def remove_from_cart(self, index):
        if 0 <= index < len(self.cart):
            self.total_price -= self.cart[index]['price']
            self.cart.pop(index)

    def clear_cart(self):
        self.cart.clear()
        self.total_price = 0

    def checkout(self):
        if self.cart:
            messagebox.showinfo("🎉 Order Placed",
                               f"Thank you for your purchase!\n"
                               f"Total Amount: ${self.total_price}\n"
                               f"Items: {len(self.cart)}\n"
                               f"Your order will be processed soon.")
            self.clear_cart()
        else:
            messagebox.showwarning("⚠️ Empty Cart", "Your cart is empty!")