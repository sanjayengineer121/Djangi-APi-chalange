import re
import smtplib

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

def verify_email(email):
    domain = email.split('@')[1]
    
    try:
        # Increase timeout to 10 seconds
        with smtplib.SMTP(domain, timeout=10) as smtp:
            code, _ = smtp.helo()
            if code == 250:
                return True
            else:
                return False
    except smtplib.SMTPConnectError:
        return False

# Example usage
email = "sanjayyadav112105786@gmail.com"
if is_valid_email(email):
    if verify_email(email):
        print("Email address is valid and exists.")
    else:
        print("Email address is valid but does not exist.")
else:
    print("Email address is not valid.")

import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("your username", "your password")
server.sendmail(
  "from@address.com", 
  "to@address.com", 
  "this message is from python")
server.quit()
