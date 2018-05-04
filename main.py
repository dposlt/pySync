#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "David Poslt"
__license__ = "David Poslt"
__version__ = "1.0.1"
__email__ = "david.poslt@gmail.com"
__status__ = "Develop"


### Testovaci procesy ###
import app.cestina as cj
cj = cj.cestina()

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
#import app.emails as send
#message = config['emails']['title'][1:-1]
#message = cj.doCeskySimple(message)
#sendM = send.Email( config['emails']['title'][1:-1], config['emails']['subject'][1:-1], config['emails']['toAddress'][1:-1] , config['emails']['fromAddress'][1:-1] ,message, cj.doCesky(config['emails']['autoreply'][1:-1]) )
#sendM = send.Email( config['emails']['title'][1:-1], config['emails']['subject'][1:-1], config['emails']['toAddress'][1:-1] , config['emails']['fromAddress'][1:-1] ,config['emails']['message'][1:-1]) )

print(message)
#sendM.sendEmail()
## Emails end ##


