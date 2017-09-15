#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# emailGroup = 'groupsEmail'
# developEmail = 'david.poslt@gmail.com'
# fromEmail = 'PySync@pysyncy.com'
#
# # Import smtplib for the actual sending function
# import smtplib, os
#
# # Import the email modules we'll need
# from email.mime.text import MIMEText
#
#
# # Create a text/plain message
# ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '\\message.txt'
# with open(ROOT_DIR, encoding = 'UTF-8') as tstMsg:
# 	msg = MIMEText(tstMsg.read())
#
#
# # me == the sender's email address
# # you == the recipient's email address
# msg['Subject'] = 'Microsites fail'
# msg['From'] = fromEmail
# msg['To'] = developEmail
#
# # Send the message via our own SMTP server.
# s = smtplib.SMTP('smtp-relay.lb.mbid.cz')
# s.send_message(msg)
# s.quit()


class Email:

	def __init__( self, groupEmail, developEmail, fromEmail ):
		self.groupEmail = groupEmail
		self.developEmail = developEmail
		self.fromEmail = fromEmail





