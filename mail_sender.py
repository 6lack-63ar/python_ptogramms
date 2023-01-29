# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 14:29:54 2023

@author: B3ar
"""

import smtplib

s_mail=input("enter the senders email :")

password=input("enter senders password : ")    


r_mail=input("Enter the recievers email address :")




subj=input("please enter the subject of the email :")
msg = input("please enter the message to send :")
part1 = """

To:%s
From:%s
Subject:%s
message:%s

"""%(s_mail,r_mail,subj,msg)

part2 =""" %s """%msg

message = part1+part2
try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(s_mail, password)
    smtp_server.sendmail(s_mail,r_mail, message.as_string())
    smtp_server.quit()
    print("email sent successfully")
except Exception:
  
    print("\r\n\r\n\r\n ***********************EMAIL NOT SENT**********************")





