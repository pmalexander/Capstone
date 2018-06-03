#can be opened in excel, remember
import csv

def read_rawdata(path, our_delimiter=','):
    firstTime = True
    header = None
    location = []
    fauna = []
    flora = []
    feature = []
# this code opens a file comma separated #CREATE OTHER SRC FILES FOR FLORA, FAUNA, AND FEATURE
    with open('location.src', 'fauna.src', 'flora.src', 'feature.src') as csvfile:
        # here we say that the file uses comma's to separate between columns
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            if firstTime == True:
                # we want to capture the first row independently to ensure we can build the dictionary
                header = row
                # once we captured the headers/first row, we no longer need this code, so we disable the flag
                firstTime = False
            else:
                # for every other non header row, we collect one line, where one line means one location
                count = 0 # we keep track of count so we can access the fields positions in rows
                entry = {} # create an empty dictionary
                for title in header:
                    # create a dictionary entry where the key is the "header" and the value is the row content
                    entry[title] = row[count]
                    # show us how does that look like
                    print("{}:{}".format(title, row[count]))
                    # next time it will be a different header(name, region etc)
                    # so we update count to be able to access a different column in the row
                    count += 1
                # we have collected a full entry, we store it in a list, so we can process it later with sqlalchemy
                location.append(entry)
                fauna.append(entry)
                flora.append(entry)
                feature.append(entry)
    #return list            
    return(location, fauna, flora, feature)
