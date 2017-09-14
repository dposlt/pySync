import zipfile, os
from app import logger

class Zipper:
    def unzip(source, desc):
        chDir = os.chdir(source)
        
        for nameZip in os.listdir(chDir):
            if zipfile.is_zipfile(nameZip):
               logger.Loger.writeLog('Start unpacking ' + nameZip +' file')
               
               with zipfile.ZipFile(nameZip, 'r') as myzip:
                   myzip.extractall(desc+'\\'+nameZip.strip('.zip'))
                   logger.Loger.writeLog('Unpacking done')
