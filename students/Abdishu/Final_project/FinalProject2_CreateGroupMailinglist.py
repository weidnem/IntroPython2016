#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script run to Register of  PythonStudyGroup 

and send out email to all member once.

"""



   
    
class PythonStudyGroup(object):
    
    """This is set of sting containg name of student volunter 
    for group python study group. The sit is limmited and student 
    Register only once as reserving sit for other not allowed"""
    
    group = {}

    #def __init__(self):
        
    """Create an empty set of names before Registirating began"""
        #self.group = group
        

    def register(self):
        
        self.name = input("Please Enter Group Member full name: ")
        self.email = input("Please Enter Group email address:")
        #try:
        if (not str(self.name) in self.group.keys()) and (not self.email in self.group.values()):
            self.group.update({self.name:self.email})
            #self.group = self.group.update({self.name:self.email})
        #except AttributeError:
            #print("You do not have key or value in your dictionary")
                        
    def member(self, name):
        """Check if name is in names"""
        return name in self.group.keys()
    def Get_email(self):
        
        return list(self.group.values())
    def Get_GroupInfo(self):
         
        return list(self.group.items())
        
    def remove(self, name):
        """Remove member from PythonStudyGroup for policy violation
        or member request to be removed """
        try:
            del self.group[name]
        except:
            raise ValueError(name + ' not member of PythonStudyGroup')
            
    
        
    def __str__(self):
        
        return str(self.group)
    
                
    
    
import smtplib
        
class Email_group(PythonStudyGroup):
    
    def __init__(self):
        
        self.To = None
        self.From =None
        self.body =[]
        self.Subject =None
        self.Email_addr ='abdirabinsha@gmail.com' #my email address.
        
        self.E_password= None
        
        
    def Send(self,E_password):
        
        #self.Email_addr = 'kasusaat34@gmail.com'  
        self.E_password = E_password

        #From = self.Email_addr  
        self.To = self.group.values()

        self.Subject = input("Enter the subject of your email: \n\n")
        self.body = input("Enter Body of the email: \n\n")


        Email_content  = """ 

        From: %s  \n
        To: %s  \n 
        "Weekly Update" %s \n\n
        "Hello Team,"  %s 

            """ % (self.Email_addr, ", ".join(self.To), self.Subject, self.body)
            

        connToServ = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        connToServ.login( self.Email_addr, E_password )
        connToServ.sendmail(self.Email_addr, self.To, Email_content)
        

s = PythonStudyGroup()         
#s.register()


numberof_member = 2
for x in range(numberof_member):

        s.register()
        
Python_groups = s.Get_GroupInfo()

"Save the group information to file"

import json
with open('Python_groups', 'w') as outfile:
    json.dump(Python_groups, outfile)

print("The python groups are: \n",Python_groups)

SEND = Email_group()
SEND.Send("Your_email_password her")   #This is not correcto password      
    
     
    

    
       
        
        