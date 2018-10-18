
# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib

try:
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
      
    # start TLS for security 
    s.starttls() 
      
    # Authentication 
    s.login("sanjaypjayan2000@gmail.com", "password") 
      
    # message to be sent 
    message = "This is a simple message using general method"
      
    # sending the mail 
    s.sendmail("sanjaypjayan2000@gmail.com", "sanjaypjayan2000@gmail.com", message) 
      
    # terminating the session 
    s.quit()

    print("mail send")

except:
    print("Got some error")
