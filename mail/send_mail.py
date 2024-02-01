# import base64
from base64 import b64decode
from smtplib import SMTP_SSL
from ssl import create_default_context
from email.message import EmailMessage



def send_verify_mail(email:str, name:str):
    """ Send verify mail to user EmailAddress

    Arguments:
        email {str} -- user's email address
        name {str} -- user's name
    """    
    sender_email = "unique52hertzwhale@gmail.com"
    pemail = b64decode("d3RkbiBnc2R0IHhlbGYganJkZw==").decode("utf-8")
    email_receiver = email
    subject = "Welcom to Mysticism"
    body = f"""
        Hi {name},\n
        Hope you are doing well.\n\n\n
                            Your account has been successfully created.
                    Thank you so much in advance for your time and expertise.
              Sources link: https://github.com/unique-mysticism?tab=repositories
                  Follow me on GitHub for more codes. (〃￣︶￣)人(￣︶￣〃)\n\n\n
        Erfan Ramezani,
        Mysticism
    """

    mail = EmailMessage()
    mail["From"] = sender_email
    mail["To"] = email_receiver
    mail["Subject"] = subject
    mail.set_content(body.center(50))
    context = create_default_context()
    
    with SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender_email, pemail)
        smtp.sendmail(sender_email, email_receiver, mail.as_string())
        


def send_verify_message(phone_num:str):
    """ Send verify message to user PhoneNumber

    Arguments:
        phone_num {str} -- user's phone number
    """
    pass