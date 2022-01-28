#Create an interface to search through system log files.
import re, sys, yaml

#Open yaml.
try: 
    with open('searchTerms.yaml', 'r') as yamlF:
        #Loads .YAML safely.
        keywords = yaml.safe_load(yamlF)
#Will stop if environment is to have errors.
except EnvironmentError as e:
    print(e.strerror)

def _sysLog(filename, service, term):
    
    #Query the yaml file for the 'term' or 'service'
    #Retrieve the strings to search on
    #terms = keywords[apache][php]
    terms = keywords[service][term]
    
    listOfKeywords = terms.split(",")
    
    #Open a file
    with open(filename) as f:
        #read the file lines
        contents = f.readlines()

    #List to store results
    results = []

    for line in contents:
        for keyword in listOfKeywords:
            #If a keyword is found in  a line:
            x = re.findall(r''+keyword+'', line)
            #It is added to results list
            for found in x:
                results.append(found)
                
    if len(results) == 0:
        ##Will display "No results found." if there is nothing in the file.
        print("No results found.")
        #Will stop program if lack of results.
        sys.exit(1)
                
    results = sorted(results)

    return results