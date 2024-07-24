
import smtplib

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
    email_address = 'casianpantilimon98@gmail.com'
    email_password = 'nisd ftan msbl xadt'
    connection.login(email_address, email_password)
    connection.sendmail(from_addr=email_address, to_addrs='casianpantilimon98@gmail.com',
                        msg="subject:This is a test Email \n\n This was sent from my IDE, hehe. ")
