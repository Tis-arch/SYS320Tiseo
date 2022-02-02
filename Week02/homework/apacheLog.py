import sysLogCheck, importlib
importlib.reload(sysLogCheck)
#SSH authentication failure checking.

def apache_proc(filename, service, term):
    #Calls sysLogCheck to query the apache log.
    is_found = sysLogCheck._sysLog(filename, service, term)
    
    found = []
    
    for eachFound in is_found:
        splitResults = eachFound.split(' ')
        #Prints out the found results.
        found.append(splitResults[3] + " " + splitResults[0] + " " + splitResults[1])
        
            
    for item in set(found):
        print(item)