#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from app import logger
class Backup:

    def ifFileExists(nameFile):
        if os.path.isfile(nameFile):
            return True
        
    def ifDirExists(*fdir):
        for dirs in fdir:
            if os.path.isdir(dirs) and os.path.isdir(dirs):
                return True                   
            else:
                print ( 'not found dir {nameOfDir} '.format(nameOfDir = dirs))
        
            '''
                if os.path.isdir(dirs):
                    return True #po tomto se jiz nevykona else | opravit
                else:
                    logger.Loger.writeLog('Dir %s is not exists' % dirs)
               '''     
                    
        
    def bckpFile(source, desc):
        if Backup.ifDirExists(source,desc):
            for name in os.listdir(source):
                filename = source+'\\'+name
                if Backup.ifFileExists(filename):
                    print(name)
                else:
                    print(filename, 'is not a file')
        else:
            logger.Loger.writeLog('Backup nothing to do')
        


                    
