from pages import LoginPage
from config import WINDOW_SIZES, COLORS

def main():
    login_page = LoginPage()
    login_page.geometry(WINDOW_SIZES['login'])
    login_page.title("🔐 Login - E-Commerce Store")
    login_page.configure(bg=COLORS['background'])
    login_page.resizable(False, False)
    login_page.eval('tk::PlaceWindow . center')
    login_page.mainloop()

if __name__ == "__main__":
    
    main()