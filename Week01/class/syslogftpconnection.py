import syslogCheck
import importlib
importlib.reload(syslogCheck)

#SSH auth fail

def ssh_fail(filename, searchTerms):
    #Call syslogCheck and return results
    is_found = syslogCheck._syslog(filename,searchTerms)
    
    found = []
    #Loop through results
    for eachFound in is_found:

        #print(eachfound)
        #Split the results
        splitResults = eachFound.split(' ')
        found.append(sp_results[4])
        
    returnedValues = set(found)

    for item in set(found):
        print(item)