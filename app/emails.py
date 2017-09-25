#!/usr/bin/python
# -*- coding: utf-8 -*-


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Email:

		def __init__( self, title, subject, developEmail, fromEmail, message ):
			self.subject = subject
			self.developEmail = developEmail
			self.fromEmail = fromEmail
			self.message = message


		def sendEmail( self ):
			from email.mime.text import MIMEText
			s = smtplib.SMTP( 'smtp-relay.lb.mbid.cz' )

			msg = MIMEMultipart('alternative')
			
			
			msg[ 'Subject' ] = self.subject
			msg[ 'From' ] = self.fromEmail
			msg[ 'To' ] = self.developEmail

			html = """
				<html>
				<head></head>
				<body>
					<table style="background-color: #ff0000;">
					<tr bgcolor="red"><td><center>""" + self.title + """</center></td></tr>
					<tr bgcolor="yellow"><td><b><center> """ + self.message + """</center></b></td></tr>
					</table>
				</body>
				</html>
				"""
			msgHtml = MIMEText( html, 'html' )
			msg.attach( msgHtml )
			#s.sendmail( self.developEmail,self.fromEmail, msg.as_string() )
			s.send_message(msg)
			s.quit()

