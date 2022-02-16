# Had some help with this one, cleaner than I usually do...
# A number of functions made to scan a directory for attack data.
import os, yaml, re

def directoryTraversal(dir):
    
    """Function that finds a directory and returns a file list."""
    
    # Check if argument is a directory
    
    if not os.path.isdir(dir): 
        print("ERROR: DIRECTORY INVALID => {}".format(dir))
        exit()

    # List to save file to.
    fList = [] 

    # Crawling through directory
    for root, subfolders, filenames in os.walk(dir):
        for f in filenames:
            filePath = root + "/" + f
            fList.append(filePath)

    return(fList)
# Function that parses a .yaml file.
def yamlParse(yamlfile):
    """ Parsing .YAML file """
    # Opens file
    try: 
        with open(yamlfile, 'r') as yamlF:
            # Safely loads .yaml files
            keywords = yaml.safe_load(yamlF)

    except EnvironmentError as e:
        print(e.strerror)
    return keywords
def logScan(filename, searchTerms, book):
    """Scans log file and searches for your term."""
    # Query .yaml file for the terms in each .yaml book to retrieve the strings to search
    #terms = keywords[book]
    terms = searchTerms[book]

    #Open a file
    with open(filename) as f:
        # Reads file lines
        contents = f.readlines()

    # List to save results to.
    results = []

    # Scans each line for each .yaml entry
    for line in contents:
        for attack in terms:
            # If keyword is in line:
            x = re.findall(r''+terms[attack]+'', line)
            # Adds it to the found array for later parsing
            # in other modules
            for found in x:
                results.append(line)
                
    results = sorted(results)

    return results

def returnResults(string):
    """Returning your results..."""
    sR = string.split(" ")
    print("""
    Time: {}{}\n
    URL: {}\n
    Status Code: {}\n
    File Size (Bytes): {}\n
    Sauce: {}\n
    {}
    """.format(sR[3].strip("["),sR[4].strip("]"), sR[6], sR[8], sR[9], sR[0], "*"*60).strip("\n"))