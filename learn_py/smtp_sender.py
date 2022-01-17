import smtplib
import os
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')     # mail to google account (env)
EMAIL_PASS = os.environ.get('EMAIL_PASS')           # pass to google account (env)

def wyslij(body,subject = 'q(o.o)p'):
    #send mail with body and subject
    
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()                                     #identification
        smtp.starttls()                                 #ciphering
        smtp.ehlo()
        
        smtp.login(EMAIL_ADDRESS,EMAIL_PASS)
         
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(EMAIL_ADDRESS,'michal19wrzes@gmail.com',msg)  #(from, to, msg)

    
    