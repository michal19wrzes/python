import smtplib
import os
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')     # mail to google account
EMAIL_PASS = os.environ.get('EMAIL_PASS')           # pass to google account (configured lesssecureapp)


with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()                                     #identyfikacja
    smtp.starttls()                                 #szyfrowanie
    smtp.ehlo()
    
    smtp.login(EMAIL_ADDRESS,EMAIL_PASS)
    
    subject = 'Testowy temat'
    body = 'Ładny dzień tralal lala'
    
    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS,msg)  #(from, to, msg)
    
    