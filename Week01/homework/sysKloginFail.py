import sysLogCheck
import sys
import importlib
importlib.reload(sysLogCheck)
#Program will detect when Klogin in linux log provided fails.

def klogin_failure(filename, searchTerms):
    #Finds the file and terms needed to search from sysLogCheck
    is_found = sysLogCheck._syslog(filename,searchTerms)
    #Puts found terms in a list.
    found = []
    
    for eachFound in is_found:
        splitResults = eachFound.split(' ')
        #Will cleanly output results and failure reason
        found.append("%s. Failure reason: %s %s" % (splitResults[4], splitResults[6], splitResults[7]))
        
    for item in set(found):
        print(item)