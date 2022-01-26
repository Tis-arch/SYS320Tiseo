import sysLogCheck
import importlib
importlib.reload(sysLogCheck)
#Program will detect when Klogin in linux log provided successful SSH logins.

def ssh_success(filename, searchTerms):
    #Finds the file and terms needed to search from sysLogCheck
    is_found = sysLogCheck._syslog(filename,searchTerms)
    #Puts found terms in a list.
    found = []
    
    #Takes out SSH IDs
    for eachFound in is_found:
        splitResults = eachFound.split(' ')
        found.append(splitResults[5])
        
            
    for item in set(found):
        print(item)