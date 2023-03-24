def containedChars(string, otherString):
    ret = True
    for c in string:
        if (otherString.find(c) == -1):
            ret = False
    
    return ret
