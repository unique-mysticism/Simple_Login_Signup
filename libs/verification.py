import re
from mail.send_mail import send_verify_mail, send_verify_message



def email_validate(email:str, name:str) -> bool|str:
    """ Email address verification using RegularExpressions
        and send mail if it is gmail email services

    Arguments:
        email {str} -- user's email address
        name {str} -- user's name

    Returns:
        bool|str -- result
    """
    
    pattern_gy = r"\b[\w_.+-]+@+(gmail|yahoo)+(.com)$"
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
        
    if re.match(pattern_gy, email):
        send_verify_mail(email, name)
        return "Check your email.\nAccount created successfully."
    elif re.match(pattern, email):
        return "Account created successfully."
    return False

     
     
def username_validate(username:str) -> bool:
    """ Username verification using RegularExpressions

    Arguments:
        username {str} -- user's username

    Returns:
        bool -- result
    """
    
    pattern = r"^[a-z][a-z0-9-]{4,31}$"

    if re.match(pattern, username):
        return True
    return False



def password_validate(password:str) -> str:
    """ Password verification using RegularExpressions

    Arguments:
        password {str} -- user's password

    Returns:
        None

    Yields:
        Iterator[str] -- returns Error
    """
    
    pattern = r"^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-])*.{6,32}$"
    enough_length = r"^[a-zA-Z0-9#?!@$%^&*-].{6,32}$"
    contain_number = r"^(?=.*?[A-Z])*(?=.*?[a-z])*(?=.*?[0-9])(?=.*?[#?!@$%^&*-])*"
    contain_small_letter = r"^(?=.*?[A-Z])*(?=.*?[a-z])(?=.*?[0-9])*(?=.*?[#?!@$%^&*-])*"
    contain_captal_letter = r"^(?=.*?[A-Z])(?=.*?[a-z])*(?=.*?[0-9])*(?=.*?[#?!@$%^&*-])*"

    if re.match(pattern, password):
        return
    if not re.match(enough_length, password):
        yield "The password must be 6-32 characters."
    if not re.match(contain_number, password):
        yield "Use at least 1 number in your password."
    if not re.match(contain_small_letter, password):
        yield "Use at least 1 small Letter in your password."
    if not re.match(contain_captal_letter, password):
        yield "Use at least 1 Capital letter in your password."
        


def phone_num_validate(phone_num:str) -> bool:
    """ Phone number verification using RegularExpressions

    Arguments:
        phone_num {str} -- user's phone_num

    Returns:
        bool -- result
    """
    
    pattern = r"^09[0-9]{9}$"

    if re.match(pattern, phone_num):
        send_verify_message(phone_num)
        return True
    return False



def name_validate(name:str) -> bool:
    """ Name verification using RegularExpressions

    Arguments:
        name {str} -- user's name

    Returns:
        bool -- result
    """
    
    pattern = r"^[a-zA-Z]*$"

    if re.match(pattern, name):
        return True
    return False