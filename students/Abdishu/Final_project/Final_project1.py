#!/usr/bin/python3  
# -*- coding: utf-8 -*-
"""
The following script run every hours. It check the computer public IP 

and send email alert when ISP change public IP Address.

Run as background job. (script_name &)
 

"""

import time
import subprocess
import smtplib,datetime



def SendEmail():
      
    

    From = 'kasusaat34@gmail.com' 
    #The following password is not correct is not a correct password
    E_password = 'SecretPassword'
    
    To = ['kasusaat34@gmail.com', 'abdirabinsha@gmail.com']  

    Subject = datetime.datetime.now()
    body1 =  subprocess.Popen(['dig +short myip.opendns.com @resolver1.opendns.com'],stdout=subprocess.PIPE, shell=True)
    body = body1.stdout.readline()
    Email_content  = """ 

        From: %s  \n
        To: %s  \n
        Subject: %s \n\n
        "Your New Pub IP is Now=>"  %s

        """ % (From, ", ".join(To), Subject, body)

    connToServ = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    connToServ.login( From, E_password )
    connToServ.sendmail(From, To, Email_content)
    

IpComand = 'dig +short myip.opendns.com @resolver1.opendns.com'
My_public_Ip = subprocess.Popen([IpComand],stdout=subprocess.PIPE, shell=True)

MY_IP = [My_public_Ip.stdout.readline()]

while True:
    
    MYIP_COMMAND2 = 'dig +short myip.opendns.com @resolver1.opendns.com'
    MYPUB_IP = subprocess.Popen([IpComand],stdout=subprocess.PIPE, shell=True)
    MY_NEW_IP = MYPUB_IP.stdout.readline()
    if MY_NEW_IP != MY_IP:
        #print("your public IP has been changed!,please check your email")
        SendEmail()

    #print("OLD IP IS:", MY_IP)
    MY_IP=MY_NEW_IP 
    #print("NEW IP IS:", MY_IP)
    time.sleep(3600) #Run every hours 
    
    