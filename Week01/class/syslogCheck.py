#was rushing through this portion, installs bugged and got hectic
#Interface to use for searching through system log (.log) files.
import re

def _syslog(filename,listOfKeywords):

    #Open file here
    with open(filename) as f:

        #Read file contents, ability to save them as variable.
        contents = f.readlines()

#Keywords of interest stored in variable for automation and ease of observation of .log file.
keywords = ['failure','session opened for user.*','exited abnormally','sshd\(pam_unix\)\[[0-9]{3,8}\]: authentication failure;',]

#Loop through retuned log file contents. Each element is a line from the smallSyslog file.
for line in contents:
    #Keywords are sifted through to pluck out lines of interest.
    for eachKeyword in listOfKeywords:

    #Search for specific terms in .log file by modifying contents of eachKeyword's keywords.
        #if eachKeyword in line:
        #Searches and returns using regular expressions, wowie!
        x= re.findall(r''+eachKeyword+'', line)
        results.append(found)

    #Check for results
    if len(results) == 0:
        print("No Results")
        sys.exit(1)

    #Sort the list
    results = sorted(results)

    return results
# print(x)