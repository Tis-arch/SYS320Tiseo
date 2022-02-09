# Imports csv and re, which is in the code and needed for findall
import re, csv
# Creates urlHausOpen function
def urlHausOpen(filename, searchTerm):
    # Opens file and stores it as variable number, and stores contents in contents using csv.review
    with open(filename) as f:
        # Reader is the correct function, and we're using f, not filename
        contents = csv.reader(f)
        # Skips comments
        for _ in range(9):
            next(contents)
        # Finds keywords
        for keyword in searchTerm:
        # Searches through all keywords found
            for eachLine in contents:
                # Searches for specific keywords
                x = re.findall(r"\." + keyword, eachLine[2])
                # In earch part of lines found in file (x)
                for _ in x:
                # Don't edit this line. It is here to show how it is possible
                # to remove the "tt" so programs don't convert the malicious
                # domains to links that an be accidentally clicked on.
                    the_url = eachLine[2].replace("http", "hxxp")
                    the_src = eachLine[4]
                    # Prints details
                    print(""" 
                    URL: %s 
                    Info: %s 
                    %s """ % (the_url, the_src, "*"*60))