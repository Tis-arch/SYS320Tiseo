# This searches through the provided yaml file and extracts the keywords and returns them as a list
import yaml

# Take logfile and searchterm and return list
def logOpen(term):
    listOfKeywords = []
    # Open the searchTerms.yaml file
    try:
        with open('searchTerms.yaml', 'r') as yf:
            keywords = yaml.safe_load_all(yf)
            # Create list for the list of keywords to search
            for eachEntry in keywords:
                for key,value in eachEntry[term].items():
                    listOfKeywords.append(value)

    except EnvironmentError as e:
        print(e.strerror)
    return listOfKeywords
