#!/usr/bin/python
# -*- coding: utf-8 -*-


import smtplib
from email.mime.text import MIMEText

class Email:

		def __init__( self, subject, developEmail, fromEmail, message ):
			self.subject = subject
			self.developEmail = developEmail
			self.fromEmail = fromEmail
			self.message = message


		def sendEmail( self ):
			from email.mime.text import MIMEText
			s = smtplib.SMTP( 'smtp-relay.lb.mbid.cz' )

			msg = MIMEText( self.message )
			#msg = self.message
			msg[ 'Subject' ] = self.subject
			msg[ 'From' ] = self.fromEmail
			msg[ 'To' ] = self.developEmail
			s.send_message(msg)
			s.quit()

