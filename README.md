# 🛍️ E-Commerce Store System
A modern and user-friendly e-commerce desktop application built with Python and Tkinter, developed during the Samsung Innovation Campus (SIC) course.
It supports user registration, login, product browsing by categories, shopping cart functionality, and order management.

🛠️ Also packaged as an .exe file using PyInstaller, making it easy to run on any Windows machine without Python.

## 🧾 Features
🔐 **User Authentication**
- User registration with comprehensive form validation
- Secure login system with email and password
- Admin panel access for store management
- Egyptian governorate selection for user location

🛒 **Shopping Experience**
- Browse products by categories (Home Appliances, Electronics, Fashion, Books, Sports)
- Add products to shopping cart with real-time stock management
- Remove items from cart or clear entire cart
- Checkout functionality with order confirmation
- Search products within categories
- Sort products by price using quick sort algorithm

📊 **Product Management**
- Comprehensive product database with JSON storage
- Product details include: name, price, brand, year, description, stock
- Real-time stock updates when items are purchased
- Category-based product organization

💻 **User Interface**
- Modern and intuitive GUI design
- Responsive layout with consistent styling
- Color-coded categories for easy navigation
- Professional typography and spacing
- Emoji-enhanced user experience

## 🧱 Project Structure
```
SIC_Project_3/
├── dist/                        # Directory for distribution files
├── __pycache__/                 # Python cache files
├── main.exe                     # Executable version of the project
├── main.py                      # Main application entry point
├── main.spec                    # PyInstaller spec file
├── pages.py                     # GUI pages and user interface logic
├── data_manager.py              # Data management classes (Product, User, Cart)
├── config.py                    # Configuration settings (colors, fonts, sizes)
├── utils.py                     # Utility functions and helpers
├── products.json                # Product database
├── users.json                   # User database
├── Project_3.pptx               # Project presentation
├── Project_3_repo_link.txt      # Repository link
└── README.md                    # Project documentation
```

## 🚀 How to Run

### ▶️ Option 1: Run with Python
Make sure Python is installed on your system (Python 3.10+ recommended):

```bash
git clone https://github.com/MohammedElEsh/SIC_Project_3.git
cd SIC_Project_3
python main.py
```

✅ Make sure `products.json` and `users.json` exist in the same folder before starting.

### 🖥️ Option 2: Run .exe (No Python needed)
If you prefer to run the executable version:

1. Navigate to the project directory
2. Double-click on `main.exe` to start the application
3. ✅ Ensure all necessary files are in the same directory as the executable

## 📦 Technologies Used
- **Python 3.12** - Core programming language
- **Tkinter** - GUI framework for desktop application
- **JSON** - Database storage for products and users
- **PyInstaller** - For building standalone executable
- **OOP Concepts** - Clean code architecture with classes
- **Data Structures** - Quick sort algorithm for product sorting

## 🎯 Key Components

### 📱 Pages (pages.py)
- **LoginPage** - User authentication interface
- **RegisterPage** - New user registration with form validation
- **HomePage** - Main dashboard with category navigation
- **CategoryPage** - Product listing with search and sort functionality
- **CartPage** - Shopping cart management
- **SearchPage** - Product search results display
- **AdminPage** - Administrative interface (admin@gmail.com / admin123)

### 💾 Data Management (data_manager.py)
- **ProductManager** - Handle product CRUD operations
- **UserManager** - Manage user registration and authentication
- **CartManager** - Shopping cart functionality with stock management

### ⚙️ Configuration (config.py)
- Color schemes and themes
- Font definitions and sizes
- Window dimensions for different pages

## 🔑 Default Admin Access
- **Email:** admin@gmail.com
- **Password:** admin123

## 📊 Product Categories
1. 🏠 **Home Appliances** - Microwave, Refrigerator, Washing Machine, AC
2. 📱 **Electronics** - Smartphones, Laptops, TVs, Gaming Consoles
3. 👗 **Fashion** - Clothing, Shoes, Accessories, Watches
4. 📚 **Books** - Classic Literature, Modern Fiction, Educational
5. ⚽ **Sports** - Athletic Wear, Equipment, Accessories

## 🛡️ Security Features
- Password field masking during input
- Email format validation
- Duplicate email prevention during registration
- Input sanitization and validation
- Session management for user authentication

## 📸 Screenshots
(Add screenshots by placing images in an `images/` folder and updating the path below)

![Application Demo](images/demo.png)

## 👨‍💻 Author
**Mohammed El Esh**
🎓 Samsung Innovation Campus Graduate
🔗 [GitHub Profile](https://github.com/MohammedElEsh)

## 📄 License
This project is licensed under the MIT License – feel free to use, modify, and share it!

## ❤️ Special Thanks
Thanks to the **Samsung Innovation Campus (SIC)** team for the training and support throughout this project.

## 🚀 Future Enhancements
- Database integration (SQLite/MySQL)
- Payment gateway integration
- Order history and tracking
- Product reviews and ratings
- Inventory management dashboard
- Email notifications
- Multi-language support
- Mobile responsive design