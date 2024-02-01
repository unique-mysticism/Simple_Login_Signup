from gui import *
import tkinter.messagebox as tkMessageBox



def message_color(txt:str):
    """ Detect message color
        If it's error message return red color
        If it's success message return blue color
        
    Arguments:
        txt {str} -- message

    Returns:
        {str} -- message color
    """
    txt = txt.casefold()
    if "success" in txt:
        return "blue"
    elif "error" in txt or "password" in txt:
        return "red"
    else:
        return "black"
       

def create_frame():
    """ 
    Create form frame
    """
    frame = Frame(form, bg=TEXT_BG)
    frame.pack(side=TOP, pady=20)
    return frame


def get_info(key:list, value:list) -> dict:
    """ Get inputs and put them in a dict

    Arguments:
        key {list} -- form lables
        value {list} -- form inputs

    Returns:
        dict
    """
    keys = ["_".join(lbl.lower().split()).strip(":") for lbl in key]
    values = [entry.get() for entry in value]
    return dict(zip(keys, values))


def exxit():
    """
    It will destroy Main window
    """
    result = tkMessageBox.askquestion("System", "Are you sure you want to exit?", icon="warning")
    if result == "yes":
        form.destroy()
        exit()
        
