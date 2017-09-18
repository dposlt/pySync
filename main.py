#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "David Poslt"
__license__ = "Moneta Money Bank a.s."
__version__ = "1.0.1"
__email__ = "david.poslt@moneta.cz"
__status__ = "Develop"


# #from logging import Loger
# import app.unziper as Zipper
#
# import os
# #Zipper.Zipper.unzip(os.getcwd() + '\\zipdata',os.getcwd())
# #Zipper.Zipper.unzip('zipdata','exctract')
# # def do_log():
# #     logging.info('start logging for microsites_copy')
#
# # writeLog.logger()
# import app.bckp as zaloha
#
# #zaloha.Backup.bckpFile('zipdata','archivea')
# #zaloha.Backup.ifDirExists('zipdataa','archive')

import app.emails as send

sendM = send.Email( 'Fail', 'david.poslt@moneta.cz','PySync@pysync.com','Došlo k chybě' )
sendM.sendEmail()

# 'subject: {subject} , to: {to} , from: {fromM}, message: {message} '.format( subject = showEmails.subject, to = showEmails.developEmail, fromM = showEmails.fromEmail, message = showEmails.message )