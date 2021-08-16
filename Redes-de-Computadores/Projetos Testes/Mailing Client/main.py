import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo() #start the process

with open("password.txt", 'r') as f:
    password = f.read()

server.login('mail@mail.com', password)

msg = MIMEMultipart()

msg['From'] = 'User Test'
msg['To'] = 'emailFromThePerson@email.com'
msg['Subject'] = 'Just A test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message), 'plain')


filename = 'imagem.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename{filename}')
msg.attach(p)

text = msg.as_string()

server.sendmail('yourEmail@gmail.com', 'emailFromThePerson@email.com', text)