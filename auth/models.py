from db.querys import *

class User:
    
    def __init__(self, username, password, confirm_password="", first_name="", last_name="", email_address="", phone_number=""):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
        # self.isactive= True
        # self.is_logined = False
    
    def user_found(self):
        db = database()
        db[1].execute(found_user, self.username_password())
        if db[1].fetchone() is not None:
            return True
        return False
            
    def user_save(self):
        db = database()
        db[1].execute(insert_user_table, self.user_info())
        db[0].commit()
        db[1].close()
        db[0].close()
        return True
        
    def change_password(self):
        db = database()
        db[1].execute(update_password, self.username_password()[::-1])
        db[0].commit()
        db[1].close()
        db[0].close()
        return True
    
    def user_info(self):
        return (self.username, self.password, self.first_name, self.last_name, self.email_address, self.phone_number)
    
    def username_password(self):
        return (self.username, self.password)