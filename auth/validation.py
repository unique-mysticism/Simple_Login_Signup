from db.querys import *
from libs.verification import *
from .models import *
from libs.messages import *
      
    
    
def check_signup(info):   
    """Checking the validity of the registration Form information

    Arguments:
        info {dict} -- user's information

    Returns:
        {str} -- validation result
    """
    validation_result = check(info)
    
    if validation_result:
        return validation_result
    if info.get("username"):
        if duplicate_found(info["username"]): 
            return error_duplicate_username
    if if_empty(info):
        return error_empty_input
    if info.get("email_address"):        
        chk_emal = email_validate(info["email_address"],info["first_name"])  
        if not chk_emal:
            return error_email_address
    ######################
    user = User(**info)
    user.user_save()
    return chk_emal


def check_login(info):
    """Checking the validity of the Login Form information

    Arguments:
        info {dict} -- user's information

    Returns:
        {str} -- validation result
    """
    validation_result = check({"username":info.get("username")})
    if validation_result:
        return validation_result
    if if_empty(info):
        return error_empty_input
    ################
    user = User(**info)
    if user.user_found():
        return successful_login
    else:
        return error_username_password_match
        

def check_reset_password(info):
    """Checking the validity of the Reset Password Form information

   Arguments:
        info {dict} -- user's information

    Returns:
        {str} -- validation result
    """
       
    validation_result = check(info)
    if validation_result:
        return validation_result
    if info.get("username"):
        if not duplicate_found(info["username"]): 
            return error_exist_username
    if if_empty(info):
        return error_empty_input
    ################
    user = User(**info)
    if user.user_found():
        return error_duplicate_password
    if user.change_password():
        return successful_password_changed
    return error_connection
    




 
def check(info):
    """Checking the validity of the information 

    Arguments:
        info {dict} -- user's information

    Returns:
        {str} -- validation result
    """
    if info.get("username"):
        if not username_validate(info["username"]):
            return error_username
        
    if info.get("password"):
        chk_paswod = list(password_validate(info["password"]))
        if chk_paswod:
            return "\n".join(chk_paswod)
        if info.get("confirm_password"):
            if not info["password"] == info["confirm_password"]:
                return error_passwords_match
        
    if info.get("first_name"):
        if not name_validate(info["first_name"]):
            return error_first_name
        
    if info.get("last_name"):
        if not name_validate(info["last_name"]):
            return error_last_name
        
    if info.get("phone_number"):
        if not phone_num_validate(info["phone_number"]):
            return error_phone_num 
        


def if_empty(info):
    """Checking if form enteries are empty or not
    
    Arguments:
        info {dict} -- user's information

    Returns:
        {bool} -- Return False if the value of an item in info, is empty
    """
    return [False for ele in list(info.values()) if ele == ""]