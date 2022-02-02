import sysLogCheck, re, importlib
importlib.reload(sysLogCheck)
#Checking Proxifier logs for QQ results.

def log_scan(filename, service, term):
    #Calls sysLogCheck to query the proxifier log.
    is_found = sysLogCheck._sysLog(filename, service, term)
    
    found = []
    
    for eachFound in is_found:
        splitResults = eachFound.split(' ')
        #Prints out the found results.
        if term == 'qqbytes' and "KB)" in splitResults[9]:
            found.append(splitResults[2] + " " + splitResults[4] + " app sent" + splitResults[6] + " has recieved" + splitResults[11])
        elif term == 'qqbytes':
            found.append(splitResults[2] + " " + splitResults[4] + " app sent" + splitResults[6] + " has recieved" + splitResults[9])
        elif term == 'qqopen':
            found.append(splitResults[2] + " opened to " + splitResults[4] + " with " + splitResults[9])
        
            
    for item in set(found):
        print(item)