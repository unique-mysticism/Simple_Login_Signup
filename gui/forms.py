from .function import *
from auth.validation import check_signup, check_login, check_reset_password



def show_message(result):
    """Printing validation result message

    Arguments:
        result {str} -- validation result

    Returns:
        bool -- If show message was blu it means action was success,
                so it returns True else returns None(False)
    """
    color = message_color(result)
    if color == "red":
        result = result.strip("Error:")
    elif color == "blue":
        empty_inputs()
        output.config(text=result, fg=color)
        return True
    output.config(text=result, fg=color)
    
    

def signup():
    """
    The register action, it takes form information such as lables as keys and entries as values,
    then passes the information as a dictionary to check if they are valid and displays the result,
    if "show_message(result)" was true, meaning the action was successful and do something as needed.
    """
    info = get_info(lbls, entries)
    result = check_signup(info)
    if show_message(result):
        pass


def login():
    """
    The Login action, it takes form information such as lables as keys and entries as values,
    then passes the information as a dictionary to check if they are valid and displays the result,
    if "show_message(result)" was true, shows profile form.
    """
    info = get_info(lbls, entries)
    result = check_login(info)
    if show_message(result):
        ToggleToProfile()
        result_profile.config(text="Here is your profile:", fg="black")


def reset_password():
    """
    The Reset Password action, it takes form information such as lables as keys and entries as values,
    then passes the information as a dictionary to check if they are valid and displays the result,
    if "show_message(result)" was true, meaning the action was successful and do something as needed.
    """
    info = get_info(lbls, entries)
    result = check_reset_password(info)
    if show_message(result):
        pass
     

       
def signup_form():
    """
    Create Signup form
    """
    global currentframe, output, lbls, entries
    lbls = ["Username:", "Password:", "Confirm Password:", "First name:", "Last name:", "Email Address:", "Phone Number:"]
    entries = [USERNAME, PASSWORD, CONFIRM_PASSWORD, FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, PHONE_NUMBER]
    links = ["Already have account?"]
    
    currentframe = create_frame()
    lbl_entry_pairs(lbls, entries)
    link_login = Label(currentframe, text=links[0], font="Helvetica 15 underline", bg=TEXT_BG)
    link_login.grid(row=8, columnspan=2)
    link_login.bind("<Button-1>", ToggleToLogin)
    btn_sginup = Button(currentframe, text="Register", font=TEXT_FONT, command=signup, width=20, bg=ENTRY_BG, borderwidth=8)
    btn_sginup.grid(row=9, columnspan=2, pady=(10,0))   
    output = Label(currentframe, text="", font=TEXT_FONT, bg=TEXT_BG, wraplength=500)
    output.grid(row=10, columnspan=2, pady=(10,0))
       
          
def login_form():
    """
    Create Login form
    """
    global currentframe, output, lbls, entries
    lbls = ["Username:", "Password:"]
    entries = [USERNAME, PASSWORD]
    links = ["Forget Password", "Don't have account?"]
    
    currentframe = create_frame()
    lbl_entry_pairs(lbls, entries)
    link_forget_password = Label(currentframe, text=links[0], font="Helvetica 15 underline", bg=TEXT_BG)
    link_forget_password.grid(row=3, columnspan=2)
    link_forget_password.bind("<Button-1>", ToggleToResetPassword)
    link_signup = Label(currentframe, text=links[1], font="Helvetica 15 underline", bg=TEXT_BG)
    link_signup.grid(row=4, columnspan=2)
    link_signup.bind("<Button-1>", ToggleToSignup)
    btn_login = Button(currentframe, text="Login", command=login, font=TEXT_FONT, width=20, bg=ENTRY_BG, borderwidth=8)
    btn_login.grid(row=5, columnspan=2, pady=(10,0))
    output = Label(currentframe, text="", font=TEXT_FONT, bg=TEXT_BG, wraplength=500)
    output.grid(row=6, columnspan=2, pady=(10,0))
    

def reset_password_form():
    """
    Create Reset Password form
    """
    global currentframe, output, lbls, entries
    lbls = ["Username:", "Password:", "Confirm Password:"]
    entries = [USERNAME, PASSWORD, CONFIRM_PASSWORD]
    
    currentframe = create_frame()
    lbl_entry_pairs(lbls, entries)
    btn_back = Button(currentframe, text="⬅️Back", command=ToggleToLogin, font=TEXT_FONT, bg=ENTRY_BG, borderwidth=8)
    btn_back.grid(row=4, sticky="W", pady=(10,0), padx=(100,0))
    btn_change_password = Button(currentframe, text="Change Password", font=TEXT_FONT, command=reset_password, width=20, bg=ENTRY_BG, borderwidth=8)
    btn_change_password.grid(row=4, columnspan=2, pady=(10,0), padx=(110,0))
    output = Label(currentframe, text="", font=TEXT_FONT, bd=15, bg=TEXT_BG, wraplength=500)
    output.grid(row=5, columnspan=2, pady=(10,0))


def profile_form():
    """
    Create Profile form
    """
    global currentframe, result_profile
    
    currentframe = create_frame()    
    btn_logout  = Button(currentframe, text="Logout", command=ToggleToLogin, font=TEXT_FONT, bg=ENTRY_BG, borderwidth=8)
    btn_logout.grid(row=1, column=1, sticky="W")
    result_profile = Label(currentframe, text="", font=TEXT_FONT, bd=15, bg=TEXT_BG)
    result_profile.grid(row=1, column=2, padx=(0,200))



def ToggleToLogin(event=None):
    """ Toggle To someform changes 'current_form' to 'profile_form' """   
    currentframe.destroy()
    login_form()

def ToggleToSignup(event=None):
    """ Toggle To someform changes 'current_form' to 'profile_form' """ 
    currentframe.destroy()
    signup_form()

def ToggleToResetPassword(event=None):
    """ Toggle To someform changes 'current_form' to 'profile_form' """ 
    currentframe.destroy()
    reset_password_form()

def ToggleToProfile(event=None):
    """ Toggle To someform changes 'current_form' to 'profile_form' """ 
    currentframe.destroy()
    profile_form()



def lbl_entry_pairs(lbls:list, entries:list):
    """Create Lable and Entrie together as pairs in forms
    
    Arguments:
        lbls {list} -- List of Lables name
        entries {list} -- List of Entries name
    """
    for row_num, lbl, entry in zip(range(len(lbls)), lbls, entries):
        lbl = Label(currentframe, text=lbl, font=TEXT_FONT, bd=15, bg=TEXT_BG, width=20)
        lbl.grid(row = row_num)
        # If the entry type is password, it shows * instead of letters.
        entry_show = "*" if entry in [PASSWORD, CONFIRM_PASSWORD] else None
        entry = Entry(currentframe, textvariable=entry, font=TEXT_FONT, bg=ENTRY_BG, width=20, show=entry_show)
        entry.grid(row = row_num, column=1, sticky="W",padx=(0,50))
        
        
        
def empty_inputs():
    """ Set all enteries empty"""
    USERNAME.set("")
    PASSWORD.set("")
    CONFIRM_PASSWORD.set("")
    FIRST_NAME.set("")
    LAST_NAME.set("")
    EMAIL_ADDRESS.set("")
    PHONE_NUMBER.set("")
    
# Define global Entries name
USERNAME = StringVar()
PASSWORD = StringVar()
CONFIRM_PASSWORD = StringVar()
FIRST_NAME = StringVar()
LAST_NAME = StringVar()
EMAIL_ADDRESS = StringVar()
PHONE_NUMBER = StringVar()

