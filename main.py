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

showEmails = send.Email( 'groupsEmail','david.poslt@gmail.com','PySync@pysync.com' )
print( 'group: {groups} , to: {to} , from: {fromM} '.format( groups = showEmails.groupEmail, to = showEmails.developEmail, fromM = showEmails.fromEmail )  )
