import os
import smtplib
import config
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate



def send_mail(send_to, text, files=[], isTls=True):
    print('Sending mail')
    msg = MIMEMultipart()
    msg['From'] = 'Deckbuilder'
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = 'Experiment log'

    msg.attach(MIMEText(text))

    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(f, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(f)))
        msg.attach(part)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    if isTls:
        smtp.starttls()
    smtp.login('paolopalmiero.p', config.GMAIL_PASSWORD)
    smtp.sendmail('Deckbuilder', send_to, msg.as_string())
    smtp.quit()
