from email.message import EmailMessage
import ssl
import smtplib
import random



def email_verification(email, verify_as_list):

    num = random.randrange(1, 10**3)
    verify = str(num).zfill(3)
    verify_as_list.append(verify)

    email_sender = 'service.etudiantid1@gmail.com'
    email_password = 'ahrlnewqmjhbgtnj'
    email_receiver = email

    subject = 'verification'
    body = f'your verification code is {verify}. please use this code to submit your registration. '



    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context= context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())



def send_email_where_id(email, id):

    email_sender = 'service.etudiantid1@gmail.com'
    email_password = 'ahrlnewqmjhbgtnj'
    email_receiver = email

    subject = 'verification'
    body = f'hello ! your ID is {id}. be careful next time UwU'

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    print('id verif message sent')


def forgot_password(email, code):

    email_sender = 'service.etudiantid1@gmail.com'
    email_password = 'ahrlnewqmjhbgtnj'
    email_receiver = email

    subject = 'verification'
    body = f'hello ! your password is {code}. be careful next time UwU'

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
