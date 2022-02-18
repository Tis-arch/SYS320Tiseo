# File to traverse a given directory and its subdir and retrieve all files
import os, argparse, fileSearchTerms

# Obligatory parser
parser = argparse.ArgumentParser(
    description="Traverses a directory and finds attacks in web logs.",
    epilog="John Tiseo 17022022"
)

# Adds CLI arguments
parser.add_argument("-d", "--directory", required="True", help="Give us the directory for logs to look through")
parser.add_argument("-s", "--searchTerm", required="True", help="Give us the search term for the .yaml")


# Parse the arguments
args = parser.parse_args()
# Stores root directory
rootdir = args.directory
# Stores search term
searchTerm = args.searchTerm


# Walk to directory
# Check if the arg is a directory
if not os.path.isdir(rootdir):
    print("ERROR: DIRECTORY INVALID: {}".format(rootdir))
    exit()

# List to save files
fList = []

# Crawl through the directory provided
for root, subfolders, filenames in os.walk(rootdir):
    for f in filenames:
        # Get the filepath of the file
        fileList = root + "/" + f
        # Add filepath to the list
        fList.append(fileList)

# Start looking through each log file in the directory
for eachFile in fList:
    
    # check each for the specified attacks
    check = fileSearchTerms._logs(eachFile,searchTerm)

    # Results are a blank list
    results = []
    print(check)
    # This time I'm not going too spicy, just grabbing URL, Status Code and Bytes
    for eachFound in check:
        # Split results on space
        attack_cheque = eachFound.split(" ")
        results.append( "\t URL: " + attack_cheque[6] + " Status Code: " + attack_cheque[8] + " File Size (Bytes): " + attack_cheque[9])

    # Phases out dupes
    results = set(results)

    for eachValue in results:
        # Print
        print(eachValue)

        # Since a shell can execute a lot of things on its own, it's pretty risky. The main problem is being able to execute shell commands themselves.
        # I liked the assignment, I just don't like my general python illiteracy since I haven't exactly trained myself much since Python Programming.
        # None, I just need a refresher on how to fix the basic python problems. Also not to use anonymous teachers for help, they're not personal enough.