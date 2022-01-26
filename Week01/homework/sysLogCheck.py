#Create and interface to search through syslog files
import re
import sys

def _syslog(filename,listOfKeywords):
    
    #Open a file
    with open(filename) as f:
        #Reads the file, segmented by each line.
        contents = f.readlines()

    #List to store results
    results = []

    for line in contents:
        for keyword in listOfKeywords:
            #If a keyword is found in a line...
            x = re.findall(r''+keyword+'', line)
            
            #It is added to the results list.
            for found in x:
                results.append(found)
                
                
    if len(results) == 0:
        #Will display "No Results" if there is nothing in the file.
        print("no results")
        #Will stop program on lack of results.
        sys.exit(1)
                
    results = sorted(results)

    return results