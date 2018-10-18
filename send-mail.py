import smtplib

import config

def send_email(subject, msg):
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(config.EMAIL_ADDRESS, config.PASSWORD)
		message = 'Subject: {}		{}'.format(subject, msg)
		server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
		server.quit()
		print("Success: Email Send.")
	except:
		print("Email Failed to Send")
		
subject = "Test Subject"
msg = "Hello There, How are you today?"

send_email(subject, msg)