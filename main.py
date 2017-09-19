#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "David Poslt"
__license__ = "David Poslt"
__version__ = "1.0.1"
__email__ = "david.poslt@gmail.com"
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
import configparser

config = configparser.ConfigParser()
config.read( 'app/config.ini' )


sendM = send.Email( 'Microsites sync', config['emails']['toAddress'][1:-1] , config['emails']['fromAddress'][1:-1] ,'Při přenosu dat na microsites server došlo k chybě, kontaktujte administrátora' )
sendM.sendEmail()
