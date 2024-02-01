from gui import *
from gui.forms import ToggleToSignup, ToggleToLogin, signup_form, login_form, exxit



def main_window():
    """
    Create main Window
    """
    form.title("(⌐■_■)ノ  Mysticism ")
    width = 600
    height = 650
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (height/1.9))
    form.geometry(f"{width}x{height}+{x}+{y}")
    form.resizable(0, 0)
    # Default page
    signup_form()
    
    
def main_menubar():
    """
    Create main Menubar
    """
    mainbar = Menu(form)
    account = Menu(mainbar, tearoff=0, font=TEXT_FONT)
    mainbar.add_cascade(label="Account 👤", menu=account)
    mainbar.add_command(label="Exit", command=exxit)
    account.add_command(label="Sign Up", command=ToggleToSignup)
    account.add_command(label="Log In", command=ToggleToLogin)
    form.config(menu=mainbar, bg=TEXT_BG)

    
def show_window():
    main_window()
    main_menubar()
    form.mainloop()