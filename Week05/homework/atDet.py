import os, argparse, re

# Imports YAML reading file
import yamlSearch

# Import file that looks for sus activity
import csvSearch

# El Parser
parser = argparse.ArgumentParser(
    description="Traverses a directory and finds attacks or attempted attacks in logs",
    epilog="Developed by John Tiseo 20220119"
)

# add argument to pass to the fs.py program
parser.add_argument("-d", "--directory", required="True", help="Directory of the logs to look through")
parser.add_argument("-s", "--searchTerm", required="True", help="The search term from the yaml file")


# Parse the arguments
args = parser.parse_args()
# Variable that stores root directory
rootdir = args.directory
# Variable that stores search term
searchTerm = args.searchTerm

# Check if the argument is a directory
if not os.path.isdir(rootdir):
    print("Invalid directory: %s".format(rootdir))
    exit()

# List to save files to
fList = []

# Crawl through the provided directory
for root, subfolders, filenames in os.walk(rootdir):
    for f in filenames:
        # Get the file's path
        fileList = root + "/" + f
        # Adds file's path to flist
        fList.append(fileList)

# Start looking through each log file in the directory
keywords = []
for eachFile in fList:

    # Gets keywords from YAML file
    keywords = yamlSearch.logOpen(searchTerm)

    # Loads CSV and stores spliced results
    results = csvSearch.logOpen(eachFile,keywords[1:])

    # print out results if there was a match found
    if len(results) > 0:
        for results in results:
            print(
                """

%s From file %s :

Hostname: %s
Program: %s
Path: %s
User: %s
PID: %s
Args: %s
        """.format(searchTerm,eachFile, keywords[0], results[2],results[3], results[6],results[5],results[1]))
