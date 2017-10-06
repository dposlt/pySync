#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "David Poslt"
__license__ = "David Poslt"
__version__ = "1.0.1"
__email__ = "david.poslt@gmail.com"
__status__ = "Develop"


### Testovaci procesy ###

import configparser
config = configparser.ConfigParser()
config.read( 'app/config.ini' )


## backup ##

# import app.bckp as bckp

# exists = bckp.Backup

# print( exists.ifDirExists( config['directory']['bckpDir'] ) ) 

## bakup end ##

## Emails ##
#ctrl k ctrl c {comments}
#ctrl k ctrl u {uncomments}
import app.emails as send
autoreply = config['emails']['autoreply'][1:-1]
print(autoreply)
#sendM = send.Email( config['emails']['title'][1:-1], config['emails']['subject'][1:-1], config['emails']['toAddress'][1:-1] , config['emails']['fromAddress'][1:-1] ,config['emails']['message'][1:-1], autoreply.encode(encoding='UTF-8',errors='strict') )
#sendM.sendEmail()
## Emails end ##


