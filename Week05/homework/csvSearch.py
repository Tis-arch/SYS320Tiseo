import csv, re

def logOpen(filename,searchTerms):

    try:
        # Stores file as f
        with open(filename) as f:

            # Reads through contents with reader and stores as f
            contents = csv.reader(f)

            # List to store the results
            results = []
            # Loops through each line
            for eachLine in contents:
                # Loop through each keyword
                for keyword in searchTerms:
                    # search with regex and store with x
                    x = re.findall(r''+keyword+'', eachLine[1])

                    for found in x:
                        # Adds to whole line that gets parsed for the important stuff later on
                        results.append(eachLine)

    except EnvironmentError as e:
        print(e.strerror)

    return results