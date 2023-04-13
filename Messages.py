import smtplib
from email.message import EmailMessage

def email_alert(sub, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = sub
    msg['to'] = to

    user = '.....'
    msg['from'] = user
    password = '.....'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

if __name__ == '__main__':
    email_alert('Testing', 'Hello World', '......')