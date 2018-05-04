class cestina:
    def doCesky(self, *codeString):
        for s in codeString:
            s.encode('mbcs').decode('utf-8')
            
        return s

    def doCeskySimple( self, codeString ):
        codeString = codeString.encode('mbcs').decode('utf-8')
        return codeString
