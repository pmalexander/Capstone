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
    with open(location.src) as csvfile
        open(fauna.src) as csvfile
        open(flora.src) as csvfile
        open(feature.src) as csvfile:
    # here we say that the file uses comma's to separate between columns
        data = csv.reader(csvfile, delimiter=our_delimiter)
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
                faunas.append(entry)
                floras.append(entry)
                features.append(entry)
            
    return location
    return fauna
    return flora
    return feature

locations = read_rawdata()

for location in locations
    print(locations)

faunas = read_rawdata()

for fauna in faunas
    print(faunas)

floras = read_rawdata()

for flora in floras
    print(flora)

features = read_rawdata()

for feature in features
#shows feature
print(feature)

"""
# guarantee that our classes have init functions that take all parameters we need to populate
class Location(object):
    def init_location(name, region, latitude, longitude, visitors, overview):
        self.name = name
        self.region = region
        self.latitude = latitude
        self.longitude = longitude
        self.vistors = visitors
        self.overview = overview


"""   