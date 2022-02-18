# Had some help with this one, cleaner than I usually do...
# Changed my mindset from functions to interface since it was more of what I learned myself and also stuff I could understand a bit easier
# The first one I had help with but it was like someone showing me their notes and being like "yep understand this?"
# This was a bit more in-depth and closer to what I know.
import re, sys, yaml, re

# Function that sifts through the log and YAML file and returns results
def _logs(logFile,searchTerm):

    # Opens
    try:
        with open('searchTerms.yaml', 'r') as yf:
            keywords = yaml.safe_load_all(yf)

            # Creates list for the list of keywords to scan
            listOfKeywords = []
            for eachEntry in keywords:
                for key,value in eachEntry[searchTerm].items():
                    listOfKeywords.append(value)

            # Open the log file up
            with open(logFile) as f:

                # Reads the file and saves it to a variable as seperate lines
                contents = f.readlines()

            # List to store results
            results = []

            # Loops through the list.
            for line in contents:

                # Loops through the keywords
                for eachKeyword in listOfKeywords:

                    # Searches and returns results
                    x = re.findall("%s" %eachKeyword, line)

                    for found in x:
                        # Append the returned keywords to the results list
                        results.append(found)

            # Check to see if there are results
            if len(results) == 0:
                print("No Results")
                sys.exit(1)

            # Sorts list
            results = sorted(results)

        return results

    except EnvironmentError as e:
        print(e.strerror)